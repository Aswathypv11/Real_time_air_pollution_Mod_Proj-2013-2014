**Server_stuck_at_GRUB_menu_after_12.04_update/upgrade**

Having this problem of Ubuntu server stuck at grub menu and not going inside automatically, button enter has to pressed to get inside and also into a blank useless screen with single hyphen with no activity to view or enter command. Workaround was by pressing ENTER after few minutes of server reboot, solved!. My problem was with Ubuntu server 12.04 LTS in IBM but started same as with a clean 
sudo apt-get upgrade
.
With a successive problem in ssh and open port (last cradle of hope to run this server), I given attention to solve the problem. This is how I solved.
One of the option to resolve grub struck problem is edit the grub2 options in file /etc/default/grub, to my surprise in the server there is no such file. 
So I re installed grub in the server using the command
sudo apt-get update; sudo apt-get install --reinstall grub
Based on: http://askubuntu.com/questions/41866...mand-not-found
While doing this I got error of this kind in update 
Err http://ppa.launchpad.net precise Release.gpg Something wicked happened resolving 'ppa.launchpad.net:http' (-5 - No address associated with hostname)
Though this error was not killing the installation processes, I resolved this error by changing the name server based on http://askubuntu.com/questions/11159...-mirror-errors.
and done a sudo apt-get update, without any such this error. After reboot there is NO hanging at grub 