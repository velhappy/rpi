#login mysql

mysql -u root -p

#show databases
SHOW DATABASES;

#create databse
CREATE DATABASE iot;

#use database
USE iot;

#create table
create table sensor_data(
   id INT NOT NULL AUTO_INCREMENT,
   temp_sensor VARCHAR(10) NOT NULL,
   PRIMARY KEY ( id )
);

SHOW TABLES;

#insert data into table
INSERT INTO sensor_data(id,temp_sensor) VALUES(2,30);


#fetch data from table
SELECT id FROM sensor_data;
