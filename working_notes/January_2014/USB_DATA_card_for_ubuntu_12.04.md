**USB_DATA_card_for_ubuntu_12.04**

* Do
dmesg |grep tty

* if not showing any thing, solved follwoing final answer of this question 

http://ubuntuforums.org/archive/index.php/t-1853306.html

* "dmesg is a ring buffer, so if there are a lot of messages being logged you will lose the initial boot messages. Try this instead:

cd /var/log ; grep ttyUSB dmesg messages *log | more"

* now showing 

fellow@dhcppc3:~$ cd /var/log ; grep ttyUSB dmesg messages *log | more
grep: messagesdmesg:[   23.391523] usb 1-1.1: GSM modem (1-port) converter now attached to ttyUSB0
: No such file or directory
dmesg:[   23.391604] usb 1-1.1: GSM modem (1-port) converter now attached to ttyUSB1
dmesg:[   23.391645] usb 1-1.1: GSM modem (1-port) converter now attached to ttyUSB2