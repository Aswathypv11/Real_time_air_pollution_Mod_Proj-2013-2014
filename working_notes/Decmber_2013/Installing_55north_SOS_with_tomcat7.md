**Installing_55north_SOS_with_tomcat7**
* Installed tomcat 7 using 
	http://askubuntu.com/questions/339169/how-to-install tomcat-7-0-42-on-ubuntu-12-04-3-lts
* to find is tomcat is really running
followed by
	http://stackoverflow.com/questions/3944157/is-tomcat-running
netstat -a | grep 8080
ps -ef | grep tomcat  
both command gives some bulge result and responses if it is working.
* if it is not working the command used to start tomcat7 is from installation page
	sudo $CATALINA_HOME/bin/startup.sh
* Installing the SOS war following tomcat manager and war file upload
* to upload the data into istsos used this command following all its installation documentation.
	python cmdimportcsv.py -s cocemsd -u http://192.168.1.100/istsos -p cocemsd_lbm_1 -w /home/fellow/D_GISE/dyloscbe -v