#######################################################################################################
"""camera.py holds the abstract camera interface and the concrete vendorspecific implementations."""
#######################################################################################################


import threading
import sys

import numpy as np
from ctypes import byref, c_float, c_int, c_uint32, c_int32, c_double, pointer
from time import sleep
from queue import Queue
from functools import partial
import scipy.ndimage.interpolation as rot


try:
    from ximea import xiapi, xidefs
except:
    pass

try:
    import datalogger.driver.vrmagic.vrmusbcamapi as vrm
except:
    pass

try:
    import datalogger.driver.pymba.pymba as pymba
except:
    pass

try:
    import datalogger.driver.ueye.ueyeapi as ueye
except:
    pass

from datalogger.logsetup import log



#######################################################################################################



class CameraManager(object):
    def __init__(self, cameras):
        """The class that manages all connected cameras.

        Parameters
        ----------
        cameras : list of `Camera` instances
            The cameras to look for. Use one per vendor.

        """
        super(CameraManager, self).__init__()
        self._cameras = cameras
        self._activecam = None
        self.isaquiring = False
        self._findconnectedcams()

    def _findconnectedcams(self):
        """Find all connected cameras and store them in _camdict"""
        self._camdict = {}
        for cam in self._cameras:
            try:
                self._camdict[cam.VENDOR] = cam.findallcams()
                log.debug('Found the following %s cameras: %s' % (cam.VENDOR, self._camdict[cam.VENDOR]))
            except NameError:
                log.warning('Could not look for cameras from %s. Is the driver installed?' % cam.VENDOR)

    @property
    def connectedcams(self):
        """Return all connected cams"""
        return self._camdict
    

    def setactivecam(self, vendor, camid):
        """Activate (open) a camera.

        Parameters
        ----------
        vendor : string
            The manufacturer of the camera.
        camid : string
            The unique camera id that can be used to get a handle.

        """
        for cam in self._cameras:
            if cam.VENDOR == vendor:
                if self._activecam:
                    #log.debug('Closing camera %s, %s' % (vendor, self._activecam.camid))
                    self._activecam.close()
                #log.debug('Opening camera %s, %s' % (vendor, camid))
                cam.open(camid)
                #log.debug('Setting active camera to %s, %s' % (vendor, camid))
                self._activecam = cam

    def caminfo(self):
        """Get information on the active camera."""
        if self._activecam:
            return (self._activecam.VENDOR, self._activecam.camid)
        else:
            log.error('No camera selected.')
            return None

    def getimage(self):
        """Return the last image from the active camera."""
        if self._activecam:
            return self._activecam.getimage()
        else:
            log.error('No camera selected.')
            return None

    def close(self):
        """Close the active camera."""
        if self._activecam:
            #log.debug('Closing cam')
            self._activecam.close()
            self._activecam = None
        else:
            log.error('No camera selected.')
            return None

    def start(self):
        """Start the active camera in continous acqisition mode."""
        if self._activecam:
            self._activecam.startcontacq()
            self.isaquiring = True
        else:
            self.isaquiring = False
            log.error('No camera selected.')
            return None

    def stop(self):
        """Stop the active camera."""
        if self._activecam:
            #log.debug('Stopping camera')
            self._activecam.stopcontacq()
            self.isaquiring = False
            #log.debug('Camera stopped')
        else:
            self.isaquiring = False
            log.error('No camera selected.')
            return None

    @property
    def exposure(self):
        """Set and get the active camera exposure in ms."""
        if self._activecam:
            return self._activecam.exposure
        else:
            log.error('No camera selected.')
            return None

    @exposure.setter
    def exposure(self, val):
        if self._activecam:
            if self.isaquiring:
                self._activecam.stopcontacq()
                self._activecam.exposure = val
                self._activecam.startcontacq()
            else:
                self._activecam.exposure = val
        else:
            log.error('No camera selected.')

    @property
    def exposurebounds(self):
        """Get the active camera exposure bounds in ms."""
        if self._activecam:
            return self._activecam.exposurebounds
        else:
            log.error('No camera selected.')
            return None

    @property
    def pixelsize(self):
        """Return the pixelsize in micrometer of the camera. Non square pixels are not supported."""
        if self._activecam:
            return self._activecam.pixelsize
        else:
            log.error('No camera selected.')
            return None

    @property
    def gain(self):
        """Set and get the camera gain of the active camera."""
        if self._activecam:
            return self._activecam.gain
        else:
            log.error('No camera selected.')
            return None

    @gain.setter
    def gain(self, val):
        if self._activecam:
            if self.isaquiring:
                self._activecam.stopcontacq()
                self._activecam.gain = val
                self._activecam.startcontacq()
            else:
                self._activecam.gain = val
        else:
            log.error('No camera selected.')

    @property
    def gainvals(self):
        """Get the possible camera gain values of the active camera."""
        if self._activecam:
            return self._activecam.gainvals
        else:
            log.error('No camera selected.')
            return None

    @property
    def maxval(self):
        """Get the maximum counts per pixel allowed for the active camera."""
        if self._activecam:
            return self._activecam.maxval
        else:
            log.error('No camera selected.')
            return None

    @property
    def queuedimages(self):
        """Return the number of queued images."""
        if self._activecam:
            return self._activecam.queuedimages()
        else:
            log.error('No camera selected.')
            return None

    @property
    def hasimages(self):
        """True if activecam has new images available"""
        if self._activecam:
            return self._activecam.hasimages()
        else:
            log.error('No camera selected.')
            return None


    def emptyqueue(self):
        """Empty the _imagequeue."""
        if self._activecam:
            self._activecam.emptyqueue()
        else:
            log.error('No camera selected.')


class Camera(object):
    VENDOR = None  # the vendor name

    def __init__(self):
        """The abstract camera class that defines the interface"""
        super(Camera, self).__init__()
        self._handle = None  # the camera handle
        self._imagequeue = Queue()  # the image fifo queue
        self._imagequeue.maxsize = 2
        self._camid = None  # the unique id of the camera

    @property
    def camid(self):
        """Return the id of the camera.

        This ID is the same that has been used to open the camera.

        """
        return self._camid

    @property
    def exposure(self):
        """Set and get the camera exposure in ms."""
        raise NotImplementedError

    @exposure.setter
    def exposure(self, val):
        raise NotImplementedError

    @property
    def exposurebounds(self):
        """Get the camera exposure bounds in ms.

        The method should return a tuple (min, max).

        """
        raise NotImplementedError

    @property
    def pixelsize(self):
        """Return the pixelsize in micrometer of the camera. Non square pixels are not supported."""
        raise NotImplementedError

    @property
    def gain(self):
        """Set and get the camera gain."""
        raise NotImplementedError

    @gain.setter
    def gain(self, val):
        raise NotImplementedError

    @property
    def gainvals(self):
        """Get the possible camera gain values.

        The method should return a tuple (g1, g2, ...).

        """
        raise NotImplementedError

    @property
    def maxval(self):
        """Get the maximum counts per pixel allowed for the active camera.

        This value is used to detect saturation in the image.
        """
        raise NotImplementedError

    def open(self, camid):
        """Open the camera and obtain a camera handle"""
        self._camid = camid
        raise NotImplementedError

    def close(self):
        """Close the camera"""
        self.emptyqueue()
        self._camid = None
        raise NotImplementedError

    def startcontacq(self):
        """Start continuous picture acquisition.

        Put acquired images on in the image queue.

        """
        raise NotImplementedError

    def stopcontacq(self):
        """Stop  continuous picture acquisition"""
        raise NotImplementedError

    def getimage(self):
        """Return a captured image from the queue"""
        if not self._imagequeue.empty():
            nextim = self._imagequeue.get()
            self._imagequeue.task_done()
            return nextim
        else:
            return None

    def queuedimages(self):
        """Return the size of the _imagequeue."""
        return self._imagequeue.qsize()

    def hasimages(self):
        """True if new images are available"""
        if self._imagequeue.empty():
            return False
        else:
            return True

    def emptyqueue(self):
        """Empty the cameras _imagequeue."""
        while not self._imagequeue.empty():
            self._imagequeue.get()
            self._imagequeue.task_done()
        self._imagequeue.join()

    def findallcams(self):
        """Find all cameras of this vendor

        Returns
        -------
        cams : dictionary
            Dictionary of all connected cameras where the key is the unique id
            that can be used to obtain a camera handle. The value is a
            description of the camera presented to the user.

        """
        raise NotImplementedError


class VRMThread(threading.Thread):

    def __init__(self, queue, handle, parent):
        """Thread that gets images from the vrm camera

        """
        super(VRMThread, self).__init__()
        self.isrunning = True
        self._queue = queue
        self._handle = handle
        self._parent = parent
        self.setDaemon(True)  # important to let the Thread exit at application close.
        #log.debug('VRM thread started')

    def run(self):
        while self.isrunning:
            framesdropped = vrm.VRmBOOL()
            image = vrm.POINTER(vrm.VRmImage)()
            r = self._parent._ce(vrm.VRmUsbCamLockNextImage(self._handle, byref(image), byref(framesdropped)))
            if r == 1:
                height = image.contents.m_image_format.m_height
                pitch = image.contents.m_pitch
                img = np.array(image.contents.mp_buffer[0:height * pitch]).reshape(height, pitch).T
                try:
                    self._queue.put(img, timeout=1)
                except:
                    pass
            self._parent._ce(vrm.VRmUsbCamUnlockNextImage(self._handle, byref(image)))
            sleep(0.1)



class VrmCamera(Camera):
    VENDOR = 'vrm'

    def __init__(self):
        """Camera class for a VR Magic camera."""
        super(VrmCamera, self).__init__()
        self._devkey = None
        self._imagecapturethread = None

    def _ce(self, val):
        """Check for errors"""
        if val == 0:
            err = vrm.VRmUsbCamGetLastError()
            log.error('VRM ERROR: %s' % err.data.decode('utf-8'))
        return val

    def findallcams(self):
        """Find all cameras of this vendor

        Returns
        -------
        cams : dictionary
            Dictionary of all connected cameras where the key is the unique id
            that can be used to obtain a camera handle. The value is a
            description of the camera presented to the user.

        """
        self._ce(vrm.VRmUsbCamUpdateDeviceKeyList())
        ndev = vrm.VRmDWORD()
        self._ce(vrm.VRmUsbCamGetDeviceKeyListSize(byref(ndev)))
        ndev = int(ndev.value)
        log.info('Found %i VRM cameras' % ndev)
        cams = {}
        # get a device key for each camera and then the info on the camera
        for nn in range(ndev):
            devkey = vrm.POINTER(vrm.VRmDeviceKey)()
            self._ce(vrm.VRmUsbCamGetDeviceKeyListEntry(nn, byref(devkey)))
            serial = devkey.contents.m_serial
            manufacturer = devkey.contents.mp_manufacturer_str.data.decode('utf-8')
            product = devkey.contents.mp_product_str.data.decode('utf-8')
            cams[serial] = '%s_%s_%s' % (manufacturer, product, serial)
            log.debug('Added camera %s_%s_%s' % (manufacturer, product, serial))
        return cams

    @property
    def exposure(self):
        """Set and get the camera exposure in ms."""
        prop = c_float()
        self._ce(vrm.VRmUsbCamGetPropertyValueF(self._handle, vrm.VRmPropId(4097), byref(prop)))
        return float(prop.value)

    @exposure.setter
    def exposure(self, val):
        self._ce(vrm.VRmUsbCamSetPropertyValueF(self._handle, vrm.VRmPropId(4097), byref(c_float(val))))

    @property
    def exposurebounds(self):
        """Get the camera exposure bounds in ms.

        The method should return a tuple (min, max).

        """
        prop_attr = vrm.VRmPropAttribsF()
        self._ce(vrm.VRmUsbCamGetPropertyAttribsF(self._handle, vrm.VRmPropId(4097), byref(prop_attr)))
        return (prop_attr.m_min, prop_attr.m_max)

    @property
    def pixelsize(self):
        """Return the pixelsize in micrometer of the camera. Non square pixels are not supported."""
        if self._devkey.contents.mp_product_str.data.decode('utf-8') == 'VRmC-12/BW':
            res = 6.0
        elif self._devkey.contents.mp_product_str.data.decode('utf-8') == 'VRmmC-12/BW':
            res = 6.0
        elif self._devkey.contents.mp_product_str.data.decode('utf-8') == 'VRmC-9+/BW':
            res = 5.2
        else:
            log.error('Unknown pixel size for %s. Using 1mum.' % self._devkey.contents.mp_product_str.data.decode('utf-8'))
            res =  1.0
        #log.info('Using pixel size %f.' % res)
        return res

    @property
    def gain(self):
        """Set and get the camera gain."""
        prop = c_int()
        self._ce(vrm.VRmUsbCamGetPropertyValueI(self._handle, vrm.VRmPropId(4131), byref(prop)))
        return float(prop.value)

    @gain.setter
    def gain(self, val):
        self._ce(vrm.VRmUsbCamSetPropertyValueI(self._handle, vrm.VRmPropId(4131), byref(c_int(int(val)))))

    @property
    def gainvals(self):
        """Get the possible camera gain values.

        The method should return a tuple (g1, g2, ...).

        """
        prop_attr = vrm.VRmPropAttribsI()
        self._ce(vrm.VRmUsbCamGetPropertyAttribsI(self._handle, vrm.VRmPropId(4131), byref(prop_attr)))
        return tuple(np.arange(prop_attr.m_min, prop_attr.m_max + 1, prop_attr.m_step))

    @property
    def maxval(self):
        """Get the maximum counts per pixel allowed for the active camera.

        This value is used to detect saturation in the image.
        """
        return 255

    def _getdevkey(self, serial):
        """Return the devkey given a serial."""
        self._ce(vrm.VRmUsbCamUpdateDeviceKeyList())
        ndev = vrm.VRmDWORD()
        self._ce(vrm.VRmUsbCamGetDeviceKeyListSize(byref(ndev)))
        ndev = int(ndev.value)
        #print(ndev)
        for nn in range(ndev):
            devkey = vrm.POINTER(vrm.VRmDeviceKey)()
            self._ce(vrm.VRmUsbCamGetDeviceKeyListEntry(nn, byref(devkey)))
            if int(serial) == int(devkey.contents.m_serial):
                return devkey
        return None

    def open(self, camid):
        """Open the camera and obtain a camera handle"""
        self._camid = camid
        #log.debug('Try opening cam with camid: %s' % camid)
        # get the devkey
        self._devkey = self._getdevkey(camid)
        if not self._devkey.contents.m_busy == 1:
            self._handle = vrm.VRmUsbCamDevice()
            self._ce(vrm.VRmUsbCamOpenDevice(self._devkey, byref(self._handle)))
            #log.debug('Success in opening cam with camid: %s' % camid)
        else:
            log.error('Could not open camera with camid: %s: BUSY' % camid)

    def _setupcam(self):
        """Prepare the camera, set defaults."""
        # set the format
        nsrcfmt = vrm.VRmDWORD()
        self._ce(vrm.VRmUsbCamGetSourceFormatListSize(self._handle, byref(nsrcfmt)))
        imagefmt = vrm.VRmImageFormat()
        self._ce(vrm.VRmUsbCamGetSourceFormatListEntry(self._handle, nsrcfmt.value - 1, byref(imagefmt)))
        self._ce(vrm.VRmUsbCamSetSourceFormatIndex(self._handle, nsrcfmt.value - 1))

    def close(self):
        """Close the camera"""
        self._ce(vrm.VRmUsbCamCloseDevice(self._handle))
        self._camid = None
        self._handle = None

    def startcontacq(self):
        """Start continuous picture acquisition.

        Put acquired images on in the image queue.

        """
        #log.debug('Trying to start camera %s' % self._camid)
        self._ce(vrm.VRmUsbCamStart(self._handle))
        if self._imagecapturethread is None or not self._imagecapturethread.is_alive():
            self._imagecapturethread = VRMThread(self._imagequeue, self._handle, self)
            self._imagecapturethread.start()
        #log.info('Started camera %s' % self._camid)

    def stopcontacq(self):
        """Stop  continuous picture acquisition"""
        if self._imagecapturethread is not None:
            self._imagecapturethread.isrunning = False
            self._imagecapturethread.join()
            self._imagecapturethread = None
        self._ce(vrm.VRmUsbCamStop(self._handle))
        #log.info('Stopped camera %s' % self._camid)

    def __del__(self):
        if self._devkey is not None:
            self._ce(vrm.VRmUsbCamFreeDeviceKey(byref(self._devkey)))

class XiapiDataWatcher(threading.Thread):
    """A thread to watch for captured data.

    Many camera drivers have a callback functionality implemented, xiapi not.
    Hence here a manual implementation.
    """

    def __init__(
        self,
        name,
        parent,
        check_data_method,
        data_queue,
        daemon=True,
        stop_event_interval=0.1,
    ):
        super().__init__(name=name)
        self._parent = parent
        self.daemon = daemon
        self._check_data_method = check_data_method
        self._data_queue = data_queue
        self._stop_event = threading.Event()
        self._stop_event_interval = stop_event_interval

    def run(self):
        while not self._stop_event.is_set():
            # We expect data to be None if nothing has been aquired. Note that
            # check_data_method should not block for long (stop_event_interval max)
            data = self._check_data_method()
            if data is not None:
                self._data_queue.put(data.T, timeout=1)
            self._stop_event.wait(self._stop_event_interval)

    def stop(self):
        self._stop_event.set()


class XiapiCamera(Camera):
    VENDOR = 'ximea'

    def __init__(self):
        super(XiapiCamera, self).__init__()
        self._cam = xiapi.Camera()
        self._devinfo = None
        self._camid = None  # the serial if a camera is open, else none
        self._imagecapturethread = None

    def findallcams(self):
        """Find all cameras of this vendor

        Returns
        -------
        cams : dictionary
            Dictionary of all connected cameras where the key is the unique id
            that can be used to obtain a camera handle. The value is a
            description of the camera presented to the user.

        """
        res = {}
        cams = [xiapi.Camera(0)]
        ndev = cams[0].get_number_devices()
        log.info('Found %i ximea cameras' % ndev)
        if ndev == 0:
            log.error('No cameras found')
        for ii in range(ndev - 1):
            cams.append(xiapi.Camera(ii + 1))
        for ii in range(ndev):
            serial = cams[ii].get_device_info_string("device_sn").decode("utf8")
            res[serial] = {
                    "serial": serial,
                    "type": cams[ii].get_device_info_string("device_type").decode(
                        "utf8"
                    ),
                    "name": cams[ii].get_device_info_string("device_name").decode(
                        "utf8"
                    ),
                    }
        return res

    @property
    def exposure(self):
        """Set and get the camera exposure in ms."""
        return self._cam.get_exposure() / 1000

    @exposure.setter
    def exposure(self, val):
        self._cam.set_exposure(int(val * 1000))

    @property
    def exposurebounds(self):
        """Get the camera exposure bounds in ms.

        The method should return a tuple (min, max).

        """
        maxi = self._cam.get_exposure_maximum()
        mini = self._cam.get_exposure_minimum()
        return (mini/1000, maxi/1000)

    @property
    def pixelsize(self):
        """Return the pixelsize in micrometer of the camera. Non square pixels are not supported."""
        if self._devinfo['name'] == 'MD028MU-SY':
            res = 4.54
        else:
            log.error('Unknown pixel size for {}. Using 5mum.'.format(self._devinfo['name']))
            res =  5.0
        #log.info('Using pixel size %f.' % res)
        return res

    @property
    def gain(self):
        """Set and get the camera gain."""
        return self._cam.get_gain()

    @gain.setter
    def gain(self, val):
        self._cam.set_gain(val)

    @property
    def gainvals(self):
        """Get the possible camera gain values.

        The method should return a tuple (g1, g2, ...).

        """
        maxi = self._cam.get_gain_maximum()
        mini = self._cam.get_gain_minimum()
        step = self._cam.get_gain_increment()
        return tuple(np.arange(mini, maxi+step, step))

    @property
    def maxval(self):
        """Get the maximum counts per pixel allowed for the active camera.

        This value is used to detect saturation in the image.
        """
        return 2**12 - 1

    def _getdevinfo(self):
        res = {
              "serial": self._cam.get_device_info_string("device_sn").decode(
                  "utf8"
              ),
              "type": self._cam.get_device_info_string("device_type").decode(
                  "utf8"
              ),
              "name": self._cam.get_device_info_string("device_name").decode(
                  "utf8"
              ),
              }
        return res

    def open(self, camid):
        """Open the camera and obtain a camera handle"""
        #log.debug('Try opening cam with camid: %s' % camid)
        try:
            self._cam.open_device_by_SN(camid)
            self._camid = camid
            self._devinfo = self._getdevinfo()
            #log.debug('Success in opening cam with camid: %s' % camid)
            self._setupcam()
        except xiapi.Xi_error as e:
            self._camid = None
            log.error("XIMEA ERROR in open_device: {}".format(e))

    def _setupcam(self):
        """Prepare the camera, set defaults."""
        self._cam.set_downsampling("XI_DWN_2x2")
        # self._cam.set_downsampling("XI_DWN_1x1")
        self._cam.set_imgdataformat("XI_MONO16")
        self._cam.disable_aeag()
        self._cam.disable_LUTEnable()
        self._cam.set_trigger_source('XI_TRG_OFF')
        # self._cam.set_trigger_delay(0)
        # self._cam.set_trigger_selector("XI_TRG_SEL_FRAME_START")
        ## set gpi port 1 to trigger (if used)
        # self._cam.set_gpi_selector("XI_GPI_PORT1")
        # self._cam.set_gpi_mode("XI_GPI_TRIGGER")
        self._cam.set_debug_level("XI_DL_DISABLED")
        # self._cam.set_buffers_queue_size(4)

    def close(self):
        """Close the camera"""
        if self._camid is not None:
            self._cam.close_device()
            self._camid = None

    def get_image(self):
        img = xiapi.Image()
        try:
            self._cam.get_image(img, 40)
            return img.get_image_data_numpy()

        except xiapi.Xi_error as e:
            #  10 = timeout, 45 = status
            if (not e.status == 10) and (not e.status == 45):
                print("XIMEA ERROR in get_image: {}".format(e))
            return None

    def startcontacq(self):
        """Start continuous picture acquisition.

        Put acquired images on in the image queue.

        """
        #log.debug('Trying to start camera %s' % self._camid)
        self._cam.start_acquisition()
        if self._imagecapturethread is not None:
            log.error("XIMEA ERROR in start_capture: Capture running")
        else:
            log.info("XIMEA: Start capture.")
            self._imagecapturethread = XiapiDataWatcher(
                "Xiapi_watcher_{}".format(self._camid),
                self,
                self.get_image,
                self._imagequeue,
                daemon=True,
                stop_event_interval=0.05,
            )
            self._imagecapturethread.start()

    def stopcontacq(self):
        """Stop  continuous picture acquisition"""
        self._cam.stop_acquisition()
        if self._imagecapturethread is not None and self._imagecapturethread.is_alive():
            self._imagecapturethread.stop()
            self._imagecapturethread.join()
            self._imagecapturethread = None
        #log.info('Stopped camera %s' % self._camid)

    def __del__(self):
        self.close()


class UEyeThread(threading.Thread):

    def __init__(self, queue, handle, parent):
        """Thread that gets images from the ueye camera

        """
        super(UEyeThread, self).__init__()
        self.isrunning = True
        self._timeout = 25 # in 10x ms
        self._queue = queue
        self._handle = handle
        self._parent = parent
        self.setDaemon(True)  # important to let the Thread exit at application close.
        log.debug('UEye thread started')

    def run(self):
        while self.isrunning:
            err0 = self._parent.ueyeapi.dll.is_FreezeVideo(c_uint32(self._handle), c_int32(self._timeout))
            self._parent._ce(err0)
            if err0 == 0:
                image = self._parent.ueyeapi.is_GetRescaledArray()
                try:
                    self._queue.put(image, timeout=1)
                except:
                    pass
            sleep(0.1)


class UEyeCamera(Camera):
    VENDOR = 'ueye'

    def __init__(self):
        """Camera class for a IDS UEye camera."""
        super(UEyeCamera, self).__init__()

        self.ueyeapi = ueye.UEyeAPI()

        self._devid = 1
        self._imagecapturethread = None

    def _ce(self, val):
        """Check for errors"""
        if val != 0:
            err = ueye.EC[val]
            log.error('UEYE ERROR: %s' % err)
        # return val

    def findallcams(self):
        """Find all cameras of this vendor

        Returns
        -------
        cams : dictionary
            Dictionary of all connected cameras where the key is the unique id
            that can be used to obtain a camera handle. The value is a
            description of the camera presented to the user.

        """
        err0, ndev = self.ueyeapi.is_GetNumberOfCameras()
        self._ce(err0)
        # ndev = int(ndev)

        cams = {}
        # get a device key for each camera and then the info on the camera
        err1, caminfo = self.ueyeapi.is_GetCameraList(camnum=ndev)
        self._ce(err1)

        camnum = int(getattr(caminfo, 'dwCount'))
        log.info('Found %i UEye cameras' % int(camnum))

        caminfolist = getattr(caminfo, 'uci[1]')

        for i in range(camnum):

            serial = getattr(caminfolist[i], 'SerNo[16]')
            manufacturer = 'IDS UEye'
            product = getattr(caminfolist[i], 'Model[16]')
            cams[serial] = '%s_%s_%s' % (manufacturer, product, serial)
            log.debug('Added camera %s_%s_%s' % (manufacturer, product, serial))
        return cams

        # err0, caminfo = ueye.is_InitCamera()
        # self._ce(int(err0))

    @property
    def exposure(self):
        """Set and get the camera exposure in ms."""
        param = c_double()
        pparam =  pointer(param)
        nsizeofparam = 8
        err0 = self.ueyeapi.dll.is_Exposure(c_uint32(self._handle), c_uint32(7), pparam, c_uint32(nsizeofparam))
        self._ce(err0)
        expotime = pparam.contents.value
        return float(expotime)

    @exposure.setter
    def exposure(self, val):
        param = c_double(val)
        pparam = pointer(param)
        nsizeofparam = 8
        err0 = self.ueyeapi.dll.is_Exposure(c_uint32(self._handle), c_uint32(12), pparam, c_uint32(nsizeofparam))
        self._ce(err0)

    @property
    def exposurebounds(self):
        """Get the camera exposure bounds in ms.

        The method should return a tuple (min, max).

        """
        minparam = c_double()
        minpparam = pointer(minparam)
        minparamsize = 8
        err0 = self.ueyeapi.dll.is_Exposure(c_uint32(self._handle), c_uint32(3), minpparam, c_uint32(minparamsize))
        self._ce(err0)
        minval = minpparam.contents.value

        maxparam = c_double()
        maxpparam = pointer(maxparam)
        maxparamsize = 8
        err1 = self.ueyeapi.dll.is_Exposure(c_uint32(self._handle), c_uint32(4), maxpparam, c_uint32(maxparamsize))
        self._ce(err1)
        maxval = maxpparam.contents.value

        return (float(minval), float(maxval))

    @property
    def pixelsize(self):
        """Return the pixelsize in micrometer of the camera. Non square pixels are not supported."""
        pixelsize = 1.0
        err0, structsensor = self.ueyeapi.is_GetSensorInfo()
        self._ce(err0)
        pixelsize = getattr(structsensor, 'wPixelSize')/100.
        #log.info('Using pixel size %f.' % (pixelsize))
        return pixelsize

    @property
    def gain(self):
        """Set and get the camera gain."""
        gainval = self.ueyeapi.dll.is_SetHardwareGain(c_uint32(self._handle), c_int32(0x8000), c_int32(-1), c_int32(-1), c_int32(-1))
        return float(gainval)

    @gain.setter
    def gain(self, val):
        val = int(val)
        err0 = self.ueyeapi.dll.is_SetHardwareGain(c_uint32(self._handle), c_int32(val), c_int32(-1), c_int32(-1), c_int32(-1))
        self._ce(err0)

    @property
    def gainvals(self):
        """Get the possible camera gain values.

        The method should return a tuple (g1, g2, ...).

        Min is 0.0, max is 100.0, stepsize is 1.0 according to manual

        """
        return tuple(np.arange(0.0, 100.0 + 1.0, 1.0))

    @property
    def maxval(self):
        """Get the maximum counts per pixel allowed for the active camera.

        This value is used to detect saturation in the image.
        """
        return 2**16 - 1

    def _getdevid(self, serial):
        """Return the device ID given a serial."""
        err0, ndev = self.ueyeapi.is_GetNumberOfCameras()
        self._ce(err0)

        err1, caminfo = self.ueyeapi.is_GetCameraList(camnum=ndev)
        self._ce(err1)

        camnum = int(getattr(caminfo, 'dwCount'))
        caminfolist = getattr(caminfo, 'uci[1]')
        devid = 1
        available = 0
        for i in range(camnum):
            serialnew = getattr(caminfolist[i], 'SerNo[16]')
            if str(serial) == str(serialnew):
                devid = int(getattr(caminfolist[i], 'dwDeviceID'))
                available = getattr(caminfolist[i], 'dwInUse')
        return devid, available

    def open(self, camserial):
        """Open the camera and obtain a camera handle"""
        self._camserial = camserial
        #log.debug('Try opening cam with serial: %s' % camserial)
        # get the devkey
        self._devid, available = self._getdevid(camserial)
        if not int(available) == 1:
            err0, self._handle = self.ueyeapi.is_CreateHandle(self._devid)
            self._ce(err0)
            #log.debug('Success in opening cam with camid: %s' % camserial)

        else:
            log.error('Could not open camera with camid: %s: BUSY' % camserial)

    def _setupcam(self):
        """Prepare the camera, set defaults.
        NOT YET IMPLEMENTED FOR UEYE
        """
        # set the format
        pass
    def close(self):
        """Close the camera"""
        err0 = self.ueyeapi.dll.is_ExitCamera(c_uint32(self._handle))
        self._ce(err0)
        #log.info('Stopped camera %s' % self._devid)
        self._devid = None
        self._handle = None


    def startcontacq(self):
        """Start continuous picture acquisition.
        We only take single shots quickly after another.
        Put acquired images on in the image queue.

        """
        #log.debug('Trying to start camera %s' % self._devid)
        self.ueyeapi.is_InitialiseMemory()
        if self._imagecapturethread is None or not self._imagecapturethread.is_alive():
            self._imagecapturethread = UEyeThread(self._imagequeue, self._handle, self)
            self._imagecapturethread.start()
        #log.info('Started camera %s' % self._devid)

    def stopcontacq(self):
        """
        Stop  continuous picture acquisition
        Only single shots - no stop method needed
        """
        if self._imagecapturethread is not None:
            self._imagecapturethread.isrunning = False
            self._imagecapturethread.join()
            self._imagecapturethread = None

        #log.info('Stopped camera %s' % self._devid)

    def __del__(self):
        if self._handle is not None:
            err0 = self.ueyeapi.dll.is_ExitCamera(c_uint32(self._handle))
            self._ce(err0)
            self._devid = None
            self._handle = None


class ImSimThread(threading.Thread):
    IMAGEFMT = (500, 500)

    def __init__(self, queue, gain, exposure, rate=0.5):
        """Thread that generates images every rate sec.

        """
        super(ImSimThread, self).__init__()
        self.isrunning = True
        self._rate = rate
        self._queue = queue
        self._gain = gain
        self._exposure = exposure
        self.setDaemon(True)  # important to let the Thread exit at application close.

    def run(self):
        peakcnt = 10. * self._gain * self._exposure
        noiseamp = 1. * self._gain
        xx, yy = np.meshgrid(np.arange(0, self.IMAGEFMT[0], 1), np.arange(0, self.IMAGEFMT[1], 1))
        while self.isrunning:
            noise = np.random.poisson(noiseamp, size=self.IMAGEFMT)
            
            ##1st beam
            
            ang1 = --40 + 80. * np.random.rand()
            sigx1 = 3. + 10. * np.random.rand()
            sigy1 = 2 + 5. * np.random.rand()
            centx1 = self.IMAGEFMT[0] / 2 + np.random.rand()*self.IMAGEFMT[0] / 15
            centy1 = self.IMAGEFMT[1] / 4 + np.random.rand()*self.IMAGEFMT[1] / 15
            #centx1 = self.IMAGEFMT[0] / 2
            #centy1 = self.IMAGEFMT[1] / 2
            img1=np.exp(-(xx - centx1)**2 / 2 / sigx1**2 - (yy - centy1)**2 / 2 / sigy1**2)
            img1=rot.rotate(img1,angle=ang1, reshape=False,prefilter=False)

            ##2nd beam
            
            ang2 = -20. + 40. * np.random.rand()
            sigx2 = 20. + 20. * np.random.rand()
            sigy2 = 6. + 5. * np.random.rand()
            centx2 = self.IMAGEFMT[0] / 2 + np.random.rand()*self.IMAGEFMT[0] / 15
            centy2 = self.IMAGEFMT[1]* 3 / 4 + np.random.rand()*self.IMAGEFMT[1] / 15
            # centx2 = self.IMAGEFMT[0] / 2
            # centy2 = self.IMAGEFMT[1] / 2
            img2=np.exp(-(xx - centx2)**2 / 2 / sigx2**2 - (yy - centy2)**2 / 2 / sigy2**2)
            img2=rot.rotate(img2,angle=ang2, reshape=False,prefilter=False)
            
            img = peakcnt * (img1+img2) + noise.T
            self._queue.put(img)
            sleep(self._rate)


class VimbaCamera(Camera):
    VENDOR = 'AVT'

    def __init__(self):
        super(VimbaCamera, self).__init__()
        self._vimba = pymba.Vimba()
        self._vimba.startup()
        self._system = self._vimba.getSystem()
        self._acquiring = False

    def __del__(self):
        self.close()
        if hasattr(self, '_vimba') and self._vimba is not None:
            self._vimba.shutdown()

    def findallcams(self):
        self._system.runFeatureCommand('GeVDiscoveryAllOnce')
        sleep(0.2)
        cams = self._vimba.getCameraIds()
        out = {}
        for cam in cams:
            c = self._vimba.getCamera(cam)
            info = c.getInfo()
            out[cam] = '{name} ({interface})'.format(
                    name=info.modelName.decode(),
                    interface=info.interfaceIdString.decode())
        log.debug(out)
        return out

    @property
    def exposure(self):
        """Set and get the camera exposure in ms."""
        return self._handle.ExposureTimeAbs / 1000

    @exposure.setter
    def exposure(self, val):
        self._handle.ExposureTimeAbs = float(val) * 1000

    @property
    def exposurebounds(self):
        """Get the camera exposure bounds in ms.

        The method should return a tuple (min, max).

        """
        return tuple(map(lambda x: x / 1000,
                         self._handle.getFeatureRange('ExposureTimeAbs')))

    @property
    def pixelsize(self):
        """Return the pixelsize in micrometer of the camera. Non square pixels are not supported."""
        res = 5.86
        #log.info('Using pixel size %f.' % res)
        return res

    @property
    def gain(self):
        """Set and get the camera gain."""
        return self._handle.Gain

    @gain.setter
    def gain(self, val):
        self._handle.Gain = float(val)

    @property
    def gainvals(self):
        """Get the possible camera gain values.

        The method should return a tuple (g1, g2, ...).

        """
        return tuple(list(np.arange(*self._handle.getFeatureRange('Gain'), 100)))

    @property
    def maxval(self):
        return 2**12-1

    def open(self, camid):
        self._camid = camid
        self._handle = self._vimba.getCamera(camid)
        self._handle.openCamera()
        log.debug('Opened AVT camera %s'%camid)

        self.set_defaults()

    def set_defaults(self):
        self._handle.PixelFormat = 'Mono12'
        self.dtype = np.uint16

        #self._handle.GainAuto = 'Off'
        #self._handle.ExposureAuto = 'Off'

        self._handle.AcquisitionMode = 'Continuous'
        self._handle.Height = self._handle.HeightMax
        self._handle.Width = self._handle.WidthMax
        #self._handle.AcquisitionFrameRateAbs \
        #    = self._handle.getFeatureRange('AcquisitionFrameRateAbs')[1]
        log.debug(self._handle.AcquisitionFrameRateAbs)
        self._handle.SyncOutSelector = 'SyncOut1'
        self._handle.SyncOutSource = 'Exposing'
        self._handle.TriggerSource = 'FixedRate'
        self._handle.ExposureTimeAbs = 10000

    def frame_callback(self, frame):
        arr = np.ndarray(buffer=frame.getBufferByteData(),
                         dtype=self.dtype,
                         shape=(frame.height, frame.width))
        self._imagequeue.put(arr, timeout=1)
        ff = partial(VimbaCamera.frame_callback, self)
        self._frame_funcs[frame] = ff
        frame.queueFrameCapture(ff)

    def close(self):
        if self._handle:
            self._handle.flushCaptureQueue()
            self._handle.endCapture()
            self._handle.revokeAllFrames()
            self._handle.closeCamera()
        self._handle = None
        self._frame_pool = []
        self.emptyqueue()

    def startcontacq(self):
        if not self._acquiring:
            # initialize a bunch of frames for later usage
            self._frame_pool = [self._handle.getFrame()
                                for _ in range(10)]
            self._frame_funcs = {}
            for frame in self._frame_pool:
                frame.announceFrame()
                ff = partial(VimbaCamera.frame_callback, self)
                self._frame_funcs[frame] = ff
                frame.queueFrameCapture(ff)
            self._handle.startCapture()
            self._handle.runFeatureCommand('AcquisitionStart')
            self._acquiring = True
            log.debug('started acquisition')

    def stopcontacq(self):
        if self._acquiring:
            self._handle.runFeatureCommand('AcquisitionStop')
            self._handle.flushCaptureQueue()
            self._handle.endCapture()
            self._handle.revokeAllFrames()
            self._frame_pool = []
            log.debug('stoped acquisition')
        self._acquiring = False




class DummyCamera(Camera):
    VENDOR = 'dummy'

    def __init__(self):
        """A Dummy camera simulating a real one"""
        super(DummyCamera, self).__init__()
        pass
        self._exposure = 1
        self._gain = 1
        self._handle = None
        self._isacquiring = False
        self._imsimthread = None
        self._camid = None

    @property
    def exposure(self):
        """Set and get the camera exposure in ms."""
        return self._exposure

    @exposure.setter
    def exposure(self, val):
        self._exposure = val

    @property
    def exposurebounds(self):
        """Get the camera exposure bounds in ms.

        The method should return a tuple (min, max).

        """
        return (0.1, 100)

    @property
    def pixelsize(self):
        """Return the pixelsize in micrometer of the camera. Non square pixels are not supported."""
        res = 5.3
        #log.info('Using pixel size %f.' % res)
        return res

    @property
    def gain(self):
        """Set and get the camera gain."""
        return self._gain

    @gain.setter
    def gain(self, val):
        self._gain = val

    @property
    def gainvals(self):
        """Get the possible camera gain values.

        The method should return a tuple (g1, g2, ...).

        """
        return (1, 2, 3, 4, 5)

    @property
    def maxval(self):
        """Get the maximum counts per pixel allowed for the active camera.

        This value is used to detect saturation in the image.
        """
        return 256

    def open(self, camid):
        """Open the camera and obtain a camera handle"""
        self._camid = camid
        if camid == 'dummycam1':
            self._handle = 1
        else:
            log.critical('Unknown camera ID.')
            raise ValueError('Unknown camera ID: %s' % camid)

    def close(self):
        """Close the camera"""
        self._camid = None
        self._handle = None

    def startcontacq(self):
        """Start continuous picture acquisition.

        Put acquired images on in the image queue.

        """
        if not self._isacquiring:
            self._isacquiring = True
            if self._imsimthread is None or not self._imsimthread.is_alive():
                self._imsimthread = ImSimThread(self._imagequeue, self._gain, self._exposure, 0.1)
                self._imsimthread.start()

    def stopcontacq(self):
        """Stop  continuous picture acquisition"""
        if self._isacquiring:
            self._isacquiring = False
            self._imsimthread.isrunning = False
            self._imsimthread.join()
            self._imsimthread = None

    def findallcams(self):
        """Find all cameras of this vendor

        Returns
        -------
        cams : dictionary
            Dictionary of all connected cameras where the key is the unique id
            that can be used to obtain a camera handle. The value is a
            description of the camera presented to the user.

        """
        return {'dummycam1': 'Dummy camera 1'}

if __name__ == "__main__":
    cam = UEyeCamera()
    # cammngr = CameraManager([cam])
    # log.debug('Connected cameras: %s' % cammngr.connectedcams)
    # cammngr.setactivecam('dummy', 'dummycam1')
    cam.findallcams()

    cam.open(1)
    #print(cam.gain)
    #print(cam.exposure)
    cam.startcontacq()
    cam.stopcontacq()
    cam.close()
