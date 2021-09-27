import adafruit_dht 
from ISStreamer.Streamer import Streamer 
import time 
import pyttsx3 
import board

SENSOR_LOCATION_NAME = "Plant"
BUCKET_NAME = "Plant Stats"
BUCKET_KEY = "dht22sensor"
ACCESS_KEY = "ist_qejleu2n7ZQvCuKUsSngQjbBfwAktkJ4"
MINUTES_BETWEEN_READS = 1/12
METRIC_UNITS = False

dhtSensor = adafruit_dht.DHT22(board.D4)
streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
engine = pyttsx3.init()


while True:
	try:
		temp_c = dhtSensor.temperature
		humidity = dhtSensor.humidity
	except RuntimeError:
		print("Error, trying again...")
		continue
	temp_f = format(temp_c * 9.0/5.0 + 32.0, ".2f")
	streamer.log(SENSOR_LOCATION_NAME + "Temperature(F)", temp_f)
	humidity = format(humidity, ".2f")
	streamer.log(SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
	print("Temperature is " + temp_f, "Humidity is " + humidity)
	if float(temp_f) > 90.0: #These temperature checks are keeping the snake plant in mind. May change this to a web application where user can choose out of some of the most common plants. 
		engine.say("I am too hot!")
		engine.runAndWait()
	elif float(temp_f) < 70.0:
		engine.say("I am too cold!")
		engine.runAndWait()
#	else:
#		engine.say("Temperature is perfect!")
#		engine.runAndWait()
	if float(humidity) > 60.0: #Same snake plant reference for humidity
		engine.say("Humidity is too high!")
		engine.runAndWait()
	elif float(humidity) < 40.0:
		engine.say("Humidity is too low!")
		engine.runAndWait()
#	else:
#		engine.say("Humidity is perfect!")
#		engine.runAndWait() 
	streamer.flush()
	time.sleep(60*MINUTES_BETWEEN_READS)
engine.stop()


