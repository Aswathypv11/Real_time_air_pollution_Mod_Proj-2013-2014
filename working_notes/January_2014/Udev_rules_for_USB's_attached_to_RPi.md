**Udev_rules_for_USB's_attached_to_RPi**

it seems the /dev/tty* address for the attached USB is changing intermittently, giving a permanent rules name for each device will be the work around. 

Based on this 
http://hintshop.ludvig.co.nz/show/persistent-names-usb-serial-devices/

So the udev rules for cocemsd, setup is as follows

/etc/udev/rules.d, with file name 90-phone.rules, with this contents

KERNEL=="ttyUSB*", ATTRS{idVendor}=="12d1", ATTRS{idProduct}=="1436", NAME="phone", MODE="0666",SYMLINK+="phone"
KERNEL=="ttyUSB*", ATTRS{idVendor}=="067b", ATTRS{idProduct}=="2303", NAME="dylos", MODE="0666",SYMLINK+="dylos"
