**How_to_BRICK_Beagle_Bone_Black**

apt-get update and upgrade make BBB's internal hard disk to crash, to solve this is to make a recovery SD card and rewrite the hard disk

* After long searching for making the SD card
finally followed this 
	http://www.armhf.com/index.php/getting-started-with-ubuntu-img-file/
* Installed the xz in ubuntu lap
	apt-get install xz-utils
* then viewed the attached sd card device name by
ls /dev/sd*
given it as sdb
* so run the xz, followed this
http://downloads.angstrom-distribution.org/demo/beaglebone/
```
xz -dkc Angstrom-Cloud9-IDE-GNOME-eglibc-ipk-v2012.12-beaglebone-2013.09.05.img.xz > /dev/sdb
```

* after some time exit the xz
then inserted the sd card and booted the beagle on from sd card now following this 

http://hipstercircuits.com/unbrick-beaglebone-black-without-erasing-emmc/

ssh root@192.168.7.2
gives a problem of denial

* followed this
http://stackoverflow.com/questions/19494619/how-to-interact-with-two-beaglebone-black-connected-to-one-computer made a finale 
.ssh/config
with this content
Host 192.168.7.* UserKnownHostsFile /dev/null StrictHostKeyChecking no
now ssh is working and followed again this
http://hipstercircuits.com/unbrick-beaglebone-black-without-erasing-emmc/

* to mount the internal hard disk with SD card running BBB

mkdir /mnt/microSD mount /dev/mmcblk0p2 /mnt/microSD
cp -r /mnt/microSD/lib/modules/3.8.13-00611-gd1fc8a7-dirty/ /media/Angstrom/lib/modules/
shutdown now
but in vein, so now plan is to copy all the files in / and copy it in mms that is inside angstrom folder and reboot it without the sd card, that also didn't turned up to correct the problem.

Reference to solve bricking
```
https://pixhawk.ethz.ch/tutorials/omap/boot_from_sd_sdhc http://eavise.wikispaces.com/Angstrom+installation 
http://www.angstrom-distribution.org/demo/beagleboard/ http://www.angstrom-distribution.org/demo/beagleboard/ http://elinux.org/BeagleBoardBeginners 
http://www.reuk.co.uk/wordpress/bricking-a-beaglebone-black/ 
http://downloads.angstrom-distribution.org/demo/beaglebone/ 
http://downloads.angstrom-distribution.org/demo/beaglebone/ 
http://hipstercircuits.com/unbrick-beaglebone-black-without-erasing-emmc/ 
http://elinux.org/BeagleBoardRecovery