## Temp.& Humidity sensor  

Temperature and humidity sensor can be logged from Raspberry pi. DHT11 is a basic low cost humidity and temp.sensor.It has capacitive humidity and thermistor to measure temp. and humidity from the surroundings. Wiring of this sensor consists of DHT11,10K ohm resistor and pi cobbler. Python and C code is used to talk with this sensor, code is available at [https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/software-install-updated]. Download code and install the dependencies using this instructions :

	sudo apt-get upgrade
	sudo apt-get install build-essential python-dev

Install python libraries by executing this command,

	sudo python setup.py install

Data pin of sensor is connected to GPIO(General Purpose Input and Output) pin 4 of pi cobbler. Run below command to get temp. and humidity of particular area. 

      cd Adafruit-Raspberry-Pi-Python-Code-master/Adafruit_DHT_Driver 
      run  sudo ./Adafruit_DHT 11 4

"11" indicates the name of sensor DHT11, and "4" indicates the GPIO pin number 4.    
output will be in the form :

      Using pin #4
      Data (40): 0x3a 0x0 0x1f 0x0 0x59
      Temp = 31 *C, Hum = 58 %
