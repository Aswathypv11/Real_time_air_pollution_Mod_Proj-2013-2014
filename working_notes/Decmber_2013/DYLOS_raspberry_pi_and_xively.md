**DYLOS_raspberry_pi_and_xively**

To connect the raspberry pi with Dylos serial to xively IOT, based on
https://sites.google.com/site/benhewitttechnology/raspberry-pi-with-xivley

the written code was this

```
#!/usr/bin/env python
from __future__ import division
import time
import os
import eeml
import sys
import syslog
import json
import serial
import subprocess
import re

a = 0.02832
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=60)
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

var = 1
while var ==1:
   output = subprocess.check_output(["./Adafruit_DHT", "11", "4"]);
   matches = re.search("Temp =\s+([0-9.]+)", output)
   if (not matches):
         time.sleep(3)
         continue
   temp = float(matches.group(1))
   matches = re.search("Hum =\s+([0-9.]+)", output)
   if (not matches):
         time.sleep(3)
         continue
   humidity = float(matches.group(1))
   break  

def dylos_ser():
     dylos = ser.readline() 
     return dylos


API_KEY = 'YgMnMSPFIiAIf8ATTVMC3eUUb4CTrc5adT7pwvopZfbFB976'
FEED = 62987336
API_URL = '/v2/feeds/{feednum}.xml'.format(feednum = FEED)

CPU_temp = getCPUtemperature()
DISK_stats = getDiskSpace()
DISK_total = DISK_stats[0]
DISK_free  = DISK_stats[1]
DISK_perc  = DISK_stats[3]
RAM_stats = getRAMinfo()
RAM_total = round(int(RAM_stats[0]) / 1000,1)
RAM_used  = round(int(RAM_stats[1]) / 1000,1)
RAM_free  = round(int(RAM_stats[2]) / 1000,1)
dylos_red = dylos_ser()
dylos_red1 = dylos_red.split(",")
dylos_red11 = dylos_red1[0]
dylos_red22 = dylos_red1[1]
dylos_05l =float(dylos_red11) / a
dylos_25l =float(dylos_red22) / a
dylos_05ls = str(round(dylos_25l))
dylos_25ls = str(round(dylos_05l))
tempS = str(temp)
HumS = str(humidity)

# open up your feed
pac = eeml.Pachube(API_URL, API_KEY)

#compile dataunit=eeml.NoOfPm3())])

pac.update([eeml.Data("CPU_Temperature", CPU_temp, unit=eeml.Celsius())])
pac.update([eeml.Data("Disk_free", DISK_free, unit=eeml.Celsius())])
pac.update([eeml.Data("RAM__Used", RAM_used, unit=eeml.Celsius())])
pac.update([eeml.Data("RAM_Free", RAM_free, unit=eeml.Celsius())])
pac.update([eeml.Data("Dylos_2.5l", dylos_05ls, unit=eeml.NoOfPm3())])
pac.update([eeml.Data("Dylos_0.5l", dylos_25ls, unit=eeml.NoOfPm3())])
pac.update([eeml.Data("Humidity", HumS, unit=eeml.RH())])
pac.update([eeml.Data("Temperature", tempS, unit=eeml.Celsius())])

#print dylos_red
#print dylos_red1
print dylos_25ls
print dylos_05ls
print dylos_red11
print dylos_red22
print humidity
print temp
# send data to cosm
pac.put()
```

The raspberry pi is connected with Dylos and DHT11 temperature humidity sensor
DHT11 is managed based on adafruit tutorial and the code is using subprocess to get the adafruit code to run to get the Tempa dn RH value from raspebrry pi GPIO.
The xively code is based on eeml, a langauge for real time sensor management, in which the units for each parameter has to be edited to called in xively, So that the eeml code specifying the unit for DYLOS reading was edited
see the code of eeml for python, which was installed as python package the code source has to be edited for including the customized units of DYLOS

this file has to be edited

/usr/local/lib/python2.7/dist-packages/Python_EEML-0.1-py2.7.egg/eeml/__init__.py


the added code was

```
class NoOfPm3(Unit):
    """
    NoOfPm3 unit class.
    """

    def __init__(self):
        """
        Initialize the `Unit` parameters with NoOfPm3.
        """
        Unit.__init__(self, 'NoOfPm3', 'contextDependentUnits', 'No.Of.particle/m3')
class NoOfPo1cuf(Unit):
    """
    NoofP01cuf unit class.
    """

    def __init__(self):
        """
        Initialize the `Unit` parameters with NoOfP01cuf.
        """
        Unit.__init__(self, 'NoofP01cuf', 'contextDependentUnits', 'No.Of.particleper01cuf')

```