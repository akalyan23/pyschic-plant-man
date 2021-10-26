import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
#from ecapture import ecapture as ec
import wolframalpha
import json
import requests
from app import sensor_readings 

engine=pyttsx3.init()
#engine.setProperty('rate',100)
engine.setProperty('volume',1) 
voices=engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')

def speak(text):
	"""
	This function converts string text into speech
	"""
	
	engine.say(text)
	engine.runAndWait()
	

def acceptCommand():
	r=sr.Recognizer()
	mic = sr.Microphone(device_index=2)
	with mic as source:
		print (source)
		speak("I'm Listening. Please state your command") #Should replace this with an audio queue to let the user know that the ai is listening
		print("Listening...")
		audio=r.listen(source, None, 4)

		try:
			usercommand=r.recognize_google(audio,language="en-US")
			print(f"user said: {usercommand}\n") #This is just for debugging right now. Prints in the terminal the user's command.
			if "feeling" in usercommand:
				if getPlantData.temperature > 60 and getPlantData.temperature < 80:
					speak("I'm doing just fine sir. Thank you!")
				elif getPlantData.temperature > 80:
					speak("I'm dying, please help")
				elif getPlantData.temperature < 60:
					speak("Warm me up, please")
			
		except Exception as e:
			speak("I couldn't understand you, may you please repeat?")
			return "None"
		return usercommand
def getPlantData():
	temperature, humidity = sensor_readings()
	print(f"The Temperature is {temperature} and the Humidity is {humidity}")
	return float(temperature), float(humidity)

print(getPlantData())



print(acceptCommand())

