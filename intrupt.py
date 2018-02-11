import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(31, GPIO.BOTH)
def my_callback():
    print(GPIO.input(31))
GPIO.add_event_callback(31, my_callback)

while 1:
	time.sleep(1000)

