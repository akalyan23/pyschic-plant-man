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
	with sr.Microphone() as source:
		print('Listening...') #Should replace this with an audio queue to let the user know that the ai is listening
		audio=r.listen(source)

		try:
			usercommand=r.recognize_google(audio,language="en-US")
			print(f"user said: {usercommand}\n") #This is just for debugging right now. Prints in the terminal the user's command.
		except Exception as e:
			speak("I couldn't understand you, may you please repeat?")
			return "None"
		return usercommand
def getPlantData():
	temperature, humidity = sensor_readings()
	return f"The Temperature is {temperature} and the Humidity is {humidity}"
#print("hello 1")
#print(getPlantData())
print("Hello")
print("This code is actually running...")
print(acceptCommand())
