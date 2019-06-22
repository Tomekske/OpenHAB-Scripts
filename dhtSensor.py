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

broker = "192.168.0.114"
 
#broker_address="iot.eclipse.org" #use external broker
client = mqtt.Client("dht") #create new instance
client.connect(broker) #connect to broker

sensor = Adafruit_DHT.DHT22

pin = 17
led = 22

print("Init: dhtSensor.py")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led, False)

    time.sleep(5)
    GPIO.output(led, True)
    humidity, temperature = ReadSensor(sensor, pin)
    client.publish("/dht/temperature", temperature) #publish
    client.publish("/dht/humidity", humidity) #publish

    print(humidity, temperature)

    time.sleep(5)
