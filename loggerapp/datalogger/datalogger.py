#################################################################################################
"""datalogger.py holds the main exporter tools for the sensors specified in sensorconfig.xml"""
#################################################################################################


import datalogger.analyser as analyser
import datalogger.cameras as cam
import datalogger.trigger as trig
from datalogger.logsetup import log
import numpy as np
from xml.dom import minidom
import xml.etree.ElementTree as ET
import ctypes
import os
import nidaqmx


#################################################################################################


DLLPATH = os.getcwd() + r'\loggerapp\datalogger\usbtc08.dll'


class Exporter:
    """Abstract Exporter class, capable of exporting data to influx format"""
    def __init__(self,type,sensor,trigger):
        self.type=type
        self.trigger=trigger
        self.sensor=sensor        
        
    def getdata(self):
        #in subclasses this will give the wanted result in a library
        pass

    
    def exporttoinflux(self):
        dat=self.getdata()
        if dat is not None:
            tags={}
            tags["sensor"]=self.sensor
            library={"measurement": self.type,"tags": tags,"fields": dat}
            exp=[]
            exp.append(library)
            return exp

        else:
            return None
            

    
    

class Camexp:
    """Class to connect to cameras"""
    def __init__(self,vendor,camid,cameras):
        self._vendor=vendor
        self._camid=camid
        self._cammngr = cam.CameraManager(cameras)
        self.startcam()
        
    
    def getcammanager(self):
        return self._cammngr
    def getanimage(self):
        return self._cammngr.getimage()
    
    def camstr(self):
        return self._vendor + " " + self._camid
    
    def selectacam(self):
        """Select cam in camera manager"""
        self._cammngr.setactivecam(self._vendor,self._camid)
    
    
    def startcam(self):
        """Start the active cam"""
        if not self._cammngr.isaquiring:
            self.selectacam()
            self._cammngr.start()
            
    def stopcam(self):
        """Stop the active cam"""
        if self._cammngr.isaquiring:
            self._cammngr.stop()
    

  
    
class Beam(Exporter):
    """Class for beam sensors, which have their own ROI settings and fit output datas"""
    def __init__(self,cam,beam,roiparams,trigger):
            self._cam=cam
            tpe=self._cam.camstr() + " " + str(beam)
            super(Beam, self).__init__("camera",tpe,trigger)
            self.latestimage=None
            self.latestroi=None
            self.latestroiparams=None
            self.IA=analyser.ImageAnalyser()
            self.IA.roiposx = roiparams[0]
            self.IA.roiposy = roiparams[1]
            self.IA.roiimgwidth = roiparams[2]
            self.IA.roiimgheight = roiparams[3]
            self.IA.pixelsize=self.getcamman().pixelsize
            if self.getcamman().isaquiring:
                self.IA.isrecording=True
            else:
                log.warning("Camera " + self._cam.camstr() + " is not recording")
     
    def getcamman(self):
        return self._cam.getcammanager()

                
    def getdata(self):        
        """Exports data field in dictionary format"""        
        if self.getcamman().hasimages:            
            self.IA.image=self._cam.getanimage()            
            try:
                self.IA.setroi()                       
            except:
                log.error('Could not set ROI of sensor %s, %s.' % (self.type,self.sensor))                           
            try:
                fitdata=self.IA.getfitdata()
                if not None in fitdata:
                    #first safes the latest image for fit data to be in sync with live cam view
                    self.latestimage=self.IA.image
                    self.latestroi=self.IA.roiimage
                    self.latestroiparams=(self.IA.roiposx,self.IA.roiposy,self.IA.roiimgwidth,self.IA.roiimgheight)
                    #then proceeds to return field values such as fit data and roi params in directionary format
                    lib={}
                    lib["hcenter"]=fitdata[0]
                    lib["vcenter"]=fitdata[1]
                    lib["largewaist"]=fitdata[2]
                    lib["smallwaist"]=fitdata[3]
                    lib["angle"]=fitdata[4]
                    return lib
                else:
                    if fitdata[0]==None:
                        log.error('Error while fitting horizontal position of sensor %s, %s.' % (self.type,self.sensor))
                    if fitdata[1]==None:
                        log.error('Error while fitting vertical position of sensor %s, %s.' % (self.type, self.sensor))
                    if fitdata[2]==None:
                        log.error('Error while fitting large waist of sensor %s, %s.' % (self.type,self.sensor))
                    if fitdata[3]==None:
                        log.error('Error while fitting small waist of sensor %s, %s.' % (self.type,self.sensor))
                    if fitdata[4]==None:
                        log.error('Error while fitting angle of sensor %s, %s.' % (self.type,self.sensor))
                    return None
            except:
                log.error('Could not aquire fit data of sensor %s, %s.' % (self.type,self.sensor))
                return None
        else:
            return None
            
    
     
    
    
class Temperature(Exporter):
    """Class for temperature sensors"""
    def __init__(self,dll,handle,tempid,tempsensors,trigger,channellist):
        if handle in tempsensors:
            super(Temperature, self).__init__("temperature",str(tempid),trigger)
            self._dll=dll
            self._handle=handle
            self._channellist=channellist
        else:
            log.error('No temperature sensor with the handle %s is connected.' % (handle))
        
    
    def getdata(self):        
        """Exports data field in dictionary format"""
        hand=int(self._handle)
        mydll = self._dll
        temp = np.zeros( (10,), dtype=np.float32)
        overflow_flags = np.zeros( (1,), dtype=np.int16)     
        mydll.usb_tc08_set_mains(hand,50)
        mydll.usb_tc08_set_channel(hand, 0, 0 )
        tc_type=ord('K')
        for i in range(1,9):
            mydll.usb_tc08_set_channel(hand,i,tc_type)
        mydll.usb_tc08_get_single(hand, temp.ctypes.data, overflow_flags.ctypes.data, 0)
        

        lib={}
        
        for i in range(0,9):
            st=self._channellist[i]
            lib[st]=temp[i]
            
        return lib




class NIAnalog(Exporter):
    """Class for NI analog power sensors"""
    def __init__(self,dev,trigger,channellist):
        super(NIAnalog, self).__init__("nianalog",dev,trigger)
        self._devstring = dev
        self._channellist=channellist
        
        
    def getdata(self):
        """Export data field in dictionary format"""
        lib={}
        for i in range(0,6):
            channelstring = self._devstring + "/ai" + str(i)
            with nidaqmx.Task() as task:
                task.ai_channels.add_ai_voltage_chan(channelstring)
                output=task.read()
            lib[self._channellist[i]]=output
        return lib
        
    
    
    
    
    
    
    
        
class Sensormanager:
    """This class reads the config file 'sensorconfig.xml' and initiates all sensors."""
    def __init__(self):
        
        self._camtypes=self._initiatecamlist()
        
        self._connectedcams=self._connectedcams()
        
        self._connectedtemp=self._initiatetemplist()
        
        self._connectedni=self._initiateni()
        
        self._paramlist=self._paramfromfile()
        
        self._triggerconf=self._triggerfromfile()
        
        self._tobeconfigured=self._getmissingsensors()
        
        self._overlyconfigured=self._getnonconnectedsensors()
        
        #Rewrite sensorxml file
    
        for ov in self._overlyconfigured.keys():
            if ov=="camera":
                for cam in self._overlyconfigured[ov]:
                    log.info("The connected camera %s %s is mentioned in sensorconfig.xml and yet does not seem to be connected." % cam)
                    delnow=input("Delete camera %s %s from sensorconfig.xml? (y/n)" % cam)
                    if delnow=="y":
                        self._delcamerasensorfromxml(cam[0],cam[1])
                        log.info("Camera %s %s was deleted from sensorconfig.xml." % cam)
            if ov=="temperature":
                for temp in self._overlyconfigured[ov]:
                    log.info("The connected temperature sensor %s is mentioned in sensorconfig.xml and yet does not seem to be connected." % temp)
                    delnow=input("Delete temperature sensor with the handle %s from sensorconfig.xml? (y/n)" % temp)
                    if delnow=="y":
                        self._deltempsensorfromxml(temp)
                        log.info("Temperature sensor with the handle %s was deleted from sensorconfig.xml." % temp)
            if ov=="nianalog":
                for ni in self._overlyconfigured[ov]:
                    log.info("The connected national instruments sensor %s is mentioned in sensorconfig.xml and yet does not seem to be connected." % ni)
                    delnow=input("Delete national instruments sensor with the devstring %s from sensorconfig.xml? (y/n)" % ni)
                    if delnow=="y":
                        self._delnisensorfromxml(ni)
                        log.info("National instruments sensor with the handle %s was deleted from sensorconfig.xml." % ni)

            
            
        for miss in self._tobeconfigured.keys():
            if miss=="camera":
                for cam in self._tobeconfigured[miss]:
                    log.info("The connected camera %s %s is not yet configured in sensorconfig.xml." % cam)
                    configurenow=input("Configure %s %s now? (y/n) "% cam)
                    if configurenow=="y":
                        nobeams=input("How many beams are tracked with this camera? ")
                        try:
                            beamlist=range(int(nobeams))
                        except:
                            log.error("Bad input. Config process stopped.")
                            break
                        
                        for beam in beamlist:
                            beamname=input("What name should beam number %i be logged as? " % (beam+1))
                            self._addcamerasensortoxml(cam[0],cam[1],beamname,"(0,0,100,100)")
            if miss=="temperature":
                for temp in self._tobeconfigured[miss]:
                    log.info("The connected temperature sensor with the handle %s is not yet configured in sensorconfig.xml." % temp)
                    configurenow=input("Configure %s now? (y/n) " % temp)
                    if configurenow=="y":
                        tempid=input("What name should this sensor be logged as? ")
                        defaultlist=[]
                        for i in range(0,9):
                            st='Channel '+ str(i+1)
                            defaultlist.append(st)
                        self._addtempsensortoxml(tempid,miss,defaultlist)
            if miss=="nianalog":
                for ni in self._tobeconfigured[miss]:
                    log.info("The connected national instruments sensor with the devstring %s is not yet mentioned in sensorconfig.xml. " % ni)
                    configurenow=input("Configure %s now? (y/n) " % ni)
                    if configurenow=="y":
                        defaultlist=[]
                        for i in range(0,6):
                            st='Channel '+ str(i+1)
                            defaultlist.append(st)
                        self._addnisensortoxml(ni,defaultlist)
                        
            
        #Reread edited xml file
        self._paramlist=self._paramfromfile()
        
        self._tobeconfigured=[]
        
        self._overlyconfigured=[]          
        
        self._connectedcamexp=self._initiatecamexpdict()
        
        self._sensorlist=self._initiatesensorlist()
        
        self._sensordict=self._initiatesensordict()
        
        
    
    def _initiatecamlist(self):
        """Finds and initiates all available camera vendors and returns a list of said camtypes."""
        cameras = []
        dummycam = cam.DummyCamera()
        cameras.append(dummycam)
        try:
            vrmmagic = cam.VrmCamera()
            cameras.append(vrmmagic)
        except:
            log.warning('No VRMagic driver installed')
        try:
            xiapi = cam.XiapiCamera()
            cameras.append(xiapi)
        except:
            log.warning('No xiapi driver installed')
        try:
            avt = cam.VimbaCamera()
            cameras.append(avt)
        except:
            log.warning('No AVT/vimba driver installed')
        try:
            ueyecam = cam.UEyeCamera()
            cameras.append(ueyecam)
        except:
            log.warning('No UEye driver installed')
        return cameras
        
        
    def _connectedcams(self):
        """Finds all connected cameras, and returns list of tuples (vendor,camid)."""
        mangr=cam.CameraManager(self._camtypes)
        a=mangr.connectedcams
        b=[]
        for i in a.keys():
            for j in a[i].keys():
                iout=str(i)
                jout=str(j)
                b.append((iout,jout))
        return b
        
    
    
    def _initiatetemplist(self):  
        """Uses DLL in order to find an connect to all temperature handles. Returns list for said handles."""
        try:
            mydll = ctypes.windll.LoadLibrary(DLLPATH)
        except:
            log.error('Failed to load DLL file usbtc08.dll')
            return None
        id=1
        templist=[]
        devlist=[]
        while id!=0:
            id=mydll.usb_tc08_open_unit() #Returns device handle, or 0 if no device was found, or -1 if an error occured
            if id!=-1:
                if id!=0:
                    log.info("Temperature sensor of handle %i encountered." % id)
                    templist.append(str(id))
                    devlist.append(id)
            else:
                err=mydll.usb_tc08_get_last_error(0)
                if err==1:
                    log.error('Failed to connect to temperature sensor: USBTC08_ERROR_OS_NOT_SUPPORTED')
                if err==2:
                    log.error('Failed to connect to temperature sensor: USBTC08_ERROR_NO_CHANNELS_SET')
                if err==3:
                    log.error('Failed to connect to temperature sensor: USBTC08_ERROR_INVALID_PARAMETER')
                if err==4:
                    log.error('Failed to connect to temperature sensor: USBTC08_ERROR_VARIANT_NOT_SUPPORTED')
                if err==5:
                    log.error('Failed to connect to temperature sensor: USBTC08_ERROR_INCORRECT_MODE')
                if err==6:
                    log.error('Failed to connect to temperature sensor: USBTC08_ERROR_ENUMERATION_INCOMPLETE')
                break
        
            
        return templist
           
    
    
    def _initiateni(self):
        """Finds all nidaqmx devices and returns device key."""
        try:
            system = nidaqmx.system.System.local()
            devlist = system.devices
            devstrlist=[]
            for device in devlist:
                devstrlist.append(device.name)
                log.info("NI device with the devstring %s was encountered." % device.name)
            return devstrlist
        except:
            return []
        
        
        
    
    def _paramfromfile(self):
        """Reads XML file and creates dictionary for parameters."""
        xmldoc = minidom.parse('sensorconfig.xml')
        sensorlist = xmldoc.getElementsByTagName('sensor')
        paramlist=[]
        for sensor in sensorlist:
            r={}
            r['type']=sensor.getElementsByTagName('type')[0].firstChild.nodeValue
            att=sensor.getElementsByTagName('parameters')[0].attributes
            if r['type']=='camera':        
                r['vendor']=att['vendor'].value
                r['camid']=att['camid'].value
                r['beam']=att['beam'].value
                r['roiparams']=att['roiparams'].value
            elif r['type']=='temperature':
                r['tempid']=att['tempid'].value
                r['handle']=att['handle'].value
                for i in range(0,9):
                    keystr='channel'+ str(i+1)
                    r[keystr]=att[keystr].value
            elif r['type']=='nianalog':
                r['devstr']=att['devstr'].value
                for i in range(0,6):
                    keystr='channel'+ str(i+1)
                    r[keystr]=att[keystr].value
            paramlist.append(r)
        return paramlist
    
    
    
    def _triggerfromfile(self):
        """Reads XML file and returns tuple with (periodic trigger, national trigger)."""
        xmldoc = minidom.parse('triggerconfig.xml')
        triggerlist = xmldoc.getElementsByTagName('trigger')
        triggerdict={}
        for trigger in triggerlist:
            triggertype=trigger.getElementsByTagName('type')[0].firstChild.nodeValue
            att=trigger.getElementsByTagName('parameters')[0].attributes
            if triggertype=='national':
                triggerdict['national']=trig.NationalTrigger(att['channel'].value,float(att['threshhold'].value),float(att['timeout'].value))
            if triggertype=='periodic':
                triggerdict['periodic']=trig.PeriodicTrigger(float(att['rate'].value),float(att['timeout'].value))
        return triggerdict
    
    
    
    
    def _initiatecamexpdict(self):
        """Returns dictionary of Camexp objects corresponding to cameras in the paramlist."""
        camexps = {}
        for pardic in self._paramlist:
            if pardic['type']=='camera':
                if not (pardic['vendor'],pardic['camid']) in camexps.keys():
                    camexps[(pardic['vendor'],pardic['camid'])] = Camexp(pardic['vendor'],pardic['camid'],self._camtypes)
        return camexps
    
    
        
    def _initiatesensorlist(self):
        """Initiates a list of sensors with the specified parameters in sensorconfig.xml."""
        ret=[]        
        for par in self._paramlist:
            if par['type']=='camera':
                roipar=eval(par['roiparams'])
                ret.append(Beam(self._connectedcamexp[(par['vendor'],par['camid'])],par['beam'],roipar,'national'))
            if par['type']=='temperature':
                channellist=[]
                for i in range(0,9):
                    keystr='channel' + str(i+1)
                    channellist.append(par[keystr])    
                ret.append(Temperature(ctypes.windll.LoadLibrary(DLLPATH),par['handle'],par['tempid'],self._connectedtemp,'periodic',channellist))
            
            if par['type']=='nianalog':
                if par["devstr"] in self._connectedni:
                    channellist=[]
                    for i in range(0,6):
                        keystr='channel' + str(i+1)
                        channellist.append(par[keystr])
                    ret.append(NIAnalog(par["devstr"],'national',channellist))
                else:
                    log.error("The NI device with the devkey %s does not seem to be connected." % par["devstr"])
                
        
        return ret
    
    
    
    def _initiatesensordict(self):
        nationallist=[]
        periodiclist=[]
        
        for sensor in self._sensorlist:
            if sensor.trigger=='national':
                nationallist.append(sensor)
            if sensor.trigger=='periodic':
                periodiclist.append(sensor)
                
        return {self._triggerconf['national']:nationallist, self._triggerconf['periodic']:periodiclist}
    

    def getcameraliststring(self):
        """Returns list of strings for all cameras following the logic type + sensor."""
        st=[]
        for sensor in self._sensorlist:
            if sensor.type=='camera':
                st.append(sensor.sensor)
        return st    
    
    
    def gettemperatureliststring(self):
        """Returns list of strings for all temperature sensors."""
        st=[]
        for sensor in self._sensorlist:
             if sensor.type=='temperature':
                    st.append(sensor.sensor)
        return st
                 
                
    def getsensorlist(self):
        return self._sensorlist
    
    def getsensordict(self):
        return self._sensordict    
    
    def getperiodiclist(self):
        l=[]
        for sensor in self._sensorlist:
            if sensor.trigger=="periodic":
                l.append(sensor)
        return l
    
    
    def _getnonconnectedsensors(self):
        """Get all sensors, which are specified in sensorconfig.xml, yet not connected."""
        currentcams=[]
        currenttemp=[]
        currentni=[]
        overcams=[]
        overtemp=[]
        overni=[]
        for par in self._paramlist:
            if par["type"]=="camera":
                currentcams.append((par["vendor"],par["camid"]))
            if par["type"]=="temperature":
                currenttemp.append(par["handle"])
            if par["type"]=="nianalog":
                currentni.append(par["devstr"])
        
        currentcamsset=set(currentcams)
        currenttempset=set(currenttemp)
        currentniset=set(currentni)
        
        if not self._connectedcams is None:
            camintersection=currentcamsset.intersection(self._connectedcams)
            for cam in list(camintersection):
                currentcamsset.remove(cam)

        if not self._connectedtemp is None:
            tempintersection=currenttempset.intersection(self._connectedtemp)
            for temp in list(tempintersection):
                currenttempset.remove(temp)
                
        if not self._connectedni is None:
            niintersection=currentniset.intersection(self._connectedni)
            for ni in list(niintersection):
                currentniset.remove(ni)
        
        missing={"camera":list(currentcamsset),"temperature":list(currenttempset),"nianalog":list(currentniset)}
        
        return missing
        
    
    def _getmissingsensors(self):
        """Get all connected sensors, which are not specified in sensorconfig.xml"""
        currentcams=[]
        currenttemp=[]
        currentni=[]
        missingcams=[]
        missingtemp=[]
        missingni=[]
        for par in self._paramlist:
            if par["type"]=="camera":
                currentcams.append((par["vendor"],par["camid"]))
            if par["type"]=="temperature":
                currenttemp.append(par["handle"])
            if par["type"]=="nianalog":
                currentni.append(par["devstr"])
                
        for cam in self._connectedcams:
            if not cam in currentcams:
                missingcams.append(cam)
        if not self._connectedtemp is None:
            for temp in self._connectedtemp:
                if not temp in currenttemp:
                    missingtemp.append(temp)
        if not self._connectedni is None:
            for ni in self._connectedni:
                if not ni in currentni:
                    missingni.append(ni)
        missing={"camera":missingcams, "temperature":missingtemp,"nianalog":missingni}
        return missing
        
        
    def _addcamerasensortoxml(self,vendor,camid,beam,roiparams):
        """Edits sensorconfig.xml to add a camera with the specified params."""
        et = ET.parse('sensorconfig.xml')
        new_sensor_tag = ET.SubElement(et.getroot(), 'sensor')
        type_tag = ET.SubElement(new_sensor_tag, 'type')
        type_tag.text = "camera"
        param_tag = ET.SubElement(new_sensor_tag, 'parameters')
        param_tag.attrib = {'vendor':vendor,'camid':camid,'beam':beam,'roiparams':roiparams}
        rough_string = ET.tostring(et.getroot(), 'utf-8')
        rough_string = rough_string.replace(b"\n",b"")
        rough_string = rough_string.replace(b"\t",b"")
        rough_string = rough_string.replace(b"  ",b"")
        reparsed = minidom.parseString(rough_string)
        new_string = reparsed.toprettyxml(indent="\t")
        f=open('sensorconfig.xml','w')
        f.write(new_string)
        f.close()
        
    def _addtempsensortoxml(self,tempid,handle,channelnamelist):
        """Edits sensorconfig.xml to add a temperature sensor with the specified params."""
        et = ET.parse('sensorconfig.xml')
        new_sensor_tag = ET.SubElement(et.getroot(), 'sensor')
        type_tag = ET.SubElement(new_sensor_tag, 'type')
        type_tag.text = "temperature"
        param_tag = ET.SubElement(new_sensor_tag, 'parameters')
        param_tag.attrib = {'tempid':tempid,'handle':handle}
        for i in range(0,9):
            keystr='channel' + str(i+1)
            param_tag.attrib[keystr]=channelnamelist[i]
        rough_string = ET.tostring(et.getroot(), 'utf-8')
        rough_string = rough_string.replace(b"\n",b"")
        rough_string = rough_string.replace(b"\t",b"")
        rough_string = rough_string.replace(b"  ",b"")
        reparsed = minidom.parseString(rough_string)
        new_string = reparsed.toprettyxml(indent="\t")
        f=open('sensorconfig.xml','w')
        f.write(new_string)
        f.close()
       
    def _addnisensortoxml(self,devstr,channelnamelist):
        """Edits sensorconfig.xml to add a national instruments sensor with devstring devstr."""
        et = ET.parse('sensorconfig.xml')
        new_sensor_tag = ET.SubElement(et.getroot(), 'sensor')
        type_tag = ET.SubElement(new_sensor_tag, 'type')
        type_tag.text = "nianalog"
        param_tag = ET.SubElement(new_sensor_tag, 'parameters')
        param_tag.attrib = {'devstr':devstr}
        for i in range(0,6):
            keystr='channel' + str(i+1)
            param_tag.attrib[keystr]=channelnamelist[i]
        rough_string = ET.tostring(et.getroot(), 'utf-8')
        rough_string = rough_string.replace(b"\n",b"")
        rough_string = rough_string.replace(b"\t",b"")
        rough_string = rough_string.replace(b"  ",b"")
        reparsed = minidom.parseString(rough_string)
        new_string = reparsed.toprettyxml(indent="\t")
        f=open('sensorconfig.xml','w')
        f.write(new_string)
        f.close()
    
    def _delcamerasensorfromxml(self,vendor,camid):
        """Edits sensorconfig.xml to delete camera with specified params."""
        et = ET.parse('sensorconfig.xml')
        for sensor in et.findall('sensor'):
            for sub in sensor.findall('type'):
                if sub.text=='camera':
                    for subel in sensor.findall('parameters'):
                        if subel.attrib['vendor']==vendor and subel.attrib['camid']==camid:
                            et.getroot().remove(sensor)

        rough_string = ET.tostring(et.getroot(), 'utf-8')
        rough_string = rough_string.replace(b"\n",b"")
        rough_string = rough_string.replace(b"\t",b"")
        rough_string = rough_string.replace(b"  ",b"")
        reparsed = minidom.parseString(rough_string)
        new_string = reparsed.toprettyxml(indent="\t")
        f=open('sensorconfig.xml','w')
        f.write(new_string)
        f.close()
        
        
    
    def _deltempsensorfromxml(self,handle):
        """Edits sensorconfig.xml to delete temperature sensor with specified params."""
        et = ET.parse('sensorconfig.xml')
        for sensor in et.findall('sensor'):
            for sub in sensor.findall('type'):
                if sub.text=='temperature':
                    for subel in sensor.findall('parameters'):
                        if subel.attrib['handle']==handle:
                            et.getroot().remove(sensor)


        rough_string = ET.tostring(et.getroot(), 'utf-8')
        rough_string = rough_string.replace(b"\n",b"")
        rough_string = rough_string.replace(b"\t",b"")
        rough_string = rough_string.replace(b"  ",b"")
        reparsed = minidom.parseString(rough_string)
        new_string = reparsed.toprettyxml(indent="\t")
        f=open('sensorconfig.xml','w')
        f.write(new_string)
        f.close()
        
        
    def _delnisensorfromxml(self,devstr):
        """Edits sensorconfig.xml to delete national instruments sensor with devstring devstr."""
        et = ET.parse('sensorconfig.xml')
        for sensor in et.findall('sensor'):
            for sub in sensor.findall('type'):
                if sub.text=='nianalog':
                    for subel in sensor.findall('parameters'):
                        if subel.attrib['devstr']==devstr:
                            et.getroot().remove(sensor)

        rough_string = ET.tostring(et.getroot(), 'utf-8')
        rough_string = rough_string.replace(b"\n",b"")
        rough_string = rough_string.replace(b"\t",b"")
        rough_string = rough_string.replace(b"  ",b"")
        reparsed = minidom.parseString(rough_string)
        new_string = reparsed.toprettyxml(indent="\t")
        f=open('sensorconfig.xml','w')
        f.write(new_string)
        f.close()
        
        
        
    def closeallcams(self):
        """Close all cams in self._connectedcamexp."""
        for cam in self._connectedcamexp.values():
            log.debug('Stopping the camera %s.' % cam.camstr())
            cam.stopcam()

    def closealltemp(self):
        """Close all temperature sensors in self._connectedtemp."""
        try:
            mydll = ctypes.windll.LoadLibrary(DLLPATH)
            for hand in self._connectedtemp:
                log.info("Closing temperature sensor with the handle %s" %hand)
                mydll.usb_tc08_close_unit(int(hand))
                log.info("Temperature sensor of handle %s has been closed." %hand)
        except:
            pass
        
