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
    def __init__(self,dev,trigger):
        super(NIAnalog, self).__init__("nianalog",dev,trigger)
        self._devstring = dev
        
        
    def getdata(self):
        """Export data field in dictionary format"""
        lib={}
        for i in range(0,6):
            channelstring = self._devstring + "/ai" + str(i)
            with nidaqmx.Task() as task:
                task.ai_channels.add_ai_voltage_chan(channelstring)
                output=task.read()
            lib["Channel" + str(i)]=output
        return lib
        
    
    
    
    
    
    
    
        
class Sensormanager:
    """This class reads the config file 'sensorconfig.xml' and initiates all sensors."""
    def __init__(self):
        
        self._camtypes=self._initiatecamlist()
        
        self._connectedcams=self._connectedcams()
        
        self._connectedtemp=self._initiatetemplist()
        
        self._connectedni=self._initiateni()
        
        self._paramlist=self._paramfromfile()
        
        self._tobeconfigured=self._getmissingsensors()
        
        self._overlyconfigured=self._getnonconnectedsensors()
        
        if len(self._overlyconfigured)!=0:
            for ov in self._overlyconfigured:
                if type(ov) is tuple:
                    log.info("The connected camera %s %s is mentioned in sensorconfig.xml and yet does not seem to be connected." % ov)
                    delnow=input("Delete camera %s %s from sensorconfig.xml? (y/n)" % ov)
                    if delnow=="y":
                        self._delcamerasensorfromxml(ov[0],ov[1])
                        log.info("Camera %s %s was deleted from sensorconfig.xml." % ov)
                if type(ov) is str:
                    log.info("The connected temperature sensor %s is mentioned in sensorconfig.xml and yet does not seem to be connected." % ov)
                    delnow=input("Delete temperature sensor with the handle %s from sensorconfig.xml? (y/n)" % ov)
                    if delnow=="y":
                        self._deltempsensorfromxml(ov)
                        log.info("Temperature sensor with the handle %s was deleted from sensorconfig.xml." % ov)

            
            
        
        if len(self._tobeconfigured)!=0:
            #Rewrite sensorxml file
            for miss in self._tobeconfigured:
                if type(miss) is tuple:
                    log.info("The connected camera %s %s is not yet configured in sensorconfig.xml." % miss)
                    configurenow=input("Configure %s %s now? (y/n) "% miss)
                    if configurenow=="y":
                        nobeams=input("How many beams are tracked with this camera? ")
                        try:
                            beamlist=range(int(nobeams))
                        except:
                            log.error("Bad input. Config process stopped.")
                            break
                        
                        for beam in beamlist:
                            beamname=input("What name should beam number %i be logged as? " % (beam+1))
                            self._addcamerasensortoxml(miss[0],miss[1],beamname,"(0,0,100,100)")

                if type(miss) is str:
                    log.info("The connected temperature sensor with the handle %s is not yet configured in sensorconfig.xml." % miss)
                    configurenow=input("Configure %s now? (y/n) " % miss)
                    if configurenow=="y":
                        tempid=input("What name should this sensor be logged as? ")
                        defaultlist=[]
                        for i in range(0,9):
                            st='Channel '+ str(i+1)
                            defaultlist.append(st)
                        self._addtempsensortoxml(tempid,miss,defaultlist)
                        
            
        #Reread edited xml file
        self._paramlist=self._paramfromfile()
        self._tobeconfigured=[]
        self._overlyconfigured=[]
                    
            
                        
        
        self._connectedcamexp=self._initiatecamexpdict()
        
        self._sensorlist=self._initiatesensorlist()
        
        
    
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
                    log.info("Temperature sensor of handle %i encountered.")
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

            paramlist.append(r)
        return paramlist
    
    
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
                ret.append(Beam(self._connectedcamexp[(par['vendor'],par['camid'])],par['beam'],roipar,trig.NationalTrigger("Dev1/ai1",3.0)))
            if par['type']=='temperature':
                channellist=[]
                for i in range(0,9):
                    keystr='channel' + str(i+1)
                    channellist.append(par[keystr])    
                ret.append(Temperature(ctypes.windll.LoadLibrary(DLLPATH),par['handle'],par['tempid'],self._connectedtemp,trig.PeriodicTrigger(8.0),channellist))
            
            if par['type']=='nianalog':
                if par["devstr"] in self._connectedni:
                    ret.append(NIAnalog(par["devstr"],trig.PeriodicTrigger(8.0)))
                else:
                    log.error("The NI device with the devkey %s does not seem to be connected." % par["devstr"])
                
        
        return ret
    
        

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
    
    
    def getperiodiclist(self):
        l=[]
        for sensor in self._sensorlist:
            if sensor.trigger.typ=="periodic":
                l.append(sensor)
        return l
    
    
    def _getnonconnectedsensors(self):
        """Get all sensors, which are specified in sensorconfig.xml, yet not connected."""
        current=[]
        over=[]
        for par in self._paramlist:
            if par["type"]=="camera":
                tup = (par["vendor"],par["camid"])
                current.append(tup)
            if par["type"]=="temperature":
                current.append(par["handle"])
                
        currentset=set(current)
        if not self._connectedcams is None:
            camintersection=currentset.intersection(self._connectedcams)
            for cam in list(camintersection):
                currentset.remove(cam)

        if not self._connectedtemp is None:
            tempintersection=currentset.intersection(self._connectedtemp)
            for temp in list(tempintersection):
                currentset.remove(temp)

        return list(currentset)
        
    
    def _getmissingsensors(self):
        """Get all connected sensors, which are not specified in sensorconfig.xml"""
        current=[]
        missing=[]
        for par in self._paramlist:
            if par["type"]=="camera":
                tup = (par["vendor"],par["camid"])
                current.append(tup)
            if par["type"]=="temperature":
                current.append(par["handle"])
        for cam in self._connectedcams:
            if not cam in current:
                missing.append(cam)
        if not self._connectedtemp is None:
            for temp in self._connectedtemp:
                if not temp in current:
                    missing.append(temp)
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
        
