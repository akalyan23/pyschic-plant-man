import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
from random import choice
import json
# import webbrowser
# import os
# import time
# import subprocess
# #from ecapture import ecapture as ec
# import wolframalpha
# import json
# import requests
# from app import sensor_readings 
	# The line above NEEDS to be uncommented. DO NOT push this version. 

engine=pyttsx3.init()
#engine.setProperty('rate',100)
engine.setProperty('volume',1) 
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

r=sr.Recognizer()

# Skye Kychenthal
# Loads a random name
def loadName ():
	return choice([
		"joe", "rohan", "skye", "intercontinental ballistic missile", "wolfe", "advaith", "bao", "sruti", "god", "plant", "planty mc plant face"
	])

# Skye Kychenthal
# Loads the users name
def loadUser():
	return "rohan"

# Skye Kychenthal
# Loads commands from a JSON 
# There is a array of triggers, if any of them are heard the "res" response is given
# IE if the trigger is hello and the res is "hi, how are you?" when it hears hello it will respond with the res
def loadCommands ():
	dr = "/Users/Nick/Desktop/pyschic-plant-man/src/webapp/res.json"
	# dr = "res.json"
	return json.load (open(dr))["commands"]

# Skye Kychenthal
# checks for variables in a trigger-res response
# A variable takes the shape of $name and the $name is replaced with the variable in the response
def checkForVar (t):
	vs = t.split("$")[1].split(' ')[0] # VS is every single variable name that starts with a $
	for v in vs:
		if (v == "temp"):
			temp = 70
			addition = ""

			# Adds another message on top if the plant is too hot or too cold
			# Numbers are arbitrary for now
			if (temp > 80):
				addition = "I am really hot."
			elif (temp < 50):
				addition = "I am freezing."

			return t.replace('$temp', temp)+addition # Replaces the var name with the temp variable in the response

	return t

def speak(text):
	"""
	This function converts string text into speech
	"""
	
	engine.say(text)
	engine.runAndWait()
	
cmds = loadCommands() # short for commands

# Rohan Nunuganda
# Rohan please comment
async def acceptCommand():
	with sr.Microphone() as source:
		print('Listening...') #Should replace this with an audio queue to let the user know that the ai is listening
		audio=r.listen(source, None, 2)

		try:
			usercommand=r.recognize_google(audio,language="en-US")
			print(f"user said: {usercommand}\n") #This is just for debugging right now. Prints in the terminal the user's command.

			if "what is" in usercommand:
				topic = (usercommand.split("what is ")[1])
				results = wikipedia.summary(topic, 2, auto_suggest=False)
				print(results)

			# If none of the custom commands work, go to the chatbot commands
			else:
				# Skye Kychenthal
				# Iterates through commands and speaks the in to out values
				for c in cmds: #looks at all command pairs in the cmds structure
					for t in c['trigger']: # iterates through all triggers for the command
						if t in usercommand: # t is the specific trigger for the a response
							msg = checkForVar(choice(c['res']))
							msgs.append(msg)
							return speak (msg) # Speaks then returns so no more responses trigger. Checks for variables using checkForVar
		
		except Exception as e:
			print(e)
			speak("I couldn't understand you, may you please repeat?")
			return 0
		return 0

# def getPlantData():
# 	temperature, humidity = sensor_readings()
# 	return f"The Temperature is {temperature} and the Humidity is {humidity}"

#print(getPlantData())

# acceptCommand()

