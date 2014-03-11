**Testing_the_RPi_with_usb_hub_usb_serial_and_data_card**

with one set of RPi, UH,US,DC there is problem of ssh and ping if it is connected with proper set up, that is RPI, UH and LAN. 
1. with huge number of iteration starting from suspecting starrting with UH adaptor, then UH itslef, then RPi and then wire connecting with UH and RPI, found the problem with wire connecting UH and RPi. 
1. With this set then started the connection of DC, it was not recognized by lsusb, then connected the US, US was recognized but no DC, then DC was removed and connected to the USB point nearer to light now lsusb showed the DC and recognized, but after a while LAN connection was disrupted and no pinging also. So for this case the problem zeroed to RPi and RPi was changed to new one.
1. Witht this new RPi all set up was working fine, that is RPi, UH, DC and US. Made a /etc/udev/rules.d/90-phone.rules with this lines
KERNEL=="ttyUSB*", ATTRS{idVendor}=="12d1", ATTRS{idProduct}=="1436", NAME="phone", MODE="0666",SYMLINK+="phone"
KERNEL=="ttyUSB*", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", NAME="dylos", MODE="0666",SYMLINK+="dylos"
1. now the /dev/phone and /dev/dylos was getting created with subsequent reboot. One exception was found if the set up RPi, UH, DC and US was removed from power and restarted the /dev/phone was not created, it is found to be problem with usb mode switch, since the lsusb shows the DC as 

Bus 001 Device 009: ID 12d1:1446 Huawei Technologies Co., Ltd. 

This problem gets solved by removing DC and reconnecting to the UH, now /dev/phone is being created with a reboot
1. serious problem with connecting wire of UH and RPi, it makes UH to stop working if connected to UH. now exchanged the US wire with this one now working, US also working have to check with dylos. Have to check RTC also.
1. Now the status is, if RPi is completely get switched off (power off) the data card will be detetcted as 

```
pi@raspberrypi ~ $ lsusb
Bus 001 Device 002: ID 0424:9512 Standard Microsystems Corp. 
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 001 Device 003: ID 0424:ec00 Standard Microsystems Corp. 
Bus 001 Device 004: ID 1a40:0101 Terminus Technology Inc. 4-Port HUB
Bus 001 Device 005: ID 1a40:0101 Terminus Technology Inc. 4-Port HUB
Bus 001 Device 006: ID 067b:2303 Prolific Technology, Inc. PL2303 Serial Port
Bus 001 Device 007: ID 12d1:1446 Huawei Technologies Co., Ltd. E1552/E1800/E173 (HSPA modem)
```

Since Huwaei as 12d1:1446 it will be detetced as modem and cannot send SMS, rather it has to be switched to 12d1:1436, usb_modeswitch is doing this job, but somehow it is not working. The usb_modeswitch.conf is like this

```
#Configuration for the usb_modeswitch package, a mode switching tool for
#USB devices providing multiple states or modes

#Evaluated by the wrapper script /usr/sbin/usb_modeswitch_dispatcher

#To enable an option, set it to "1", "yes" or "true" (case doesn't matter)
#Everything else counts as "disable"


#Disable automatic mode switching globally (e.g. to access the original
#install storage)

DisableSwitching=0


#Enable logging (results in a extensive report file in /var/log, named
#"usb_modeswitch_<interface-name>" and probably others

EnableLogging=0

DefaultVendor= 0x12d1
DefaultProduct=0x1446

TargetVendor=  0x12d1
TargetProductList="1001,1406,140b,140c,1412,141b,1433,14ac"

CheckSuccess=20

MessageContent="55534243123456780000000000000011062000000100000000000000000000"
```

so doing this for firiing usb_modeswitch give this

pi@raspberrypi ~ $ sudo usb_modeswitch -c /etc/usb_modeswitch.conf

giving 

"No new devices in target mode or class found

Mode switch has failed. Bye."

So edited the /etc/usb_modeswitch.conf with this new conf content from Ubuntu forums [ubuntu] Huawei E173...have spent 3 days trying to connect to the net.html

################################################## ######
# Huawei E173

DefaultVendor= 0x12d1
DefaultProduct=0x1c0b

TargetVendor= 0x12d1
TargetProduct= 0x1c0b

CheckSuccess=5

MessageContent="5553424312345678000000000000001106 0000000000000000000000000000"

################################################## ###########

# Huawei E173s

;DefaultVendor= 0x12d1
;DefaultProduct= 0x1c0b

;TargetVendor= 0x12d1
;TargetProduct= 0x1c0b

;CheckSuccess=20

MessageEndpoint= 0x0f
MessageContent="5553424312345678000000000000001106 2000000100000000000000000000"
################################################## ##


sudo ./Adafruit_DHT 11 4