#############################
"""Defines triggerevents."""
#############################


from time import time


#############################


class Trigger:
    def __init__(self,typ):
        self._typ=typ
        
    def checktrigger(self):
        #Trigger specific trigger, should return True in case of triggerevent and False elsewise.
        pass
        
class PeriodicTrigger(Trigger):
    """Triggers periodically at a specific rate."""
    def __init__(self,rate):
        super(PeriodicTrigger, self).__init__("periodic")
        self._timecounter=time()
        self._rate=rate
    
    def checktrigger(self):
        if self._rate<time()-self._timecounter<self._rate+self._rate+0.01:
            self._timecounter=time()
            return True
        return False
    
        