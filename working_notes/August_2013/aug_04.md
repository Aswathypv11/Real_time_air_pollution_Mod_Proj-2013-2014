 **Installing maven in Ubuntu 12.04**

Based on links
http://docs.geotools.org/latest/userguide/build/install/mvn.html http://www.mkyong.com/maven/how-to-install-maven-in-ubuntu/ http://lukieb.wordpress.com/2011/02/15/installing-maven-3-on-ubuntu-10-04-lts-server/

Download, untar and copy maven in /usr/local/

wget http://archive.apache.org/dist/maven/binaries/apache-maven-3.0.4-bin.tar.gz
tar -zxf apache-maven-3.0.4-bin.tar.gz
sudo cp -R apache-maven-3.0.4 /usr/local 


then link with bin folder

sudo ln -s /usr/local/apache-maven-3.0.4/bin/mvn /usr/bin/mvn 


Then add java home link in the .bashrc
sudo nano .bashrc 
---JAVA_HOME=/usr/lib/jvm/java-1.7.0-openjdk-amd64 Thats it maven is installed Test it

mvn –version

Seems every think ok but there will be issue while mvn install, error of
javac": java.io.IOException: error=2, No such file or directory javac not found

type
javac – version in terminal it will say

 

javac --version 

The program 'javac' can be found in the following packages:
 * default-jdk
 * ecj
 * gcj-4.6-jdk
 * openjdk-6-jdk
 * gcj-4.5-jdk
 * openjdk-7-jdk


So do sudo apt-get install default-jdk
the error goes away 