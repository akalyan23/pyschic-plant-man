import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
from random import choice
import json
from app import sensor_readings 
	# The line above NEEDS to be uncommented. DO NOT push this version. 

engine=pyttsx3.init()
#engine.setProperty('rate',100)
#engine.setProperty('volume',1) 
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
	"""
	This function converts string text into speech
	"""
	
	engine.say(text)
	engine.runAndWait()
	
# Rohan Nunuganda
# Rohan please comment
def acceptCommand():
	r=sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		print('Listening...') #Should replace this with an audio queue to let the user know that the ai is listening
		audio=r.listen(source, None, 4)
		try:
			usercommand=r.recognize_google(audio,language="en-US")
			print(f"user said: {usercommand}\n") #This is just for debugging right now. Prints in the terminal the user's command.
			

			if "feeling" in usercommand:
				if getPlantTemperature() > 60 and getPlantTemperature() < 80:
					speak("I'm doing just fine sir. Thank you!")
				elif getPlantTemperature() > 80:
					speak("I'm dying, please help")
				elif getPlantTemperature() < 60:
					speak("Warm me up, please")
			


			if "what is" in usercommand:
				topic = (usercommand.split("what is ")[1])
				results = wikipedia.summary(topic, 2, auto_suggest=False)
				print(results)

			# If none of the custom commands work, go to the chatbot commands
		

		except Exception as e:
			print(e)
			speak("I couldn't understand you, may you please repeat?")

			return "None"
		return usercommand
#def getPlantData():
#	temperature, humidity = sensor_readings()
#	print(f"The Temperature is {temperature} and the Humidity is {humidity}")
#	return temperature, humidity

def getPlantTemperature():
	temperature, humidity, moisture, plant_temp = sensor_readings()
	print(f"The Temperature is {temperature}")
	return temperature
def getPlantHumidity():
	temperature, humidity, moisture, plant_temp = sensor_readings()
	print(f"The Humidity is {humidity}")
	return humidity

# def getPlantData():
# 	temperature, humidity = sensor_readings()
# 	return f"The Temperature is {temperature} and the Humidity is {humidity}"

#print(getPlantData())


speak("Hello darling")
#getPlantData()
acceptCommand()



