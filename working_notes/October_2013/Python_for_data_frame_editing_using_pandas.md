 **Python_for_data_frame_editing_using_pandas**

Pandas is a library for data frame manipulation and analysis, it gives ability to python as R like functionality.
This is for converting a CSV file into the form to import into istsos as a tutorial sensor observations.
The steps need to be done is

 1. remove the unwanted column in csv file
 2.  filter each stations readings
 3. remove duplicates
 4.convert the date and time formate into ISO standards as demo data

to read csv
import pandas 
df = read_csv('the path/CBE_TNAU.csv')

to remove duplicates
STPT_ND= df.drop_duplicates('column heading')

To remove certain columns, first view the available columns in the data frame then call only needed columns

df=pa.DataFrame(df,columns=['needed column 1','needed column 2', etc])


To save the data frames as csv

df.to_csv('path/file.csv')


To select rows with specific entry 
df1 = df[df.columnname == "row entry"]

To work with the date and time format of the istsos
Based on the answer

http://stackoverflow.com/questions/9632336/change-string-containing-datetime-to-another-format-of-datetime http://stackoverflow.com/questions/1398674/python-display-the-time-in-a-different-time-zone

dateS = "28-08-2013 09:00" 
from datetime import datetime 
my_date = datetime.strptime(dateS, '%d-%m-%Y %H:%M')
my_new_string = my_date.strftime('%Y-%m-%dT%H:%M:%S.000000+0530')
>>>'2013-08-28T09:00:00.000000+0530'

Another code

from pytz import timezone
from datetime import datetime
India = timezone('Asia/Kolkata')
in_time = datetime.now(India)
print in_time.strftime('%Y-%m-%d_%H-%M-%S')


Date time editing using pandas
to know python packages version for example for pandas

pandas.__version__


the to_datetime to edit whole column date and time, 
based on
http://stackoverflow.com/questions/17134716/convert-dataframe-column-type-from-string-to-datetime
and for strftime
http://stackoverflow.com/questions/13999850/how-to-specify-date-format-when-using-pandas-to-csv

Dt = pa.to_datetime(df[‘Time’], format=‘%Y-%m-%dT%H:%M:%S.000000+0530’) Dt2 = df[‘Time’].apply(lambda x: x.strftime(‘%Y-%m-%dT%H:%M:%S.000000+0530’))

Setting index for the date time column
df = pa.read_csv(‘csv file’,index_col=‘Time’)
