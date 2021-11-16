import speech_recognition as sr
import datetime
import wikipedia
from random import choice
import json
from app import sensor_readings
import RPi.GPIO as GPIO
import time
import re
import os

GPIO.setmode(GPIO.BCM)
TRIG = 21
ECHO = 20
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
time.sleep(2)

# Skye Kychenthal
# Loads commands from a JSON 
# There is a array of triggers, if any of them are heard the "res" response is given
# IE if the trigger is hello and the res is "hi, how are you?" when it hears hello it will respond with the res
def loadCommands ():
	dr = "res.json"
	return json.load (open(dr))["commands"]

#Rohan Nunugonda and Adithya
def detectPerson():
    while(GPIO.input(ECHO) == 0):
        pulse_start = time.time()
    while(GPIO.input(ECHO) == 1):
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    time.sleep(2)
    return distance

# Skye Kychenthal
# checks for variables in a trigger-res response
# A variable takes the shape of $name and the $name is replaced with the variable in the response
#def checkForVar (t):
#	_vs = t.split("$")
#	vs = []
#	if (len(_vs) > 0):
#		vs = _vs[1].split(' ')[0] # VS is every single variable name that starts with a $
#	else:
#		return t
#	print(vs)
#	print ("TEST")
#	if (vs == "temp"):
 #       	temp = getPlantTemperature()
  #      	addition = ""
#
 #       # Adds another message on top if the plant is too hot or too cold
  #      # Numbers are arbitrary for now
   #    		if (temp > 80):
    #        		addition = "I am really hot."
     #   	elif (temp < 60):
      #      		addition = "I am freezing."
#
 #       	return t.replace('$temp', temp)+addition # Replaces the var name with the temp variable in the response
#	return 

cmds = loadCommands() # short for commands
print(cmds)

def speak(text):
	"""
	This function converts string text into speech
	"""
	
	os.system(f"espeak -v f4 -p 80 -s 180 '{text}'") 
	
# Rohan Nunuganda
def acceptCommand():
	r=sr.Recognizer()
	mic = sr.Microphone()
	with mic as source:
		print('Listening...') 
		audio=r.listen(source, None, 4) #Listens for 4 seconds
		try:
			usercommand=r.recognize_google(audio,language="en-US")
			print(f"user said: {usercommand}\n") #This is just for debugging right now. Prints in the terminal the user's command.

			

			# If none of the custom commands work, go to the chatbot commands
				# Skye Kychenthal and Rohan Nunugonda
				# Iterates through commands and speaks the in to out values
			for c in cmds: #looks at all command pairs in the cmds structure
				for t in c['trigger']: # iterates through all triggers for the command
					print(t in usercommand)
					if t in usercommand: # t is the specific trigger for the a response
						msg = choice(c['res'])
						if "$" in msg:
							print("entered the gnarly if statement", msg)
							termInCheck = re.findall(r'[$]\w+', msg)
							print("termInCheck", termInCheck) 
							variableInCheck = termInCheck[0][1:]
							print("variableInCheck", variableInCheck)
							if variableInCheck == 'temp':
								msg = msg.replace(termInCheck[0], str(int(getPlantSoilTemp())))
								print("MSG: ", msg)
						#msg_checked = checkForVar(msg)
						#print("The Message is ", msg_checked)
						speak(msg) # Speaks then returns so no more responses trigger. Checks for variables using checkForVar
						return
							
            	#if "what is" in usercommand:
                 #   topic = (usercommand.split("what is ")[1])
                  #  results = wikipedia.summary(topic, 2, auto_suggest=False)
                  #  print(results)

		except Exception as e:
			print(e)
			speak("I couldn't understand you, may you please repeat?")
		return usercommand


def getPlantTemperature():
	temperature, humidity, moisture, plant_temp = sensor_readings()
	print(f"The Temperature is {temperature}")
	return temperature
def getPlantHumidity():
	temperature, humidity, moisture, plant_temp = sensor_readings()
	print(f"The Humidity is {humidity}")
	return humidity
def getPlantMoisture():
    temperature, humidity, moisture, plant_temp = sensor_readings()
    print(f"The Moisture is {moisture}")
    return moisture
def getPlantSoilTemp():
    temperature, humidity, moisture, plant_temp = sensor_readings()
    print(f"The Soil Temp is {plant_temp}")
    return plant_temp

while True:
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	distance = detectPerson()
	if distance <= 300:
        	speak("Hey you, come talk to me!")
        	acceptCommand()
GPIO.cleanup()







