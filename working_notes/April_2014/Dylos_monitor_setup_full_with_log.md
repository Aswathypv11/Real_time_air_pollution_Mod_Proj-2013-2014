**Dylos_monitor_setup_full_with_log**
Following http://hintshop.ludvig.co.nz/show/persistent-names-usb-serial-devices/ and Udev_rules_for_USB's_attached_to_RPi 

create a udev rule for RPI

edited the file /etc/udev/rules.d

using command

sudo nano /etc/udev/rules.d/90-phone.rules

and add follwoing lines to giving persistant name for USB data card (HUWAEI E303F) and USB to serial cable for Dylos monitor.

KERNEL=="ttyUSB*", ATTRS{idVendor}=="12d1", ATTRS{idProduct}=="1506", NAME="phone", MODE="0666",SYMLINK+="mobile"
KERNEL=="ttyUSB*", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", NAME="dylos", MODE="0666",SYMLINK+="dylos"

by this, while connecting these two devices, the folder /dev shows the files for USB data card and USB to serial cable for Dylos monitor. By this, these device can be refered in python script or gammu-config etc.

Gammu installation

gammu-config , with /dev/phone 
gammu --identify, hangs whole computer, no pinging, and RPI has to be restarted, this is the problem with BBB also, inwhich it even non detect the usb in lsusb.


Found gammu makes problem with RPi, alternative is use it as inetrnet based data tranfer following

http://bigcowpi.blogspot.in/2013/03/raspberry-pi-as-3g-huawei-e303-wireless.html

Internet gets connected with hipuchs, any how try,

Use github as data repository, a alternative to xylos.
cron with git push.
1. Writing code for collecting serial and save it as csv file, Use logging module to save the exception and info into a file. 
2. Exception hanlder for serial connection and data base problem was addressed by follwoing 
http://stackoverflow.com/questions/4508849/how-to-log-python-exception
executing this

```
import logging 
def foo():
    try:
        some_code()
    except:
        logging.exception('')
```
This makes the python command to run silent and error and exception recorded in log file. exception for SERIAl, database was made.
3. The data coming from serial has to be cleaned to remove unwanted chareterc and spaces. used this command

```
a= '2014-04-10T09:35,4941,513    '
>>> b = a.strip( ' \r\n' )
```
Still in sqlite a special chrecters is seen.
4. There is a problem in csv file it is not getting updated, instead overwritten. follwoed this

and changed the flag from 'w' to 'a'
5. In csv file there is a " in each line has to see, finally found a old script written for this and used instead, the script is as follows

```
#!/usr/bin/env python
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=60)
time.sleep(60)

logfile = open('DYLOS_log.csv', 'a')

while 1:
	line = ser.readline() 
	now = time.strftime("%Y-%m-%dT%H:%M:%S:00.000000+0530", time.localtime())
	a =  "%s,%s" % (now,line)
	#print a	
	logfile.write(a)
        logfile.flush()    
logfile.close()
ser.close()

```
6. ##giving github access to RPi##
- followed this to genrate a key
https://help.github.com/articles/generating-ssh-keys
followed this subprocess based python script to make git push
7. ##adding crontab properly with python script itself 
followed
http://stackoverflow.com/questions/8727935/execute-python-script-on-crontab

3. Sqlite database was cleaned by follwoing 
http://stackoverflow.com/questions/4245714/select-numbers-between-a-range-1-to-100-in-sqlite 
and executed the command of
http://stackoverflow.com/questions/4245714/select-numbers-between-a-range-1-to-100-in-sqlite