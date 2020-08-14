#################################################################################################
"""datalogger.py holds the main exporter tools for the sensors specified in sensorconfig.xml"""
#################################################################################################


import datalogger.analyser as analyser
import datalogger.cameras as cam
from datalogger.logsetup import log
from xml.dom import minidom
import xml.etree.ElementTree
import ctypes


#################################################################################################


class Exporter:
    """Abstract Exporter class, capable of exporting data to influx format"""
    def __init__(self,type,sensor):
        self.type=type
        self.sensor=sensor
        
        
    def getdata(self):
        #in subclasses this will give the wanted result in a library
        pass

    
    def exporttoinflux(self):
        dat=self.getdata()
        if dat is not None:
            
            tags={}
            tags["type"]=self.type
            tags["sensor"]=self.sensor
            library={"measurement": "log","tags": tags,"fields": dat}
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
    

  
    
class Beam(Exporter):
    """Class for beam sensors, which have their own ROI settings and fit output datas"""
    def __init__(self,cam,beam,roiparams):
            self._cam=cam
            tpe=self._cam.camstr() + " " + str(beam)
            super(Beam, self).__init__("camera",tpe)
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
    def __init__(self,dll,handle,tempid,tempsensors):
        if handle in tempsensors:
            super(Temperature, self).__init__("temperature",str(tempid))
            self._dll=dll
            self._handle=handle
        else:
            log.error('No temperature sensor with the handle %s is connected.' % (handle))
        

    
    def getdata(self):        
        """Exports data field in dictionary format"""        
        mydll = self._dll
        temp = np.zeros( (10,), dtype=np.float32)
        overflow_flags = np.zeros( (1,), dtype=np.int16)     
        mydll.usb_tc08_set_mains(self._handle,50)
        mydll.usb_tc08_set_channel(self._handle, 0, 0 )
        tc_type=ord('K')
        for i in range(1,9):
            mydll.usb_tc08_set_channel(self._handle,i,tc_type)
        mydll.usb_tc08_get_single(self._handle, temp.ctypes.data, overflow_flags.ctypes.data, 0) 
        mydll.usb_tc08_close_unit(self._handle)          
        lib={}
        for i in range(0,9):
            st='channel'+ str(i+1)
            lib[st]=temp[i]
        return lib
        
    
         
        
class Sensormanager:
    """This class reads the config file 'sensorconfig.xml' and initiates all sensors."""
    def __init__(self):
        
        self._camtypes=self._initiatecamlist()
        
        self._connectedcams=self._connectedcams()
        
        self._connectedtemp=self._initiatetemplist()
        
        self._paramlist=self._paramfromfile()
        
        self._tobeconfigured=self._getmissingsensors()
        
        if len(self._tobeconfigured)!=0:
            pass
        
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
                b.append((i,j))
        return b
        
    
    
    def _initiatetemplist(self):  
        """Uses DLL in order to find an connect to all temperature handles. Returns list for said handles."""
        try:
            mydll = ctypes.windll.LoadLibrary('usbtc08.dll')
        except:
            log.error('Failed to load DLL file usbtc08.dll')
            return None
        id=1
        templist=[];
        while id!=0:
            id=mydll.usb_tc08_open_unit() #Returns device handle, or 0 if no device was found, or -1 if an error occured
            if id!=-1:
                if id!=0:
                    templist.append(id)
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
                ret.append(Beam(self._connectedcamexp[(par['vendor'],par['camid'])],par['beam'],roipar))
            if par['type']=='temperature':
                ret.append(Temperature(ctypes.windll.LoadLibrary('usbtc08.dll'),par['handle'],par['tempid'],self._connectedtemp))  
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
        """Edits sensorconfig.xml to add a sensor with the specified params."""
        f=open('sensorconfig.xml','w')
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
        f.write(new_string)
        f.close()
