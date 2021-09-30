import numpy # https://www.instructables.com/Plot-Data-of-DHT11-Using-Raspberrypi-and-Arduino-U/ 
import matPlotLib as plt
from drawNow import *

tempF = []
humidity = []
plt.ion()

def makeFig():
 plt.yLim(60,80)
 plt.title('Real time temp and humidity of my plant')
 plt.grid(True)
 plt.ylabel('Temp F')
 plt.xlabel('Time')
 plt.plot(tempF,'b^-',label = 'degree F')
 plt.legend(loc = 'upper right')
 plt2=plt.twinx()
 plt.ylim(50,70) 
 plt2.plot(humidity, 'g*-', label='Humidity')
 plt2.set_ylabel('Humidity')
 plt2.ticklabel_format(useOffset=False)
 plt2.legend(loc='upper left')
 temp = float( dataArray[0])
 hum = float( dataArray[1])
 tempF.append(temp)
 humidity.append(hum)
 drawnow(makeFig)
 plt.pause(.000001)
 count+=1
  
 if(count>20): 
  tempF.pop(0)
  humidity.pop(0)
  
