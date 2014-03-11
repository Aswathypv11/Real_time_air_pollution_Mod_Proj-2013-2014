**DYLOS_raspberry_pi_experiment**

The Dylos air quality monitor with serial to USB port was connected tot the raspberry pi, raspberry pi is connected through mini usb for power, LAN is connected to RPi, for SD card preparation followed this

* using DD already had .img file of old raspberry pi SD card linux files
* then to make fresh SD card for RPi, SD card is formated with FAT file formate and then run
* df -h to view the currently mounted devices,
* it shows the presence of “/dev/mmcblk0p1”
* then unmounted the /dev/mmcblk0p1
* then ran this command
    dd bs=4M if=~/2012-12-16-wheezy-raspbian.img of=/dev/mmcblk0
* it took several hours to perform
* then remove cache by
    sudo sync
and safely removed the card

Now raspberry pi is working from the SD card
based on http://elinux.org/RPi_Easy_SD_Card_Setup

* Steps for viewing the attached serial to USB deivces in case of DYLOS air quality moniotr /dev

dmesg | grep -i tty

based on http://www.linfo.org/dmesg.html
* Now to use this for data logging and GSM data transmission
for data logging python script from this replay #3 http://forum.arduino.cc/index.php?topic=105148.0 was used
```
import serial
import time
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=60)
time.sleep(60)
logfile = open('test.csv', 'a')
while 1:
        line = ser.readline()
        now = time.strftime("%Y-%m-%dT%H:%M:%S:00.000000+0530", time.localtime())
        a =  "%s,%s" % (now,line)
        print a
        logfile.write(a)
        logfile.flush()
logfile.close()
ser.close()
```
* To make the RPi run automatically this script for every reboot, followed this well written tutorial
http://blog.scphillips.com/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/
the steps were

* added this line to the first line of python script

     #!/usr/bin/env python

* then moved this file to the location of /usr/local/bin/myservice here myservice folder has to  be created
* give execute command for the file
    chmod 755 pythonscript.py
* then create a file in /etc/init.d as pythonscript.sh
* add following codes in it
```
     #!/bin/sh
     ### BEGIN INIT INFO
     # Provides: myservice
     # Required-Start: $remote_fs $syslog
     # Required-Stop: $remote_fs $syslog
     # Default-Start: 2 3 4 5
     # Default-Stop: 0 1 6
     # Short-Description: Put a short description of the service here
     # Description: Put a long description of the service here
     ### END INIT INFO
     # Change the next 3 lines to suit where you install your script and what you want to call it
    DIR=/usr/local/bin/myservice
    DAEMON=$DIR/pythonscript.py
    DAEMON_NAME=pythonscript

    # This next line determines what user the script runs as.
    # Root generally not recommended but necessary if you are using the Raspberry Pi GPIO from Python.
    DAEMON_USER=root

    # The process ID of the script when it runs is stored here:
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
* give execute command for this file
    chmod 755 pythonscript.sh
* now test it with this command

    sudo /etc/init.d/pythonscript start

    it will show

    [ ok ] Starting system dylos_csv_ser daemon:.

* now give this command

    sudo /etc/init.d/dylos_csv_ser.sh stop

    it give this error [….] Stopping system dylos_csv_ser daemon:start-stop-daemon: warning: failed to kill 2794: No such process No process in pidfile ‘/var/run/dylos_csv_ser.pid’ found running; none killed.
* Check any pesky mistake in the python script python script has to run with this command it self
    cd into the python script directory then run ./pythonscript.py it has to run other wise problem is in python script, mine was due to a space in front of the python (Hrrrrrrah) interpreter in the python script

    #!/usr/bin/env python

    after changing this all are fine

* Another tips to rename files in linux

mv file1 file2

have to careful it can replace the file, can see more option in
http://www.cyberciti.biz/faq/linux-rename-file/

that is it, python script is in daemon and keep automatically work after rebooting.
For GSM based transmission of DYLOS reading, use http://misc.flogisoft.com/phone/gammu_send_sms
