 **Store json data into Mysql using python**
Web services APIs such as weather underground data provided in json format is stored in Mysql table using this python script.

It is based on stack overflow answers
http://stackoverflow.com/questions/1640715/get-json-data-via-url-and-use-in-python-simplejson
 http://stackoverflow.com/questions/5687718/python-mysql-insert-data

import urllib2
import json
import MySQLdb


req = urllib2.Request("http://api.wunderground.com/api/YOUR API key/conditions/q/country/town.json")
opener = urllib2.build_opener()
f = opener.open(req)
data = json.load(f)
print data['current_observation']['observation_location']['city'],data['current_observation']['observation_time_rfc822']

conn = MySQLdb.connect(host= "localhost",
                  user="YOUR username",
                  passwd="YOUR password",
                  db="database")
x = conn.cursor()

try:
   x.execute(
   "INSERT INTO CBE_meterology (Station, DateAP)" 
   "VALUES (%s,%s)",(data['current_observation']['observation_location']['city'],data['current_observation']['observation_time_rfc822']))
   conn.commit()
except:
   conn.rollback()

conn.close()


the script collect json from url and then convert into python object and feed into mysql table using sql command.