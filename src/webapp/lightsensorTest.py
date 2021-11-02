#import board
#import digitalio
#import busio

#print("Hello Blinka")

#pin = digitalio.DigitalInOut(board.D4)
#print("digital io good")
#i2c = busio.I2C(board.SCL, board.SDA)
#print("i2c good")
#spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
#print("SPI good")
#print("done")

import time
import  board 
import adafruit_bh1750
import digitalio
import busio

i2c_bus = busio.I2C(SCL, SDA)
lightsensor = adafruit_bh1750.BH1750(i2c_bus, address=0x48)
while True:
	print("%.2f Lux" %  lightsensor.lux)
	time.sleep(1)
