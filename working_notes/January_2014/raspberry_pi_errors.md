**raspberry_pi_errors**

1. with GSM data caard and serial to usb connected to USB hub
, after connecting GSM data card, few minutes after the ssh is getting disconnected
1. After dismantelling the RPi with RTC, clock time become erroneous, so it was re connected with lots of reboot and set the time mannually using the command

```
sudo hwclock --set --date "01/16/2014 08:33:01"
```

to set the computer time using 

https://wiki.debian.org/DateTime#Set_the_time_manually

date --set 1998-11-02 
     date --set 21:08:00


1. Now RPI is connected with data card, with out connecting seriel to USB wire, now the RPi is working without problem.
data card is checked with sms also, so now connecting the seriel usb to RPi, by connecting the USB seriel second to data card, not showing any problem.

create sqite data base

sudo apt-get install sqlite3 libsqlite3-dev
sqlite3 mydatabase.db
CREATE TABLE data3 (SNo  INTEGER PRIMARY KEY, data VARCHAR(100));