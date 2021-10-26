#Adithya Kalyan Sensor Readings 10/2021
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
	
