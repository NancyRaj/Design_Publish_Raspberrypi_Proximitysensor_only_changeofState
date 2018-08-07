
#Display only when there is a change of state in sensor
#Publish from RaspberryPi
"""
import Package
Create a client object
Connect the client to broker
Publish data
Disconnect from the broker
"""
import paho.mqtt.client as mq
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BOARD)
pin=10
gpio.setup(pin,gpio.IN)
init=0
c=mq.Client()
while True:
    val=gpio.input(pin)
    if val==1 and init==0:
        c.connect('iot.eclipse.org',1883)
        time.sleep(1)
        c.publish('nancy/iot','No object present')
        c.disconnect()
        print('No object present')
        init=1
    
    elif val==0 and init==1:
        c.connect('iot.eclipse.org',1883)
        time.sleep(1)
        c.publish('nancy/iot','Object Present')
        c.disconnect()
        print('Object is detected')
        init=0
    