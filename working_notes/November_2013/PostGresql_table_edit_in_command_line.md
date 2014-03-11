 **PostGresql_table_edit_in_command_line**

To edit the istsos data base table “measures” in postgresql
it is to over come the error in istsos import saying the the dylos reading is exceeding the digit limit of the column val_meas in the table. normally it is easy to change column digit size through pgadmin. But for command line it requires following commands.


1. Get access to postgresql

sudo -u postres psql

2. To view the datbase in postgresql
\dt

3. To connect with particular database
\c istsos      here istsos is data base

4. To display the details of table
\d dlyosecbe.measrues        here dlyosecbe.measrues is the table name
5. To change the columns digit size use the SQl command got from pgadmin
ALTER TABLE dyloscbe.measures k ALTER COLUMN val_msr TYPE numeric(14,6);