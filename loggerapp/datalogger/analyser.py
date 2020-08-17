#######################################################################################################
"""This module holds the Imageanalyser class which manages the image analysis as the name suggests."""
#######################################################################################################

import numpy as np

import scipy.optimize as opt
import scipy.ndimage.interpolation as rot

from datalogger.logsetup import log


#######################################################################################################


class ImageAnalyser(object):
    def __init__(self):
        """The ImageAnalyser manages all image analysis functions.

        """
        super(ImageAnalyser, self).__init__()
        self._image = None
        self._roiimage = None
        self._pixelsize = None
        self.isrecording = False
        # roi stuff
        self._roiposx = None
        self._roiposy = None
        self._roiimgwidth = None
        self._roiimgheight = None
        # fitting related stuff
        self._vfitparams = None
        self._hfitparams = None
        self._lfitparams = None
        self._sfitparams = None
        self._fitangle = None #in degrees
        
        

    
    
    @property
    def roiimgheight(self):
        return self._roiimgheight

    @property
    def roiimgwidth(self):
        return self._roiimgwidth
    
    
    @roiimgheight.setter
    def roiimgheight(self,val):
        self._roiimgheight=val
    
    @roiimgwidth.setter
    def roiimgwidth(self,val):
        self._roiimgwidth=val
        


    @property
    def roiposx(self):
        return self._roiposx

    @roiposx.setter
    def roiposx(self,val):
        self._roiposx=val
    
    @property
    def roiposy(self):
        return self._roiposy
    
    @roiposy.setter
    def roiposy(self,val):
        self._roiposy=val
    
    
    @property
    def image(self):
        """The image."""
        return self._image

    @image.setter
    def image(self, val):
        self._image = val    

    @property
    def roiimage(self):
        return self.image[self._roiposy:self._roiimgheight+self._roiposy,self._roiposx:self._roiimgwidth+self._roiposx]
    

    @property
    def rotimage(self):
        """Rotated image. The large elliptical semi axis should be parallel to the x-axis."""
        rotimg = rot.rotate(self.roiimage,-self._fitangle,reshape=False,mode="reflect")
        return rotimg
        
        
    @property
    def hasimage(self):
        if self._image is not None:
            return True
        else:
            return False
        
        
        

    @property
    def imgheight(self):
        return self._image.shape[0]

    @property
    def imgwidth(self):
        return self._image.shape[1]
    
    @property
    def rotimgheight(self):
        return self.rotimage.shape[0]
    
    @property
    def rotimgwidth(self):
        return self.rotimage.shape[1]
    
    
    
    
    @property
    def pixelsize(self):
        """The camera pixelsize in micrometer. Non square pixels are not supported by this program."""
        return self._pixelsize

    @pixelsize.setter
    def pixelsize(self, val):
        self._pixelsize = val

        
        
        
    @property
    def vroiprof(self):
        """The vertical profile (sum) over the roi image."""
        return self.roiimage.sum(axis=0)

    @property
    def hroiprof(self):
        """The horizontal profile (sum) over the roi image."""
        return self.roiimage.sum(axis=1)
    
    @property
    def longroiprof(self):
        """The profile(sum) along the long elliptical beam axis."""
        return self.rotimage.sum(axis=1)
    
    
    
        
    
    @property
    def shortroiprof(self):
        """The profile(sum) along the short elliptical beam axis."""
        return self.rotimage.sum(axis=0)
    
    
    @property
    def longroifit(self):
        """Returns the gaussfit of the profile along the long elliptical semi axis"""
        xx = np.arange(0,self.rotimgheight)
        if self._sfitparams is not None:
            return self._gaussfit(xx,self._sfitparams)
        else:
            return None
                           
    @property
    def shortroifit(self):
        """Returns the gaussfit of the profile along the short elliptical semi axis"""
        xx=np.arange(0,self.rotimgwidth)
        if self._lfitparams is not None:
            return self._gaussfit(xx,self._lfitparams)
        else:
            return None
 
        
    @property
    def vroifit(self):
        """Return the gaussfit of the vertical profile"""
        xx = np.arange(0, self.roiimgwidth)
        if self._hfitparams is not None:
            return self._gaussfit(xx, self._hfitparams)
        else:
            return None

    
    
    @property
    def hroifit(self):
        """Return the gaussfit of the horizontal profile"""
        xx = np.arange(0, self.roiimgheight)
        if self._vfitparams is not None:
            return self._gaussfit(xx, self._vfitparams)
        else:
            return None

        
        
        
        
    
    

    @property
    def imageoffset(self):
        """Get the mean count per pixel in the region where no beam is.

        Notes
        -----
        Obviously this function will not work as expected if the beam is on the
        edge of the image (displacement, large beam).

        """
        return (self._image[0:10, :].mean() + self._image[-10:, :].mean()) / 2

    
    
    
    
    
    def findnewroicenter(self,formerroi):
        """Estimates the beam center and resets the ROI, so that the beam always hits in the center"""
        vsum=np.sum(formerroi,axis=0)
        hsum=np.sum(formerroi,axis=1)
        hcest=np.argmax(vsum)
        vcest=np.argmax(hsum)
        newposx=int(self.roiposx+hcest-self.roiimgwidth/2)
        newposy=int(self.roiposy+vcest-self.roiimgheight/2)
        if 0<=newposx<=self.imgwidth-self.roiimgwidth:
            self._roiposx=newposx
        else:
            log.warn("Could not find new ROI x-Position because beam is too close to the edges")
        if 0<=newposy<=self.imgheight-self.roiimgheight:
            self._roiposy=newposy
        else:
            log.warn("Could not find new ROI y-Position because beam is too close to the edges")
        
        

    def setroi(self,posx=None,posy=None,width=None,height=None):
        """Finds and sets ROI in image"""
        if self.image is not None:

            if (self._roiposx,self._roiposy,self._roiimgwidth,self._roiimgheight) != (None,None,None,None):
                self.findnewroicenter(self.roiimage)

            if posx is not None:
                self._roiposx=posx

            if posy is not None:
                self._roiposy=posy

            if width is not None:
                self._roiimgwidth=width

            if height is not None:
                self._roiimgheight=height
                
        
        else:
            log.warn("Could not set ROI because image is None")
     
    
            
            
            
    def getfitdata(self):
        """Fits image and returns vcenter, hcenter, vwidth, hwidth as well as the beam angle"""

        self.fitangle()
        self.fitprofiles()

        try:
            if self._hfitparams is not None and self._vfitparams is not None and self._lfitparams is not None and self._sfitparams is not None:
                if np.abs(self._lfitparams[2])<max(self.imgheight/2,self.imgwidth/2) and np.abs(self._sfitparams[2])<max(self.imgheight/2,self.imgwidth/2):
                    vc=(self._vfitparams[1]+self._roiposy) * self._pixelsize
                    hc=(self._hfitparams[1]+self._roiposx) * self._pixelsize
                    lsa=4*np.abs(self._lfitparams[2]) * self._pixelsize
                    ssa=4*np.abs(self._sfitparams[2]) * self._pixelsize


                    data=[]
                    data.append(hc)
                    data.append(vc)
                    data.append(lsa)
                    data.append(ssa)
                    data.append(self._fitangle)


                    return data
                else:
                    log.warn("Unrealistic waist fits were acquired. Data export was supressed.")
                    return None


            else:
                return None
        except:
            log.debug("Error in getfitdata()")
            return None

        
        
        
        
    def _maxprofile(self,ang):
        """Finds the maximum horizontal sum after a rotation (should reach minimum for large semi-axis of the beam horizontal)"""
        roi=rot.rotate(self.roiimage,angle=ang, reshape=False)
        list=roi.sum(axis=1)
        return -1*np.amax(list)
        
        
    def fitangle(self):
        """Fits the angle of the beam in the interval (-90,90)"""
        try:
            ang = -opt.minimize_scalar(self._maxprofile,bounds=(-90, 90), method='bounded').x
            self._fitangle=ang
                    
        except:
            return None
            

    
    def _gaussfit(self, x, p):
        """Fit function"""
        return p[0] * np.exp(-(x - p[1])**2 / 2 / p[2]**2) + p[3]

    def _gaussfitdiff(self, p, x, y):
        """The fit error function"""
        return self._gaussfit(x, p) - y
    
    

    def fitprofiles(self):
        """Fit the horizontal and vertical profile, as well as the profiles along the long and short elliptical axis."""
        xx = np.arange(0, self.roiimgwidth)
        yy = np.arange(0, self.roiimgheight)
        try:
            fitres1 = opt.leastsq(self._gaussfitdiff, (self.roiimgheight / 10 * 100, self.roiimgheight / 2, self.roiimgheight / 10, self.imageoffset * self.roiimgwidth), args=(yy, self.hroiprof))
            self._vfitparams = fitres1[0]
        except:
            log.debug("VFIT Error")
            self._vfitparams = None

        try:
            fitres2 = opt.leastsq(self._gaussfitdiff, (self.roiimgwidth / 10 * 100, self.roiimgwidth / 2, self.roiimgwidth / 10, self.imageoffset * self.roiimgheight), args=(xx, self.vroiprof))
            self._hfitparams = fitres2[0]
        except:
            log.debug("HFIT Error")
            self._hfitparams = None

            
        try:
            fitres3 = opt.leastsq(self._gaussfitdiff, (self.roiimgheight / 10 * 100, self.roiimgheight / 2, self.roiimgheight / 10, self.imageoffset * self.roiimgwidth), args=(yy, self.longroiprof))
            self._sfitparams = fitres3[0]
        except:
            log.debug("SFIT Error")
            self._sfitparams = None

        try:
            fitres4 = opt.leastsq(self._gaussfitdiff, (self.roiimgwidth / 10 * 100, self.roiimgwidth / 2, self.roiimgwidth / 10, self.imageoffset * self.roiimgheight), args=(xx, self.shortroiprof))
            self._lfitparams = fitres4[0]
        except:
            log.debug("LFIT Error")
            self._lfitparams = None
        
  
