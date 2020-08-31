#############################################################
"""iter.py holds cycle method called during each iteration"""
#############################################################


from influxdb import InfluxDBClient
from datalogger.logsetup import log
from time import time


#############################################################


def cycle(sensors,client):
        for sensor in sensors:
            if sensor.trigger.checktrigger():
                starttime=time()
                sensordata=sensor.exporttoinflux()
                if sensordata is not None:
                    client.write_points(sensordata)
                    endtime=time()
                    log.info("Sensor %s of type %s has exported data via a %s trigger. This took %f seconds." % (sensor.sensor,sensor.type,sensor.trigger.typ,endtime-starttime))
                else:
                    log.warning("Sensor %s of type %s could not export data" % (sensor.sensor,sensor.type))
            

            
            
def snapshot(sensor,client):
    starttime=time()
    sensordata=sensor.exporttoinflux()
    if sensordata is not None:
        client.write_points(sensordata)
        endtime=time()
        log.info("Sensor %s of type %s has exported data via a snapshot. This took %f seconds." % (sensor.sensor,sensor.type,endtime-starttime))
    else:
        log.warning("Sensor %s of type %s could not export data" % (sensor.sensor,sensor.type))
