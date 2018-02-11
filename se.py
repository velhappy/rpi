import RPi.GPIO as GPIO
import time
import mysql.connector

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.IN)

cnx = mysql.connector.connect(host='localhost',user='root',password = 'root',database='iot')
cursor = cnx.cursor()
add_employee = ("INSERT INTO sensor_data(temp_sensor) VALUES (%s)")

while True:
	a=GPIO.input(7)
	data_employee = (str(a))
	print a
	cursor.execute(add_employee, data_employee)
	cnx.commit()
	time.sleep(2)
