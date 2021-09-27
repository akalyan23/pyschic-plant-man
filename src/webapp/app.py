from flask import Flask, render_template
import adafruit_dht
import board
import numpy # https://www.instructables.com/Plot-Data-of-DHT11-Using-Raspberrypi-and-Arduino-U/ 
import matplotlib as plt
#from matplotlib.figure import figure 
from drawnow import *

dhtSensor = adafruit_dht.DHT22(board.D4)
app = Flask(__name__)

@app.route('/')
def index():
	temperature, humidity = sensor_readings()
	#make_graphs()
	return render_template("index.html", temperature=temperature, humidity=humidity)
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
def make_graphs():
	"""
	This method does NOT work. May need to refactor.
	"""
	tempF = []
	humidity = []
	plt.ion()
	plt.ylim(60,80)
	plt.title('Real time temp and humidity of my plant')
	plt.grid(True)
	plt.ylabel('Temp F')
	plt.xlabel('Time')
	plt.plot(tempF,'b^-',label = 'degree F')
	plt.legend(loc = 'upper right')
	plt2=plt.twinx()
	plt.ylim(50,70) 
	plt2.plot(humidity, 'g*-', label='Humidity')
	plt2.set_ylabel('Humidity')
	plt2.ticklabel_format(useOffset=False)
	plt2.legend(loc='upper left')
	temp, hum = sensor_readings()
	tempF.append(temp)
	humidity.append(hum)
	drawnow(make_graphs)
	plt.pause(.000001)
	count+=1
  
	if(count>20): 
		tempF.pop(0)
		humidity.pop(0)
	return fig1, fig2


if __name__ == "__main__":
	app.run()
