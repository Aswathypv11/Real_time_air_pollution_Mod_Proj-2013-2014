#!/usr/bin/python
import serial
import time
import sqlite3 as lite
import logging
#import csv

logger = logging.getLogger('lbm1')
hdlr = logging.FileHandler('/home/pi/lbm1_status/status.log')
formatter = logging.Formatter('%(asctime)s: %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
logger.info("cronjob started")

#csv_path='/home/pi/lbm1/obj0/data.csv'
#writer = csv.writer(open(outfile_path, 'a'))
#headers = ['urn:ogc:def:parameter:x-istsos:1.0:time:iso8601','urn:ogc:def:parameter:x-istsos:1.0:cbe:dylos:np05mg','urn:ogc:def:parameter:x-istsos:1.0:cbe:dylos:np25mg']
#writer.writerow(headers)
csv_file= open('/home/pi/lbm1/obj0/data.csv','a')
ser = serial.Serial('/dev/dylos', 9600, timeout=60)
try:
   with ser:
       	time.sleep(60)
       	line = ser.readline()
	now = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
        a =  "%s,%s" % (now,line)
        #print a
        b = a.strip(' \00/r/n')
        #print b
        #headers = ['urn:ogc:def:parameter:x-istsos:1.0:time:iso8601','urn:ogc:def:parameter:x-istsos:1.0:cbe:dylos:np05mg','urn:ogc:def:parameter:x-istsos:1.0:cbe:dylos:np25mg']
        #csv_file.write(headers)
        csv_file.write(b)
        csv_file.flush()
        csv_file.close()
       
except:
        logger.exception('serial not ready')
finally:
    if ser:
       ser.close()

#csv_file= open('/home/pi/lbm1/obj0/data.csv','a')
	#headers = ['urn:ogc:def:parameter:x-istsos:1.0:time:iso8601','urn:ogc:def:parameter:x-istsos:1.0:cbe:dylos:np05mg','urn:ogc:def:parameter:x-ist$
        #csv_path.write(headers)
#now = time.strftime("%Y-%m-%dT%H:%M", time.localtime())
#a =  "%s,%s" % (now,line)
#print a
#b = a.strip(' \00/r/n')
#print b
#csv_file.write(b)
#csv_file.flush()
#csv_file.close()

logger.info("CSV file now written")

con = lite.connect('/home/pi/lbm1_status/dylos.db')
try:
   with con:
       cur = con.cursor()
       cur.execute("INSERT INTO data(data) VALUES(?)", (b,))
       logger.info("data saved in db")
except:
        logger.exception('database yet to ready')
finally:
    if con:
       con.close() 
logger.info("cronjob over")
