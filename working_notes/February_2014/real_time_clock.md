## Real time clock(RTC) on Raspberry pi

Raspberry pi is an ultra-low cost computer, so real time clock(RTC) is not included in Rpi to keep costs low and size small.But RTC with low cost battery can be added to rpi to keep time. RTC circuit consists of Adafruit DS1307 RTC Breakout Board Kit and pi cobbler.Four connections between rtc and pi cobbler are,

	*connect vcc to the 5V pin of pi
	*connect GND to the GND pin of pi
	*connect SDA to the SDA0 pin of pi
	*connect SCL to the SCL0 pin of pi

I2C interface pins that allows to connect hardware modules with just two control pins. The pins SDA and SCL are used for i2c. Initially i2c is need to be setup on pi using these commands:

	sudo nano /etc/modules

and add these two lines at the bottom of file,

	i2c-bcm2708
	i2c-dev

To verify the wiring of RTC, run this command 
  
          i2cdetect -y 1
          
Output will be in the format, 
  
       		 0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
	00:          -- -- -- -- -- -- -- -- -- -- -- -- -- 
	10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
	60: -- -- -- -- -- -- -- -- UU -- -- -- -- -- -- -- 
	70: -- -- -- -- -- -- -- --        

once have the kernel driver driving ,i2cdetect will skip over 0*68 and disply UU instead, this means its working!!!!!
 
Reference links [https://learn.adafruit.com/downloads/pdf/adding-a-real-time-clock-to-raspberry-pi.pdf],[

 
