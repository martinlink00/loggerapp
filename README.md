LOGGERAPP README

1. Short introduction

    - This program is supposed to log temperature data as well as beam-profiler fitdata as well as other log data into an influxdb database using Python 3. The GUI was made with dash. All plots were made using plotly.
    - Note that the GUI is only supposed to control the logging process. This was done to strictly seperate the database (possibly running on a server) from the logger app.
    - Connecting to the camera sensors is achieved by using the class 'cameras' from the beamprofiler program. Acquiring fit data by the cameras also built upon the preexisting class 'analyser', which was modified for this use case
    - Connecting to the temperature sensors was achieved by modifying the preexisting temperature logging program. A good guideline for the usage of the temperature sensor can be found here: https://www.picotech.com/download/manuals/usb-tc08-thermocouple-data-logger-programmers-guide.pdf.
    - Triggering, as well as further data aquisition was done using NI-DAQmx. Documentation can be found here: https://nidaqmx-python.readthedocs.io/en/latest/.
    
    

2. Database and usage

    - The Data storage works with InfluxDB. For more info on how to query and analyse data stored in Influx, see https://docs.influxdata.com/influxdb/v1.7/.
    - Data is saved into a database right now running on localhost:8086 (see db_interface.initiatedb() for more info) called "DB". Each datapoint has a tag called 'sensor'. For each sensor type ('camera', 'temperature' and so on), one corresponding measurement name exists.
    - For camera sensors the measurement is called 'camera', and the sensor tag is a string following the logic "vendor + ' ' + camid+ ' '+ instance". So for example an entry in the database could have the tag {'sensor':'vrm 123 incoming'}. Beam data is written using the float fields 'vcenter', 'hcenter', 'largewaist', 'smallwaist' and 'angle'.
    - Note that one camera can have multiple measuring instances which all export fit data seperately. Each instance has their own ROI, which automatically "follows" the beams. It can also be manually moved in the GUI.
    - For temperature sensors the measurement is called 'temperature', and the sensor tag is a name assigned to a handle via the config file. So the tag dictionary might look like {'sensor':'temperaturesensor123'}. Temperature data is written using float fields (e.g. 'channel1', 'channel2' and so on) which can also be modified in sensorconfig.xml.


3. GUI options

    - The GUI allows the user to turn the datalogging process on and off, and set the rate at which periodically triggered sensors export to the database.
    - It also lets the user see the latest beam images and fit data from all connected cameras.
    - Even when the program thread is not running, the user can create snapshots of the selected camera instance

    


4. Setup
    1. Install required modules and influx
        - Install InfluxDB from https://www.influxdata.com/
        - Install NI-DAQmx from https://www.ni.com/de-de/support/downloads/drivers/download.ni-daqmx.html#348669
        - Install all camera drivers in the loggerapp/datalogger/driver folder
        - Open a command prompt and change the directory to where the program was copied
        - Run "pip install -r requirements.txt"
    2. Initiate Sensors
        - All sensors are configured via the sensorconfig.xml file. When the program encounters a connected sensor, which is not mentioned in the config file, it will offer to automatically edit the xml file via inputs from the command prompt. Thus it is not necessary to manually edit the xml file for each new connected sensor.
        - For automatic xml file editing:
            - Connect all new sensors and run program
            - Follow the instructions in the command line
        - For manually editing the xml file:
            - For camera sensors, include the parameters 'vendor', 'camid' (both used to find and connect to the camera) and 'beam' (used to distinguish between multiple beams on one camera) as well as the desired initial 'roiparams' in the format '(x-Position,y-Position,width,height)' (in pixels). The Roiparams do not need to be very exact, as the program will automatically reset the ROI anyways.
            - For temperature sensors, include the parameter 'handle' used by the DLL to connect to each temperature sensor as well as 'tempid', a name that will be used for this specific device in the database, as well as the measurement labels each channel should hold.

    
    
    
5. Running the program
    - Run 'influxd.exe' from the InfluxDB install
    - Once again, open a command prompt and change the directory to the program directory
    - Run 'python run.py' 
    - You should see an output of the type "Running on https://IP:Port"
    - Open a browser window and copy-paste the adress
 


 
