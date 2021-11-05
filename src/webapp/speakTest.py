# Runs through all responses in order to check if they sound good or not

import pyttsx3
import json

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Skye Kychenthal
# Loads commands from a JSON 
# There is a array of triggers, if any of them are heard the "res" response is given
# IE if the trigger is hello and the res is "hi, how are you?" when it hears hello it will respond with the res
def loadCommands (dr=""):
    norm = loadFile (dr)
    blair = loadFile ("res", dr)
    for r in blair:
        norm.append (r)
    return norm

def loadFile (ff="res", dr=""):
    print (ff, dr)
    return json.load (open(dr + f"{ff}.json"))["commands"]


def speak(text):
	"""
	This function converts string text into speech
	"""
	
	engine.say(text)
	engine.runAndWait()


# cmds = loadCommands("/Users/Nick/Desktop/pyschic-plant-man/src/webapp/")
cmds = loadFile(ff="blairres", dr="/Users/Nick/Desktop/pyschic-plant-man/src/webapp/")

# speak ("Testing commands")

# Peddie has to be written as "pedd e"
for c in cmds: #looks at all command pairs in the cmds structure
    #print("c" + c)
    print(c['trigger'])
    words = ''
    for l in c['trigger']:
        words += l
    speak("Testing for the words " + words)
    for t in c['res']: # iterates through all triggers for the command
        print (t)
        speak (t)