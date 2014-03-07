**Sending SMS in Beagle bone black**

It is an angstrom linux BBB, first connected to Ubuntu lap using usb wire from BBB, then a USB was connected to the powered USB hub, in which a serial USB connector and a Huwaei e 173 data (This was tested for Huwaei E303F also, it worked) card was connected.
* ssh's into it using ssh 192.168.7.2 -l root and password blank (a enter)
* Now lsusb showing 
Huwaei with modem and serial usb.
* Now the need of usb_modeswitch for Huwaei GSM, so need of usb_modeswitch in the Angstrom, downloaded ipk file (deb in angstrom) from

	http://feeds.angstrom-distribution.org/feeds/unstable/ipk/glibc/armv7a/base/usbmodeswitch_1.1.3-r0.5_armv7a.ipk

and transfered the file into BBB using the command from lap Ubuntu

	scp Downloads/usbmodeswitch_1.1.3-r0.5_armv7a.ipk root@192.168.7.2:~/Desktop/

* To install used
opkg install usbmodeswitch_1.1.3-r0.5_armv7a.ipk

* Edited usb_modeswitch.conf as
##################################
DefaultVendor= 0x12d1
DefaultProduct=0x1446

TargetVendor=  0x12d1
TargetProductList="1001,1406,140b,140c,1412,141b,1433,14ac"

CheckSuccess=20

MessageContent="55534243000000000000000000000011060000000000000000000000000000"
###################################
following
	http://www.draisberghof.de/usb_modeswitch/bb/viewtopic.php?p=4521
	https://bbs.archlinux.org/viewtopic.php?id=118746

* Then fired usb_modeswitch as
usb_modeswitch -I -W -c /etc/usb_modeswitch.conf

* it finally says good news of modem switch, based on 
	http://www.tabletroms.com/forums/adam-general-development/510-success-3g-usb-modems-now-work*-adam-35.html

* to send the SMS followed

https://groups.google.com/forum/#!msg/beagleboard/lW60u9wR-iA/ziuvODtCaZQJ

Made a sms.sh file copyed the contents follows

echo -e -n "AT+CMGF=1 \015" > /dev/ttyUSB1
echo -e -n "AT+CMGS=\"your mobile number\" \015" > /dev/ttyUSB1
echo -e -n "your text message \015" > /dev/ttyUSB1
echo -e -n "\032" > /dev/ttyUSB1
echo "******SMS was sent successfully!******"

run the file as sh sms.sh and immediately good news came SMS was sent successfully. dmesg| grep tty given the information to choose /dev/ttyUSB1
