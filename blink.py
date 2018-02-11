import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

while True:
	GPIO.output(11,GPIO.HIGH)
	print "high"
	time.sleep(1)
	GPIO.output(11,GPIO.LOW)
	print "low"
	time.sleep(1)
	
