import numpy
import matPlotLib as plt
from drawNow import
tempF = []
plt.ion()
def makeFig()
  plt.yLim(60,80)
 plt.title('Real time temp and humidity of my plant')
 plt.grid(True)
 plt.ylabel('Temp F')
 plt.xlabel('Time')
 plt.plot(tempF,'b^-',label = 'degree F')
 plt.legend(loc = 'upper right')
 
