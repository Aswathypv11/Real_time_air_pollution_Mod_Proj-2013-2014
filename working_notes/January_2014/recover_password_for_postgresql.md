**recover_password_for_postgresql**

based on 
http://scratching.psybermonkey.net/2009/06/postgresql-how-to-reset-user-name.html

1. sudo nano /etc/postgresql/9.1/main/pg_hba.conf
1. change |local   all         postgres    md5| to | local   all         postgres     trust|
1. sudo service postgresql restart
1. now enter into the postgresql using 
    psql -U postgres
1. ALTER USER postgres with password 'new password';
1. then again change the pg_hba.conf as  earlier and restart the postgresql for invoking the password protection