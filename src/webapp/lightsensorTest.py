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
import board
import adafruit_bh1750

i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

while True:
	print("%.2f Lux" %  sensor.lux)
	time.sleep(1)
