Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

while True:
   # read moisture level through capacitive touch pad
   # read temperature from the temperature sensor
   temp = ss.get_temp()
   
   print("temp: " + str(temp) + "  moisture: " + str(touch))
   
SyntaxError: multiple statements found while compiling a single statement
>>> 	import time #importing clock
	from board import SCL, SDA #importing two of the GPIOs from the board with sensor info (GPIO 2 & GPIO 3)
	import busio #module containing classes to support serial protocols 
	from adafruit_seesaw.seesaw import Seesaw#convertor that allows you to add or extend raspberry pi to sensor

	i2c_bus = busio.I2C(SCL, SDA)

	ss = Seesaw(i2c_bus, addr=0*36)
	
	while True:
		touch = ss.moisture_read()# read moisture level through capacitive touch pad
		temp = ss.get_temp()# read temperature from the temperature sensor
		print("temp: " + str(temp) + "  moisture: " + str(touch))
		
SyntaxError: unexpected indent
>>> import time #importing clock
from board import SCL, SDA #importing two of the GPIOs from the board with sensor info (GPIO 2 & GPIO 3)
import busio #module containing classes to support serial protocols 
from adafruit_seesaw.seesaw import Seesaw#convertor that allows you to add or extend raspberry pi to sensor

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0*36)
	
while True:
	touch = ss.moisture_read()# read moisture level through capacitive touch pad
	temp = ss.get_temp()# read temperature from the temperature sensor
	print("temp: " + str(temp) + "  moisture: " + str(touch))
	
SyntaxError: multiple statements found while compiling a single statement
>>> import time #importing clock
from board import SCL, SDA #importing two of the GPIOs from the board with sensor info (GPIO 2 & GPIO 3)
import busio #module containing classes to support serial protocols
from adafruit_seesaw.seesaw import Seesaw#convertor that allows you to add or extend raspberry pi to sensor

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0*36)
	
while True:
	touch = ss.moisture_read()
	# read moisture level through capacitive touch pad
	temp = ss.get_temp()
	# read temperature from the temperature sensor
	print("temp: " + str(temp) + "  moisture: " + str(touch));
	
SyntaxError: multiple statements found while compiling a single statement
>>> import time #importing clock
from board import SCL, SDA #importing two of the GPIOs from the board with sensor info (GPIO 2 & GPIO 3)
import busio #module containing classes to support serial protocols
from adafruit_seesaw.seesaw import Seesaw#convertor that allows you to add or extend raspberry pi to sensor

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0*36)
	
while True:
	touch = ss.moisture_read()
	# read moisture level through capacitive touch pad
	temp = ss.get_temp()
	# read temperature from the temperature sensor
	print("temp: " + str(temp) + "  moisture: " + str(touch)) time.sleep(1);
	
SyntaxError: multiple statements found while compiling a single statement
>>> #Adithya Kalyan Sensor Readings 10/2021
import time
	#importing clock
from board import SCL, SDA
	#importing two of the GPIOs from the board with sensor info (GPIO 2 & GPIO 3)

import busio
	#module containing classes to support serial protocols

from adafruit_seesaw.seesaw import Seesaw
	#convertor that allows you to add or extend raspberry pi to sensor

i2c_bus = busio.I2C(SCL, SDA)
#SCL is clock pin, SDA is data pin
ss = Seesaw(i2c_bus, addr=0*36)
	
while True:
	#This loop gets the moisture sensor values and the temperature sensor values and prints them into a string
	touch = ss.moisture_read()
	temp = ss.get_temp()
	print("temp: " + str(temp) + "  moisture: " + str(touch)
	      
	time.sleep(1);
		#halting the function for one second before running it again
	
