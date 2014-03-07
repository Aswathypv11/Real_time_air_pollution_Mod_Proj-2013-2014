**Python_for_fetching_Mysql_table**

This is for converting the mysql backed sms gateway data into sos import formate. COCEMS_lbm are sending the data every 15 minutes through SMS and it is received by server side data card and gammu SMS gateway backed by mysql, the data is in inbox table. Following python script do the job, long time was consumed in understanding the array, list objects in python, clear understanding would n't cost much time consumption. 
After long frustration this I found in to takle the problem of addressing the numpy array out of mysql fetch.
following,

```
http://stackoverflow.com/questions/7061824/whats-the-most-efficient-way-to-covert-mysql-output-into-a-numpy-array-in-python
based on
http://zetcode.com/db/mysqlpython/
```

The code is 

```
import MySQLdb as mdb
import csv
from datetime import datetime
import itertools
import collections
#Here goes connection with mysql data base and fecting the table.
con = mdb.connect (host = "localhost", user = "YOURPASSWORD", passwd = "YOURPASSWORD", db = "kalkun")
with con:
    cur = con.cursor(mdb.cursors.DictCursor)
    cur.execute('SELECT DISTINCT TextDecoded FROM `inbox` WHERE SenderNumber = "MOBILENUMBER" ORDER BY TextDecoded DESC LIMIT 1')
#Here fetching all data from single data column into row variable and then ooped inside the content to clean the data with unwanted charecters attahced in the SMS and serial read from sensor 
    rows = cur.fetchall()
    a = []
    for row in rows:
        row1 = row["TextDecoded"].rstrip('\n\r')
        a.append(row1)
#Here making a DAT file formate for inserting data into istSOS 
outfile_path='cocemsd_lbm_1.DAT'
writer = csv.writer(open(outfile_path, 'w'))
headers = ['urn:ogc:def:parameter:x-istsos:1.0:time:iso8601','urn:ogc:def:parameter:x-istsos:1.0:cocemsd:nptm','urn:ogc:def:parameter:x-istsos:1.0:cocemsd:npfm']
writer.writerow(headers)
#Here making another loop to convert the array into list and editing the date formate to suite with istSOS formate
b =[]
for line in a:
    col = line.strip().split(',')
    date = datetime.strptime (col[0], "%Y-%m-%dT%H:%M").strftime("%Y-%m-%dT%H:%M:%S.000000+0530")
    data = date+','+col[1]+','+col[2]
    b.append(data)
print b
#Here making another and final loop to convert a single row data into multiple rows for dat formate.
writer.writerows([x.split(',') for x in b])
```

