import time
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

while True:
    # reads moisture levels and takes the temperature level and converts it to F
   # read moisture level through capacitive touch pad
   touch = ss.moisture_read()

   temp = ss.get_temp()
   temp_f = format(temp * 9.0 / 5.0 + 32, ".2f")
   
i2c = board.I2C()

lightsensor = adafruit_bh1750.BH1750(i2c)
    #it allows you to read the sensor readings from the bh1750 sensor much easier

while True:

   time.sleep(60*MINUTES_BETWEEN_READS)

