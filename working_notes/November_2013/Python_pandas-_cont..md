**Python_pandas-_cont.**
To call specific column in data frame df[df.columns[2:4]]
To join called rows, in concatenating fashion df[“DateTime”] = [’ ’.join(row) for row in df[df.columns[2:4]].values]
To speifiy the date time foramte in data frame of DPCC dMDI_DT= pa.to_datetime(Time, format=‘%A, %B %d, %Y %H:%M:%S’)


based on http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/
http://stackoverflow.com/questions/12030398/concatenate-multiple-columns-based-on-index-in-pandas
A best tutorial for visualization in pyhton
http://nbviewer.ipython.org/urls/raw.github.com/bolhovsky/notebooks/master/earth-day-data-challenge.ipynb