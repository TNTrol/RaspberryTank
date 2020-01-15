import RPi.GPIO as GPIO

#name
PIN1 = 1
PIN2 = 2
PIN3 = 3
PIN4 = 4
#. . .

class Tank(object):
	def __init__(self):
		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		#init pin
		GPIO.setup(PIN1, GPIO.OUT)
		#. . .

	def doing(self, value):
        	#something code
		#with GPIO.output(pin, value)
		pass
