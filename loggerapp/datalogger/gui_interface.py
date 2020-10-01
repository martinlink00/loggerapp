#####################################################################################################################
"""gui_interface.py provides necessary tools for the GUI to communicate with the cameras, as well as the database"""
#####################################################################################################################


import numpy as np
import math

import loggerapp.datalogger.iter as run
import loggerapp.datalogger.Thread as Thread
import loggerapp.datalogger.datalogger as dat
import loggerapp.datalogger.db_interface as db

import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as subplt


#####################################################################################################################


class Guiinterfacelogger:
    """This class provides essential tools for the datalogger to communicate with the GUI (loggerapp)"""
    def __init__(self,rate,database="DB",host="localhost",port=8086):
        self.camviewer=Camviewer()
        self._rate=rate
        self.sensormngr=dat.Sensormanager()
        self._client=db.initiatedb(database,host,port)
        self.thread=Thread.PeriodicTimer(0,run.cycle,self.sensormngr.getsensordict(),self._client)
        
    
    def snapshot(self):
        if self.camviewer.getselectedcam() is not None:
            run.snapshot(self.camviewer.getselectedcam(),self._client)
    

    def getrate(self):
        return self._rate
    
    def setrate(self,rate):
        """Changes the rate at which periodic sensors are exporting"""
        if self._rate!=rate:
            self._rate=rate
            for sens in self.sensormngr.getperiodiclist():
                sens.trigger.setrate(rate)
        else:
            pass


 
        
    def selectcam(self,sensorid):
        for sensor in self.sensormngr.getsensorlist():
            if sensor.type=='camera' and sensor.sensor==sensorid:
                self.camviewer.setselectedcam(sensor)

                
    def fitvis(self):
        """Returns plotly figure for UI, and saves latest image"""
        pixel=self.camviewer.pixelsize
        client=self._client
        
        if self.camviewer.latestimage() is not None:
            #Extract Image Data
            
            latestdata=db.getlatestdata(client,self.camviewer.getselectedcam().sensor)
            fullimg=self.camviewer.latestimage()
            roiimg=self.camviewer.latestroi()
            roiparams=self.camviewer.latestroiparams()
            profsandfits=self.camviewer.latestroiprofs()
            
            
            #Extracted ROI Data
            
            posx=roiparams[0]
            posy=roiparams[1]
            width=roiparams[2]
            height=roiparams[3]
            
            #Extracted Beam Data in mum and pixels
            
            vcentermum=latestdata['vcenter']
            hcentermum=latestdata['hcenter']
            largewaistmum=latestdata['largewaist']
            smallwaistmum=latestdata['smallwaist']
            
            vcenter=vcentermum/pixel
            hcenter=hcentermum/pixel
            largewaist=largewaistmum/(4*pixel)
            smallwaist=smallwaistmum/(4*pixel)
            
            ang=latestdata['angle']
                        
            
            ##Indicator shapes
            
            #Corners for ROI
            
            corner1=[posx,posy]
            corner2=[width+posx,height+posy]
            
            #Beamposition of Center
            
            beampos=[hcenter,vcenter]
            beamposrel=[beampos[0]-corner1[0],beampos[1]-corner1[1]]
            
            ##Complete image plot
            

            fig1=px.imshow(fullimg)
            fig1.update_layout(
                coloraxis_showscale=False
            )
            
            #Implement indicator shapes
            
            fig1.update_layout(
                shapes=[
                    #ROI rectangle
                    dict(
                        type="rect",
                        x0=corner1[0],
                        y0=corner1[1],
                        x1=corner2[0],
                        y1=corner2[1],
                        line=dict(
                            color="RoyalBlue",
                        )
                    )
                ]
            )
            fig1.write_html("latestimages/latestimage.html")
            
            ##ROI image plot
            
            #Line styles for waist indication
            lslw = dict(color="LightSeaGreen",width=3) #long waist
            lssw = dict(color="DarkRed",width=3) #short waist
            
            
            fig2=px.imshow(roiimg)
            
            steps=np.arange(0,2*math.pi,0.05)
            xx=[largewaist*math.cos(t)*math.cos(math.radians(-ang))-smallwaist*math.sin(math.radians(-ang))*math.sin(t)+beamposrel[0] for t in steps]
            yy=[largewaist*math.cos(t)*math.sin(math.radians(-ang))+smallwaist*math.cos(math.radians(-ang))*math.sin(t)+beamposrel[1] for t in steps]

            fig2.add_trace(go.Scatter(x=xx,y=yy,mode='lines',line=dict(color='lightgreen', width=2)))
            
            
            
            fig2.update_layout(
                coloraxis_showscale=False,
                showlegend=False,
                shapes=[
                    #Long waist line
                    dict(
                        type="line",
                        x0=xx[63],
                        y0=yy[63],
                        x1=xx[0],
                        y1=yy[0],
                        line=lslw                       
                    ),
                    #Short waist line
                    dict(
                        type="line",
                        x0=xx[31],
                        y0=yy[31],
                        x1=xx[94],
                        y1=yy[94],
                        line=lssw                       
                    ),
                    #Center circle
                    dict(
                        type="circle",
                        xref="x",
                        yref="y",
                        fillcolor="black",
                        x0=beamposrel[0]-1,
                        y0=beamposrel[1]-1,
                        x1=beamposrel[0]+1,
                        y1=beamposrel[1]+1
                    ),
                ]
            )
            
            
            fig2.write_html("latestimages/latestroi.html")
            
            ##Fit visualization plots
            
            #Linestyles for plots
            
            ls1=dict(color='LightSkyBlue', width=4) #Lines for profile plot along x and y
            ls2=dict(color='orangered', width=4) #Lines for profile plot along axis
            ms=dict(color='black', size=5) #Marker style
            
            
            fig3=subplt.make_subplots(rows=2, cols=2,
                subplot_titles=("Horizontal profile", 
                                "Profile along long axis",
                                "Vertical profile",
                                "Profile along short axis")
            )
            

                                    
            
            fig3.add_trace(go.Scatter(x=np.arange(height),y=profsandfits[0],mode='markers',marker=ms),row=1,col=1)
            
            fig3.add_trace(go.Scatter(x=np.arange(height),y=profsandfits[1],mode='lines',line=ls1),row=1,col=1)
                        

            fig3.add_trace(go.Scatter(x=np.arange(width),y=profsandfits[2],mode='markers',marker=ms),row=2,col=1)
            
            fig3.add_trace(go.Scatter(x=np.arange(width),y=profsandfits[3],mode='lines',line=ls1),row=2,col=1)
            
            
            fig3.add_trace(go.Scatter(x=np.arange(height),y=profsandfits[4],mode='markers',marker=ms),row=1,col=2)
            
            fig3.add_trace(go.Scatter(x=np.arange(height),y=profsandfits[5],mode='lines',line=ls2),row=1,col=2)
            
            
            fig3.add_trace(go.Scatter(x=np.arange(width),y=profsandfits[6],mode='markers',marker=ms),row=2,col=2)
            
            fig3.add_trace(go.Scatter(x=np.arange(width),y=profsandfits[7],mode='lines',line=ls2),row=2,col=2)
            

            
            
            fig3.update_layout(showlegend=False)
            
            
            ##Table string data
            
            hcenterout = str(round(hcentermum,1)) + " μm"
            vcenterout = str(round(vcentermum,1)) + " μm"
            lwout = str(round(largewaistmum,1)) + " μm"
            swout = str(round(smallwaistmum,1)) + " μm"
            angout = str(round(ang,1)) + "°"
            roiposout = "(%i, %i)" % (posx,posy)
            roiwidthout = str(width) + " px"
            roiheightout = str(height) + " px"
            pixelout = str(round(pixel,1)) + " μm/px"
            
            
            
            return fig1, fig2, fig3, hcenterout, vcenterout, lwout, swout, angout, roiposout, roiwidthout, roiheightout, pixelout
        else:
            blackimg=px.imshow(np.zeros((200,200)))
            blackimg.update_layout(coloraxis_showscale=False)
            return blackimg,blackimg,blackimg, 0, 0, 0, 0, 0, 0, 0, 0, 0

 

    

class Camviewer:
    def __init__(self):
        self._selectedcam=None
        self._hasactivecam=False
        self.pixelsize=None
        

    def setselectedcam(self,sensor):
        if self._hasactivecam:
            if self._selectedcam!=sensor:
                self._selectedcam=sensor
                self.pixelsize=sensor.IA.pixelsize
        else:
            self._selectedcam=sensor
            self.pixelsize=sensor.IA.pixelsize
            self._hasactivecam=True 
                
                
    def getselectedcam(self):
        return self._selectedcam
        
        
        
    def latestimage(self):
        if self._hasactivecam:
            return self._selectedcam.latestimage
    def latestroi(self):
        if self._hasactivecam:
            return self._selectedcam.latestroi
    
    def latestroiparams(self):
        if self._hasactivecam:
            return self._selectedcam.latestroiparams
        
    def latestroiprofs(self):
        if self._hasactivecam:
            hroiprof=self._selectedcam.IA.hroiprof
            vroiprof=self._selectedcam.IA.vroiprof
            longroiprof=self._selectedcam.IA.longroiprof
            shortroiprof=self._selectedcam.IA.shortroiprof
            hroifit=self._selectedcam.IA.hroifit
            vroifit=self._selectedcam.IA.vroifit
            longroifit=self._selectedcam.IA.longroifit
            shortroifit=self._selectedcam.IA.shortroifit
            
            return hroiprof, hroifit, vroiprof, vroifit, longroiprof, longroifit, shortroiprof, shortroifit
