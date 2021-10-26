from flask import Flask, render_template, send_from_directory, jsonify
import adafruit_dht
import board
import numpy # https://www.instructables.com/Plot-Data-of-DHT11-Using-Raspberrypi-and-Arduino-U/ 
import matplotlib as plt
#from matplotlib.figure import figure 
from drawnow import *

dhtSensor = adafruit_dht.DHT22(board.D4)
app = Flask(__name__) 

# realtime endpoint API
@app.route ('/realtime')
def rl ():
	temperature, humidity = sensor_readings()
	return jsonify(
        temperature=temperature,
        humidity=humidity
    )

@app.route('/')
def index():
	return send_from_directory('templates', "index.html")

def sensor_readings():
	while True:
		try:
			humidity = dhtSensor.humidity
			temp_c = dhtSensor.temperature
		except RuntimeError:
			print("Error, trying again...")
			continue
		break
	#humidity = format(humidity, ".2f")
	temp_f = format(temp_c * 9.0/5.0 + 32.0, ".2f")
	print(f"The Temperature, as per app, is {temp_f} and humidity is {humidity}")
	return temp_f, humidity

if __name__ == "__main__":
	app.run()
