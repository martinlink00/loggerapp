#############################
"""Defines triggerevents."""
#############################


import nidaqmx
from time import time
from datalogger.logsetup import log


#############################


class Trigger:
    def __init__(self,typ):
        self.typ=typ
        
    def checktrigger(self):
        #Trigger specific trigger, should return True in case of triggerevent and False elsewise.
        pass
        
class PeriodicTrigger(Trigger):
    """Triggers periodically at a specific rate."""
    def __init__(self,rate):
        super(PeriodicTrigger, self).__init__("periodic")
        self._timecounter=time()
        self._rate=rate
        
    def setrate(self,rate):
        self._rate=rate
    
    def checktrigger(self):
        if self._rate<time()-self._timecounter:
            self._timecounter=time()
            return True
        
        return False
    

class NationalTrigger(Trigger):
    """National instruments DAQ Trigger."""
    def __init__(self,channel,threshhold):
        super(NationalTrigger,self).__init__("national")
        self._channel=channel
        self._threshhold=threshhold
            
    def checktrigger(self):
        with nidaqmx.Task() as task:
            task.ai_channels.add_ai_voltage_chan(self._channel)
            output=task.read()
        
        if output>=self._threshhold:
            return True
        
        return False
        
        
