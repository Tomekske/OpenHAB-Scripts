import time

import RPi.GPIO as GPIO

pin = 17
led = 27
led2 = 22


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)



print("init")

while True:
	GPIO.output(led, False)
	GPIO.output(led2, False)

	time.sleep(2)
	GPIO.output(led, True)
	GPIO.output(led2, True)
	time.sleep(2)
