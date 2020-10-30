#############################################################
"""iter.py holds cycle method called during each iteration"""
#############################################################


from influxdb import InfluxDBClient
from datalogger.logsetup import log
from time import time
from time import sleep


#############################################################


def cycle(sensors,client):
    #sensors: dictionary of the format {trigger:sensorlist}
    for trigger in sensors.keys():
        if trigger.checktrigger():
            for sensor in sensors[trigger]:
                starttime=time()
                sensordata=sensor.exporttoinflux()
                if sensordata is not None:
                    client.write_points(sensordata)
                    endtime=time()
                    log.info("Sensor %s of type %s has exported data via a %s trigger. This took %f seconds." % (sensor.sensor,sensor.type,sensor.trigger,endtime-starttime))
                else:
                    log.warning("Sensor %s of type %s could not export data" % (sensor.sensor,sensor.type))
            sleep(trigger.timeout)


            
            
def snapshot(sensor,client):
    starttime=time()
    sensordata=sensor.exporttoinflux()
    if sensordata is not None:
        client.write_points(sensordata)
        endtime=time()
        log.info("Sensor %s of type %s has exported data via a snapshot. This took %f seconds." % (sensor.sensor,sensor.type,endtime-starttime))
    else:
        log.warning("Sensor %s of type %s could not export data" % (sensor.sensor,sensor.type))
