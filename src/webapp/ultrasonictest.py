import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


TRIG = 21
ECHO = 20

print ("Distance Measurement in proggress")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
print("Waiting for sensor to setup")
time.sleep(2)



def detectPerson():
    
    while(GPIO.input(ECHO) == 0):
        pulse_start = time.time()
        #print("got start time")
    while(GPIO.input(ECHO) == 1):
        pulse_end = time.time()
        #print("got end time")

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print("Distance: ", distance, "cm")
    time.sleep(2)
    return distance

while(True):
    print("reached beginning")
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    detectPerson()


GPIO.cleanup()
