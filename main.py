import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt 
GPIO.setmode(GPIO.BOARD)

buttonPin = 16

mqttBroker ="35.228.72.67" 

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# sätter inbyggd resistor så man inte behöver koppla en egen

client = mqtt.Client("jonny_pi")
client.connect(mqttBroker) 

pressed = False

while True:
	buttonState = GPIO.input(buttonPin)
	if buttonState == False:
		if pressed == False:
			pressed = True
			print("pressed")
			client.publish("morse", ".")
	else:
		pressed = False
