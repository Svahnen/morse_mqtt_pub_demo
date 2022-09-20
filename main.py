import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time 
GPIO.setmode(GPIO.BOARD)

buttonPin = 16

mqttBroker ="35.228.72.67" 

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# sätter inbyggd resistor så man inte behöver koppla en egen

client = mqtt.Client("jonny_pi")
#client.connect(mqttBroker) 

pressed = False

loops = 0

while True:
	client.connect(mqttBroker)
	buttonState = GPIO.input(buttonPin)
	if buttonState == False:
		time.sleep(0.1)
		loops+=1
		if pressed == False:
			pressed = True
	else:
		if loops > 5 and pressed == True:
			print("long")
			client.publish("morse", "_")
		elif pressed == True:
			print("short")
			client.publish("morse", ".")
		pressed = False
		loops = 0
