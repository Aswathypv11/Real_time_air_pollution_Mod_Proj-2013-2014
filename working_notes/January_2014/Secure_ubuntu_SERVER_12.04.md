**Secure_ubuntu_SERVER_12.04**

* For key pair login and removing the password based on 

	http://ubuntuforums.org/archive/index.php/t-30709.html http://blog.nas-admin.org/?p=63
	http://www.thefanclub.co.za/how-to/how-install-psad-intrusion-detection-ubuntu-1204-lts-server following first one
* cd .ssh/ 
* ssh-keygen -t dsa 
* scp id_dsa.pub serverusername@IP:./id_dsa.pub 
* ssh into server 
* cd .ssh 
* touch authorized_keys2
* chmod 600 authorized_keys2 
* cat ../id_dsa.pub >> authorized_keys2 
* rm ../id_dsa.pub
* edited the /etc/ssh/sshd_config
for #PasswordAuthentication yes >>> PasswordAuthentication no PermitRootLogin yes >>> PermitRootLogin no >>> DebianBanner no 
* have to restart the ssh
sudo /etc/init.d/ssh restart now with out key file the permission will be denied
* following this steps for security 
http://www.thefanclub.co.za/how-to/how-secure-ubuntu-1204-lts-server-part-1-basics
    Firewall - UFW sudo apt-get install ufw sudo ufw allow ssh sudo ufw allow http sudo ufw enable sudo ufw status verbose
* to make into static ip address following 
http://lani78.wordpress.com/2012/07/19/change-to-static-ip-on-the-ubuntu-precise-pangolin-server/ 
for a error I made a changing of ip address of public what ISP provider has given, it is wrong, given the current situation of sever display problem it was a disastrous discretion. by doing this the ssh access only the final method to access the server is disrupted, it was rectified by running the live Ubuntu server cd and accessed the hard drive from that using a given shell script.

Instead of this erroneous ip address specifying the port forwarding under the router has to be done to make the server truly Internet accessible. for this the NAT option in router selected inside that there virtual server has to be access in which the port forwarding option has to mention the static ip address of the server computer which is given has to mention for web server by 80 and ssh by 22 port.
based on this
http://askubuntu.com/questions/299572/making-websites-visible-to-outside-networks-with-ubuntu-server-12-04