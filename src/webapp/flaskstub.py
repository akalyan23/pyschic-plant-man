from flask import Flask, render_template, send_from_directory

from opensimplex import OpenSimplex

from flask import jsonify

noise_temp = OpenSimplex()
noise_humidity = OpenSimplex()

noise_i = 0

app = Flask(__name__)

def getNoise ():
    global noise_i
    return  noise_i, noise_temp.noise2d(noise_i, 0)*10+70, noise_humidity.noise2d(noise_i, 0) 

@app.route ('/realtime')
def rl ():
	global noise_i
	i, temperature, humidity = getNoise()
	noise_i += 1
	return jsonify(
        index=i,
        temperature=temperature,
        humidity=humidity
    )
	
@app.route('/')
def index():
	i, temperature, humidity = getNoise()
	return send_from_directory('templates', "index.html")

if __name__ == "__main__":
	app.run()