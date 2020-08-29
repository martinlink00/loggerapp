########################################################################################
"""db_interface.py provides basic tools for communication with an influxdb database"""
########################################################################################


from influxdb import InfluxDBClient
import datalogger.datalogger as datl


########################################################################################


def extractdatahist(client,beamselec,fieldselec,xrange):
    """Returns data from a client as tuple"""
    res=client.query('select * from "camera" where time <='+xrange[1]+' and time >='+xrange[0])
    points=res.get_points(tags={'sensor':beamselec})
    d=[]
    t=[]
    
    for i in points:
        d.append(i[fieldselec])
        t.append(i['time'])
        
    return t, d




def getlatestdata(client,beamselec):
    """Returns latest data entry of a client"""
    res=client.query('SELECT * FROM "camera" GROUP BY * ORDER BY DESC LIMIT 1')
    points=res.get_points(tags={'sensor':beamselec})
    for i in points:
        return i

def sensorsindb(client,type):
    """Returns a list of all beam sensors of a client"""
    queryst='SELECT * FROM "' + type + '"'
    res=client.query(queryst)
    points=res.get_points()
    l=[]
    for i in points:
        if i['sensor'] not in l:
            l.append(i['sensor'])

    return l
            

def initiatedb(db="LabLog",host="localhost",port=8086):
    """Returns a client with the active Database DB"""
    client=InfluxDBClient(host,port)
    #Note that client.create_database(db) does nothing if the Database db already exists
    client.create_database(db)
    client.switch_database(db)
    return client

    




