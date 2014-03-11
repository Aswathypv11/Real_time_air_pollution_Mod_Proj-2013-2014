**Script_for_json_to_csv_for_weather_underground_API_fetching_historical_data**

1. based on this
https://github.com/PythonJournos/LearningPython/blob/master/tutorials/convert_json_to_csv.py
a sample script

```
import urllib2
import json
import csv
outfile_path='history.csv'
writer = csv.writer(open(outfile_path, 'w'))
headers = ['date']
writer.writerow(headers)
req = urllib2.Request("http://api.wunderground.com/api/YOUR_KEY/history_20131001/q/India/Coimbatore.json")
opener = urllib2.build_opener()
f = opener.open(req)
data = json.load(f)
for history in data['history']['observations']:
       row = []
       row.append(str(history['date']['pretty']))
       row.append(str(history['tempm']))
       writer.writerow(row)
```

2. Now the url has to be itrated to give a range of historical data required and most important the date range has to set.
The date range is based on answer http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python

a sample script
```
from datetime import date
from dateutil.rrule import rrule, DAILY

a = date(2009, 5, 30)
b = date(2009, 6, 9)

for dt in rrule(DAILY, dtstart=a, until=b):
    print dt.strftime("%Y-%m-%d")
```

The url itration based on this answer
http://stackoverflow.com/questions/16632569/for-loops-in-python-to-read-long-url-from-shortened-url
a sample code
```
import urllib2
from BeautifulSoup import BeautifulSoup

for x in ('20131011','20131012'):
  shortURL = 'http://api.wunderground.com/api/4d09b615cbc7726e/history_'+str(x)+'/q/India/Coimbatore.json'
  output = urllib2.urlopen(shortURL)

  print output.url


3. now the problem is how to take the for loop date range into the url for looping, long searched for making a list from the print
    dt.strftime(“%Y-%m-%d”)

finally got write by empty array . append, hoooorahe! http://learnpythonthehardway.org/book/ex32.html
the sample code become

```
import urllib2 from datetime
import date from dateutil.rrule
import rrule, DAILY
a = date(2009, 6, 3)
b = date(2009, 6, 9)
dtm = []
for
dt in rrule(DAILY, dtstart=a, until=b): print dt.strftime(“%Y%m%d”)
dtm.append(dt.strftime(“%Y%m%d”))
print dtm
for x in (dtm): shortURL = ‘http://api.wunderground.com/api/YOURKEY/history_’+str(x)+‘/q/India/Coimbatore.json’ output = urllib2.urlopen(shortURL)
print output.url ``` the out put looks
20090603 20090604 ——— 20090609 [‘20090603’, ‘20090604’, ‘20090605’, ‘20090606’, ‘20090607’, ‘20090608’, ‘20090609’] http://api.wunderground.com/api/YOURKEY/history_20090603/q/India/Coimbatore.json —————- http://api.wunderground.com/api/YOURKEY/history_20090609/q/India/Coimbatore.json
```

now the challenge is how to intgrate above code with csv write code.
The solution is another for loop for urllib
the final code is
```
import urllib2
import json
import csv
from datetime import date
from dateutil.rrule import rrule, DAILY

outfile_path='history.csv'
writer = csv.writer(open(outfile_path, 'w'))
headers = ['TimeIST','TemperatureC','Dew PointC','Humidity','Wind SpeedKm/h','Gust SpeedKm/h','Wind DirectionDe','Wind Direction','VisibilityKm','Sea Level PressurehPa','Events','Heatindex','Precipitationmm','Conditions']
writer.writerow(headers)


a = date(2013, 8, 1)
b = date(2013, 8, 2)

dtm = []
for dt in rrule(DAILY, dtstart=a, until=b):
    dtm.append(dt.strftime("%Y%m%d"))

for x in (dtm):
    url = 'http://api.wunderground.com/api/4d09b615cbc7726e/history_'+str(x)+'/q/India/Coimbatore.json'
    req = urllib2.Request(url)
    opener = urllib2.build_opener()
    f = opener.open(req)
    data = json.load(f)
for history in data['history']['observations']:
       row = []
       datewu = history['date']['year']+'-'+history['date']['mon']+'-'+history['date']['mday']+'T'+history['date']['hour']+':'+history['date']['min']+':00.000000+0530'    
       row.append(str(datewu))
       row.append(str(history['tempm']))
       row.append(str(history['dewptm']))
       row.append(str(history['hum']))
       row.append(str(history['wspdm']))
       row.append(str(history['wgustm']))
       row.append(str(history['wdird']))
       row.append(str(history['wdire']))
       row.append(str(history['vism']))
       row.append(str(history['pressurem']))
       row.append(str(history['windchillm']))
       row.append(str(history['heatindexm']))
       row.append(str(history['precipm']))
       row.append(str(history['conds']))
       writer.writerow(row)
```

The aboe code doen’t done the job, it only taking the last date from the date range, the code has to change.
the final working code

```
import urllib2
import json
import csv from datetime
import date from dateutil.rrule
import rrule, DAILY
outfile_path=‘history1.csv’
writer = csv.writer(open(outfile_path, ‘w’))
headers = [‘TimeIST’,‘TemperatureC’,‘Dew PointC’,‘Humidity’,‘Wind SpeedKm/h’,‘Gust SpeedKm/h’,‘Wind DirectionDe’,‘Wind Direction’,‘VisibilityKm’,‘Sea Level PressurehPa’,‘Events’,‘Heatindex’,‘Precipitationmm’,‘Conditions’] writer.writerow(headers)
a = date(2013, 8, 5) b = date(2013, 8, 10)
dtm = [] for dt in rrule(DAILY, dtstart=a, until=b): # print dt.strftime(“%Y%m%d”) dtm.append(dt.strftime(“%Y%m%d”))
dtl = [] for x in (dtm):
shortURL = ‘http://api.wunderground.com/api/4d09b615cbc7726e/history_’+str(x)+‘/q/India/Coimbatore.json’ output = urllib2.urlopen(shortURL) # print output.url dtl.append(output.url)
print dtl
dtd = [] for url in (dtl): req = urllib2.Request(url)
opener = urllib2.build_opener()
f = opener.open(req) data = json.load(f) # print data dtd.append(data)
for d in (dtd): for history in d[‘history’][‘observations’]: if d != history: row = [] datewu = history[‘date’][‘year’]+’-‘+history[’date’][‘mon’]+’-‘+history[’date’][‘mday’]+‘T’+history[‘date’][‘hour’]+’:‘+history[’date’][‘min’]+’:00.000000+0530’
row.append(str(datewu)) row.append(str(history[‘tempm’])) row.append(str(history[‘dewptm’])) row.append(str(history[‘hum’])) row.append(str(history[‘wspdm’])) row.append(str(history[‘wgustm’])) row.append(str(history[‘wdird’])) row.append(str(history[‘wdire’])) row.append(str(history[‘vism’])) row.append(str(history[‘pressurem’])) row.append(str(history[‘windchillm’])) row.append(str(history[‘heatindexm’])) row.append(str(history[‘precipm’])) row.append(str(history[‘conds’])) writer.writerow(row)
print data
```

Create a csv from Json for WU current observations
the non working code for past 5 hours

```
import urllib2
import json
import csv
from datetime import date
#from dateutil.rrule import rrule, DAILY

outfile_path='CART.DAT'
writer = csv.writer(open(outfile_path, 'w'))
headers = ['urn:ogc:def:parameter:x-istsos:1.0:time:iso8601','urn:ogc:def:parameter:x-istsos:1.0:cbe:aws:dewpont','urn:ogc:def:parameter:x-ists$
writer.writerow(headers)


req = urllib2.Request("http://api.wunderground.com/api/4d09b615cbc7726e/conditions/q/India/Coimbatore.json")
opener = urllib2.build_opener()
f = opener.open(req)
data = json.load(f)


for current_observation in data['current_observation']:
     print ['station_id']
```
one working code for converting json into csv

```
import csv
import json

x="""[ 
    { "pk": 22, "model": "auth.permission", "fields": 
        { "codename": "add_logentry", "name": "Can add log entry", "content_type": 8 } 
    }, 
    { "pk": 23, "model": "auth.permission", "fields": 
        { "codename": "change_logentry", "name": "Can change log entry", "content_type": 8 } 
    },
    { "pk": 24, "model": "auth.permission", "fields": 
        { "codename": "delete_logentry", "name": "Can delete log entry", "content_type": 8 } 
    }
]"""

x = json.loads(x)

f = csv.writer(open("test.csv", "wb+"))

# Write CSV Header, If you dont need that, remove this line
f.writerow(["pk", "model", "codename", "name", "content_type"])

for x in x:
    f.writerow([x["pk"], 
                x["model"], 
                x["fields"]["codename"], 
                x["fields"]["name"],
                x["fields"]["content_type"]])
```

always getting TypeError: string indices must be integers
hrrr
finally got working code based on experience that, with current json file of single row, it is unnecessary and erroneous to call ‘for loop’, (took 5 hours to realize) and as per this answer http://stackoverflow.com/questions/14784334/python-csv-error-sequence-expected
so the working code is as follows
``` import csv import json import urllib2 from datetime import date outfile_path=‘CART.DAT’ writer = csv.writer(open(outfile_path, ‘w’)) headers = [‘urn:ogc:def:parameter:x-istsos:1.0:time:iso8601’,‘urn:ogc:def:parameter:x-istsos:1.0:cbe:aws:dewpont’] writer.writerow(headers) req = urllib2.Request(“http://api.wunderground.com/api/4d09b615cbc7726e/conditions/q/India/Coimbatore.json”) opener = urllib2.build_opener() f = opener.open(req) data = json.load(f) #for data in data: rows = [data[“current_observation”][“temp_c”]] writer.writerow(rows)
``` Now having problem in converting the date time formate of wu date formate to istsos’s. followed this for converting last answer, http://stackoverflow.com/questions/13350909/convert-other-time-values-to-datetime-format-in-python
but that answer has a mistake, in specifying the shortened version of month, it should be %b not %m as specified in the answer.
this is from http://www.lightbird.net/py-by-example/datetime.date-module.html
so the final code for converting the date and making a csv.DAT is this

```
import csv
import json
import urllib2
from datetime import datetime


outfile_path='CART.DAT'
writer = csv.writer(open(outfile_path, 'w'))
headers = ['urn:ogc:def:parameter:x-istsos:1.0:time:iso8601','urn:ogc:def:parameter:x-istsos:1.0:cbe:aws:dewpont']
writer.writerow(headers)

req = urllib2.Request("http://api.wunderground.com/api/4d09b615cbc7726e/conditions/q/India/Coimbatore.json")
opener = urllib2.build_opener()
f = opener.open(req)
data = json.load(f)



#for data in data:
dateNF = data['current_observation']['observation_time_rfc822'].strip( '+0530' );
print dateNF
dateITS = datetime.strptime (dateNF, "%a, %d %b %Y %H:%M:%S ").strftime("%Y-%m-%dT%H:%M:%S.000000+0530")
print dateITS
rows = [dateITS,data["current_observation"]["temp_c"]]
writer.writerow(rows)
```