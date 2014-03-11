**Daemon_service_for_RPI_for_running_python_script**
To make a python script run in demaon which stores serial reading into a csv file and send one serial read value into SMS.

* First save the python script as my service inside this folder make it executable

/usr/local/bin/myservice/myscript.py

```
#!/usr/bin/env python
import serial
import time
import gammu

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
time.sleep(180)
SMS = {
        'Class': 1,                            #SMS Class
        'Text': a,     #Message
        'SMSC': {'Location': 1},
        'Number': "",              #The phone number
      }
gamu_sm = gammu.StateMachine()
gamu_sm.ReadConfig()              #Read the default config file (~/.gammurc)
gamu_sm.Init()                    #Connect to the phone   
gamu_sm.SendSMS(SMS)

```

* then make a sh script in 
/etc/init.d/

```
#!/bin/sh
 
###BEGIN INIT INFO
#Provides: myservice
#Required-Start: $remote_fs $syslog
#Required-Stop: $remote_fs $syslog
#Default-Start: 2 3 4 5
#Default-Stop: 0 1 6
#Short-Description: Put a short description of the service here
#Description: Put a long description of the service here
###END INIT INFO
 
#Change the next 3 lines to suit where you install your script and what you want to call it
DIR=/usr/local/bin/myservice
DAEMON=$DIR/dylos_csv_ser.py
DAEMON_NAME=dylos_csv_ser
 
#This next line determines what user the script runs as.
#Root generally not recommended but necessary if you are using the Raspberry Pi GPIO from Python.
DAEMON_USER=root
 
#The process ID of the script when it runs is stored here:
PIDFILE=/var/run/$DAEMON_NAME.pid
 
. /lib/lsb/init-functions
 
do_start () {
log_daemon_msg "Starting system $DAEMON_NAME daemon"
start-stop-daemon --start --background --pidfile $PIDFILE --make-pidfile --user $DAEMON_USER --startas $DAEMON
log_end_msg $?
}
do_stop () {
log_daemon_msg "Stopping system $DAEMON_NAME daemon"
start-stop-daemon --stop --pidfile $PIDFILE --retry 10
log_end_msg $?
}
 
case "$1" in
 
start|stop)
do_${1}
;;
 
restart|reload|force-reload)
do_stop
do_start
;;
 
status)
status_of_proc "$DAEMON_NAME" "$DAEMON" && exit 0 || exit $?
;;
*)
echo "Usage: /etc/init.d/$DEAMON_NAME {start|stop|restart|status}"
exit 1
;;
 
esac
exit 0
```

* then make it executable by

sudo chmod 755 /etc/init.d/NameOfYourScript

* then make it into start up by 

sudo update-rc.d NameOfYourScript defaults 

this command has to run catuosly, will be different according to the OS distribution.

* based on
http://blog.scphillips.com/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/

http://www.stuffaboutcode.com/2012/06/raspberry-pi-run-program-at-start-up.html

* RPi Email IP On Boot Debian

http://elinux.org/RPi_Email_IP_On_Boot_Debian

