import Adafruit_DHT
import datetime
import csv
import time
import Adafruit_DHT
import datetime
import csv
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

def ReadSensor(sensor, pin):
    humidity,temperature = Adafruit_DHT.read_retry(sensor, pin)
    return round(humidity, 2), round(temperature, 2)

def on_message(client, userdata, message):
	dt = datetime.datetime.now()
	date = dt.strftime("%d-%m-%y")
	ctime = dt.strftime("%H:%M:%S")

	GPIO.output(led, True)
	humidity, temperature = ReadSensor(sensor, pin)
	print(date, ctime, humidity, temperature,str(message.payload.decode("utf-8")))
	with open('/home/openhabian/fan.csv', mode='a') as employee_file:
		csvWrite = csv.writer(employee_file, delimiter=',')
		csvWrite.writerow([date,ctime, humidity, temperature, str(message.payload.decode("utf-8"))])

broker = "192.168.0.114"

pin = 17
led = 27

client = mqtt.Client('rpi')
client.connect(broker)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

sensor = Adafruit_DHT.DHT22

print("Init: controlFan.py")

while True:
	GPIO.output(led, False)

	client.loop_start()
	client.on_message=on_message
	client.subscribe("stat/fan/POWER")

	time.sleep(2)

client.disconnect() #disconnect
client.loop_stop() #stop loop
