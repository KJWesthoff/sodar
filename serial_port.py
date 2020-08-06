# listen to serial port

import serial
import time
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ser = serial.Serial('/dev/ttyACM0',9600)
#time.sleep(2)

timestamp = []
distancestamp = [] 



def animate(i):
    timestamp.append(read_dist()[0])
    distancestamp.append(read_dist()[1])
    
    plt.cla()
    plt.plot(timestamp,distancestamp)

# parse data from serial port
def read_dist():
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    
    try:
        dist = float(string)
        t = time.time()
        return (t,dist)
    except:
        exit #exit function
    


ani = FuncAnimation(plt.gcf(), animate, interval = 500)

plt.tight_layout
plt.show()


#while True:
#    read_dist()
#    time.sleep(0.1)
    
    
 
ser.close()
