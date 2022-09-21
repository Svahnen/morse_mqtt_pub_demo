import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
GPIO.setmode(GPIO.BOARD)

buttonPin = 16  # GPIO 23

mqttBroker = "35.228.72.67"  # IP address of the MQTT broker

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Enable pull up resistor on button so we dont need an external resistor

client = mqtt.Client() # Anonemous connection

pressed = False  # Variable to keep track of button state

loops = 0  # Variable to keep track of how many times the loop has run

while True:
    client.connect(mqttBroker)
    buttonState = GPIO.input(buttonPin)
    if buttonState == False:
        # Debounce and make sure every loop takes at least 0.1 seconds
        time.sleep(0.1)
        loops += 1
        if pressed == False:
            pressed = True
    else:
        if loops > 5 and pressed == True:  # If the button has been pressed for more than 5 = 0.5 seconds send long
            print("long")
            client.publish("morse", "_")  # Publish to topic morse
        elif pressed == True:  # If the button has been pressed for less, send short
            print("short")
            client.publish("morse", ".")  # Publish to topic morse
        pressed = False  # Reset pressed variable
        loops = 0  # Reset loops
