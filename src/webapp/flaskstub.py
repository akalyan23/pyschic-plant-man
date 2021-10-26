# Skye Kychenthal
# Stub flask server producing realtime values randomized using perlin noise

from flask import Flask, render_template, send_from_directory, jsonify

from opensimplex import OpenSimplex # OpenSimplex is a function emulating Perlin noise

import threading

import asyncio

msgs = []

import ai

# ai.speak(f"Hello {ai.loadUser()}, {ai.loadName()} is now speaking!")
# ai.speak("How would I help you?")

noise = OpenSimplex()

noise_i = 0 # The index for the perlin noise

app = Flask(__name__)

noises = [] 

def randomize (t):
	return (t-2)*2

# Gets a noise value roughly between 68 and 72
def getNoise ():
    global noise_i
    return  noise_i, int(noise.noise2d(noise_i, 0)*4+70), int(noise.noise2d(randomize(noise_i), 0)*4+55)

@app.route ('/msgs')
def messages ():
	return jsonify(m=msgs)

# realtime endpoint API
@app.route ('/realtime')
def rl ():
	global noise_i
	i, temperature, humidity = getNoise()
	noises.append (getNoise())
	noise_i += 1
	return jsonify(
        index=i,
        temperature=temperature,
        humidity=humidity
    )

# Currently unused enpoint that gets the latest 10 points
# This is being done on the front-end using cookies
@app.route('/getlatest')
def ten ():
	global noise_i, noises

	latest = []
	if (noises > 10):
		for i in range (10):
			latest.append( noises[len(noises)-1-i] )

		return jsonify(
			latest=latest
		)

	return 0
	
# The index returning the index.html file
@app.route('/')
def index():
	# i, temperature, humidity = getNoise()
	return send_from_directory('templates', "index.html")


async def main ():
	asyncio.run(ai.acceptCommand())
	print ("MEOW")
	return 0

if __name__ == "__main__":
	main()