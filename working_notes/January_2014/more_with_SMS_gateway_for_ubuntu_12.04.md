**more_with_SMS_gateway_for_ubuntu_12.04**

* based on this

http://blog.sleeplessbeastie.eu/2012/07/16/kalkun-how-to-setup-sms-gateway-at-home/

http://back2arie.wordpress.com/2010/07/27/using-gammu-smsd-with-multiple-phone/


* problem rectified by 

http://askubuntu.com/questions/211739/gammu-and-device-permissions

* steps followed are

installed 

1. sudo apt-get install gammu gammu-smsd
2. sudo cp /usr/share/doc/gammu/examples/config/gammurc /etc/gammurc
the gammurc file will not be there, has to do this step,
instaed of running gammu-conifg is a problem and make gammurc files in home folder
3. now run 
gammu --identify, it gives
no phone detected or some other error

4. for this the config file gammurc has to edited as per like this

```
[gammu]

device = /dev/phone
connection = at

to makde the /dev/phone, the udev files has to be created, inside 

/etc/udev/rules.d, with file name 90-phone.rules, with this contents

KERNEL=="ttyUSB*", ATTRS{idVendor}=="12d1", ATTRS{idProduct}=="1436", NAME="phone", MODE="0666",SYMLINK+="phone"
KERNEL=="ttyUSB*", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", NAME="dylos", MODE="0666",SYMLINK+="dylos"



 ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", SYMLINK+="dylos"
```

now reboot the system, now inside the /dev folder there will be phone file

change the gammurc file as earlier and reboot

now gammu --identify can be run with out sudo

it shows

gammu --identify
Device               : /dev/phone
Manufacturer         : Huawei
Model                : E173 (E173)
Firmware             : 11.126.30.00.00
IMEI                 : 868860005573702
SIM IMSI             : 404805166582360

now go to gammu-smsd

it remove file permission error like this, if it running gammu --identify with sudo

```
 gammu-smsd -c /etc/gammu-smsdrc
Can't open log file "/var/log/gammu-smsd.log"
Failed to read config: Can not open specified file.
```

by rectifying the gammu --identify with out sudo, by this now the gammu-smsdrc will also be running and storing the received sms in its in box of mysql if it is configured as per the earlier references, te gammu-smsdrc config file look like this

```
[gammu]
device = /dev/phone
connection = at

[smsd]
PIN=9999
runonreceive = /var/www/kalkun/scripts/daemon.sh
logfile = /var/log/gammu-smsd.log
commtimeout = 10
sendtimeout = 20
deliveryreport = log
phoneid = mdsms
transmitformat = auto

#Storage - MySQL
service = SQL
driver = native_mysql
database = kalkun
user = yourrootname
password = yourpassword
pc = localhost

#Storage - Files
#service = FILES
#inboxpath = /home/milosz/sms/inbox/
#outboxpath = /home/milosz/sms/outbox/
#sentsmspath = /home/milosz/sms/sent/
#errorsmspath = /home/milosz/sms/error/
#inboxformat = standard
```

and also the mysql has to given with a database and sql import from the sql file provided with the gammu or gammu-smsd, to unzip the gz files use 

sudo gzip -d pgsql.sql.gz

in this folder 

/usr/share/doc/gammu/examples/sql

now the kalkun is not working has to see other time