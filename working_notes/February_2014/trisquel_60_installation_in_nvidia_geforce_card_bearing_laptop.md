**trisquel 6.0 installation in nvidia geforce card bearing laptop**

There are problems in installing trisquel 6.0 in HCL ME laptop having Nvidia geforce graphic card. 
I used live usb created from Ubuntu 12.04 using start up disk creator, the installation screen never turned up. It shows a blank screen with a large cursor object then get into trisquel popular background image and stay there forever with hopeful rotating mouse pointer for some time time and then into a hopeless state, this is the first problem.

* Problem 1
solution:
While blank screen with large cursor shows up after BIOS setup, press F1 (you have to fast enough here if you loose this screen you have to restart the system), it brings a screen with some numerics, then press ESC you will be get into screen with boot : _ . Type here "help" (with out " ") and press Enter, you will be welcomed with help screen with several options and its functions. Type here
F3 (Here also you have to fast enough, other wise it goes to the later screen stays forever and pretend you to restart the system) and type "install nomodeset" 
It will be prompted to  the normal installation screen of trisquel and can continue with the normal installation.

* Problem 2
After installation and one time reboot, the system hangs into the background image and stays forever.
Solution:
Here you need to specify the nomodeset in grub, to get grub screen of trisquel, keep on press shift key after blue bios screen, stop pressing only after the GRUB screen of trisquel shows up. To edit grub option you will be prompted with user name and password of GRUB, note that those are not the password or user name setup you done during installation. You can know about user name and password by going inside just installed trisquel. Moreover the password is random generated and so only way is to get into the file system of trisquel located in  /etc/grub.d/01_PASSWORD and view it in text editor to know about user name and password (so the question how go inside the system and view a file even if it is not gets started arise, solution- use live usb, I used a another Ubuntu live USB and follow the above step up to the installation screen and get into testing mode with out installation then mount the hard disk and view the file from there.). After knowing password, restart the system with out live USB enter into grub screen and type the user name and password just noted. You will be get into the grub option screen, press e or d as specified, a new screen comes up and  edit content in there, remove "quit splash" into "nomodeset" (here again no " "). After editing press CTRL+X and you can get into your installed trisquel, cheer up. So to make permanently nomodeset for grub for avoiding the black screen problem, edit the grub file from /etc/default/grub and edit a line,
GRUB_CMDLINE_LINUX="nomodeset", save the file and you are done now you can restart the system to know every think works fine.