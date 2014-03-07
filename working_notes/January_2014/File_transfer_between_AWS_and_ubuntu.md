**File_transfer_between_AWS_and_ubuntu**

* Use scp 

```
sudo scp -i .ssh/gssa.pem ubuntu@ip.ap-southeast-1.compute.amazonaws.com:/home/ubuntu/CORE-Ubuntu_eWRF.zip /home/fellow
```
* Use rsync, to transfer file from local host to aws
```
sudo rsync -avz –stats /home/fellow/sim.txt -e “ssh -i .ssh/gssa.pem” ubuntu@ip.ap-southeast-1.compute.amazonaws.com:/home/ubuntu/
sudo rsync -P –stats -e “ssh -i .ssh/gssa.pem” ubuntu@ip.ap-southeast-1.compute.amazonaws.com:/home/ubuntu/CORE-Ubuntu_eWRF.zip /home/fellow/
```
to transfer file from aws to local host

```
sudo rsync -avz –stats -e “ssh -i .ssh/gssa.pem” ubuntu@ecip.ap-southeast-1.compute.amazonaws.com:/home/ubuntu/sim.txt /home/fellow/
```
to resume a download after a net connection break

```
sudo rsync -P –stats -e “ssh -i .ssh/gssa.pem” ubuntu@ip.ap-southeast-1.compute.amazonaws.com:/home/ubuntu/sim.txt /home/fellow/
```

rsync is most useful for backup purpose to transfer or update file between, external hard disk and laptop
Based on
http://x-ian.net/2009/05/15/resume-rsync-transfer-after-ssh-connection-crash/
