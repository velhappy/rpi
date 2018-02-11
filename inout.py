import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.setup(7,GPIO.IN)

while True:
	
	a=GPIO.input(7)
	
	if a==1:
		GPIO.output(11,GPIO.HIGH)
		print "high"
	else:
		GPIO.output(11,GPIO.LOW)
		print "LOW"
		
