 **Xvfb – the X Virtual FrameBuffer error for Ubuntu server 12.04**
Frame buffer is the hardware portion in memory to provide display. X window systems are the the basic display setup for computers, remember in computer every display is organized as bitmap windows. In head less Ubuntu servers virtual framebuffers are used for the application which specifically requires the display such as Firefox or other browsers.
Xvfb is provides virtual display for those application. In Ubuntu headless server (server without any GUI) I installed for mainly running Selenium scripts which requires browser to run and browser requires display. It is installed in Ubuntu 12.04 following this
http://www.installationpage.com/selenium/how-to-run-selenium-headless-firefox-in-ubuntu/
and followed the commands


sudo apt-get install xvfb

sudo Xvfb :10 -ac
firefox
export DISPLAY=:10

But somehow after a reboot, it shows error

[dix] Could not init font path element /usr/share/fonts/X11/misc, removing from

list!
Could not init font path element /usr/share/fonts/X11/cyrillic, removing from

[dix]
 list!
[dix] Could not init font path element /usr/share/fonts/X11/100dpi/:unscaled,
/:unscaled, removin

removing from list!
[dix] Could not init font path element /usr/share/fonts/X11/75dp
ig from list!
[dix] Could not init font path element /usr/share/fonts/X11/Type1, removing
from list!
ot init font path element /usr/share/fonts/X11/75dpi, removing from list!

[dix] Could not init font path element /usr/share/fonts/X11/100dpi, removing
from list!
[dix] Could 

I thought it is not working but after waiting for sometime it seems actually starting the display, any how I move forward to the error and installed following package to resolve the error based on

http://blog.martin-lyness.com/tag/xvfb


sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic

sudo apt-get install xserver-xorg-core

and followed this for final touch up
http://www.guguncube.com/2733/python-spynner-installation-in-ubuntu
and installed


sudo apt-get install -y x11-xkb-utils

sudo apt-get install -y xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic

sudo apt-get install -y x-ttcidfont-conf cabextract ttf-mscorefonts-installer

sudo dpkg-reconfigure --default-priority x-ttcidfont-conf

then in a different terminal ssh’d to run the display and then the Firefox, now it working nice, other wise it gets lot of error.
like  RAND is not working etc.
Another tips:
to show the hidden file by cmd, use

ls -a

References
http://stackoverflow.com/questions/17944234/xlib-extension-randr-missing-on-display-21-trying-to-run-headless-googl
http://askubuntu.com/questions/131051/how-to-kill-and-to-start-the-x-server
http://permalink.gmane.org/gmane.comp.multimedia.puredata.general/88691
http://www.guguncube.com/2733/python-spynner-installation-in-ubuntu
http://veeraramkumar.blogspot.in/2011_06_01_archive.html
https://github.com/daneroo/phantom-test
http://serverfault.com/questions/239597/xvfb-error-on-ubuntu
http://ubuntuforums.org/archive/index.php/t-1956577.html
http://ivanvillareal.com/linux/xvfb-and-firefox-headles-screenshot-generator/
http://blog.martin-lyness.com/tag/xvfb
http://www.installationpage.com/selenium/how-to-run-selenium-headless-firefox-in-ubuntu/
