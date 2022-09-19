import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

buttonPin = 16

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# sätter inbyggd resistor så man inte behöver koppla en egen

pressed = False

while True:
	buttonState = GPIO.input(buttonPin)
	if buttonState == False:
		if pressed == False:
			pressed = True
			print("pressed")
	else:
		pressed = False
