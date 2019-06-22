import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =",str(message.payload.decode("utf-8")))
print('heey')

broker = "192.168.0.114"

client = mqtt.Client('rpi')
client.connect(broker)

while True:
    client.loop_start()
    client.on_message=on_message
    client.subscribe("stat/fan/POWER")#subscribe
    time.sleep(1)
client.disconnect() #disconnect
client.loop_stop() #stop loop
