 **AWS_postgresql_remote_host_connection**

To connect and run pstgresql database for istsos in aws ubunut 12.04. As per istsos tutorial, specifying localhost in database credentials says the database is inactive and subsequent service creation will be end up in error, saying wrong database
the postgresql TCP/IP connection and access credentials has to changed.

* have to edit

sudo nano /etc/postgresql/9.1/main/postgresql.conf

file line listen_addresses ‘localhost’ to listen_addresses ‘*’
and

* sudo nano /etc/postgresql/9.1/main/pg_hba.conf

file ipv4 section IP address to

host    all      all        0.0.0.0/0            md5

the line

#host    all     all       127.0.0.1/32            md5

has to be un comment as above.

* then postgreql has to be restarted by this comment
/etc/init.d/postgresql restart the aws security group also has to be changed for credential for port number 5432 with allowable ip address. and the port for postgrsql is the aws instance name given by aws 

* based on

    https://github.com/snowplow/snowplow/wiki/Setting-up-PostgreSQL
    http://hackgeo.com/cloud-computing/amazon-web-services/configuring-postgresql-9-1-and-postgis-2-on-ubuntu-12-04-in-amazon-aws
    http://askubuntu.com/questions/50621/cannot-connect-to-postgresql-on-port-5432
    http://www.cyberciti.biz/faq/postgresql-remote-access-or-connection/
