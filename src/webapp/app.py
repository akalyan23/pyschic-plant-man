from flask import Flask, render_template, send_from_directory, jsonify
import adafruit_dht
import board
import time
from adafruit_seesaw.seesaw import Seesaw
import numpy # https://www.instructables.com/Plot-Data-of-DHT11-Using-Raspberrypi-and-Arduino-U/ 
import matplotlib as plt
#from matplotlib.figure import figure 
from drawnow import *

dhtSensor = adafruit_dht.DHT22(board.D4)
i2c_bus = board.I2C()
ss = Seesaw(i2c_bus, addr=0x36)
app = Flask(__name__) 

# realtime endpoint API
@app.route ('/realtime')
def rl ():
	temperature, humidity, moisture, plant_temperature = sensor_readings()
	return jsonify(
       	temperature=temperature,
        humidity=humidity,
        moisture=moisture,
        plant_temperature=plant_temperature
    )

@app.route('/')
def index():
	return send_from_directory('templates', "index.html")

def sensor_readings():
	while True:
		try:
			humidity = dhtSensor.humidity
			temp_c = dhtSensor.temperature
			moisture = ss.moisture_read()
			plant_temp = ss.get_temp()
			
		except RuntimeError:
			print(dhtSensor.humidity, dhtSensor.temperature, ss.moisture_read(), ss.get_temp())
			print("Error, trying again...")
			continue
		break
	#humidity = format(humidity, ".2f")
	#temp_f = format(temp_c * 9.0/5.0 + 32.0, ".2f")
	temp_f = temp_c * 9.0/5.0 + 32.0
	plant_temp = format(plant_temp, ".2f")
	print(f"The Temperature, as per app, is {temp_f} and humidity is {humidity} and the moisure is {moisture} and the plant temp is {plant_temp}")
	return temp_f, humidity, moisture, plant_temp


if __name__ == "__main__":
	app.run()
