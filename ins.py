#Before you install, it is important to run update and upgrade;

	#sudo apt-get update
	#sudo apt-get upgrade

#Either install connector for Python 2;

	#sudo apt-get -y install python-mysql.connector
	
#Or install connector for Python 3;

	#sudo apt-get -y install python3-mysql.connector

import mysql.connector

cnx = mysql.connector.connect(host='localhost',user='root',password = 'root',database='iot')
cursor = cnx.cursor()


add_employee = ("INSERT INTO sensor_data(temp_sensor) VALUES (%s)")

data_employee = ('0')

# Insert new employee
cursor.execute(add_employee, data_employee)

# Make sure data is committed to the database
cnx.commit()

cursor.close()
cnx.close()
