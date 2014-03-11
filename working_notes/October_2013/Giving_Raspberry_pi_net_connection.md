 **Giving_Raspberry_pi_net_connection**

The static IP address addition on SD card seems not connecting RPi (Raspberry Pi) to Internet (1)

1. Possible way is DHCP was removed and static is invoked
2. So the the command netstat -nr will show up only the

Destination     Gateway         Genmask         Flags   MSS 
192.168.1.0     0.0.0.0         255.255.255.0   U         0
Window  irtt   Iface
 0          0        eth0

without UG flag (from http://raspberrypi.stackexchange.com/questions/7146/static-local-ip-gateway-config-on-startup-issues)

so no gateway, no way to access Internet

3. Solution is to add following entries

pi@raspberrypi ~ $ cat /etc/network/interfaces
auto lo

iface lo inet loopback
iface eth0 inet static
address 192.168.1.104
netmask 255.255.255.0
gateway 192.168.1.1


allow-hotplug wlan0
iface wlan0 inet manual
wpa-roam /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp

and

pi@raspberrypi ~ $ cat /etc/resolv.conf
DNS 218.248.240.179
nameserver 218.248.240.179

and

sudo /sbin/route add -net 0.0.0.0 gw 192.168.1.254 eth0
sudo /sbin/route add -net 0.0.0.0 gw 192.168.1.1 eth0

4. it makes three line in netstat table with these gatway address, after this the Internet will be getting.

now the  netstat -nr will looks like


pi@raspberrypi ~ $ netstat -nr
Kernel IP routing table
Destination     Gateway         Genmask         Flags   MSS Window  irtt Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG        0 0          0 eth0
0.0.0.0         192.168.1.254   0.0.0.0         UG        0 0          0 eth0
192.168.1.0     0.0.0.0         255.255.255.0   U         0 0          0 eth0


References:
1. http://raspberrypi.stackexchange.com/questions/7624/setting-a-static-eth0-ip
2. http://raspberrypi.stackexchange.com/questions/7146/static-local-ip-gateway-config-on-startup-issues
3. http://www.soslug.org/wiki/getting_your_raspberry_pi_to_run_on_a_static_ip_with_internet
4. http://www.penguintutor.com/linux/raspberrypi-webserver
5. http://pihw.wordpress.com/guides/direct-network-connection/
6. http://www.penguintutor.com/linux/raspberrypi-headless