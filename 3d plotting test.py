#trying to plot the joint positions like this didn't make sense.
#i tried to work with joint space coordinates like they were cartesian

#data plot exploration
import pickle
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import curve_fit
import numpy as np


data= pickle.load( open("C:\\Users\Cory's Asus\Documents\Dexai\converted logs\\20181203\T174049.pkd", "rb") )

#syler's function for writing out a menu of the contents of the lcm
def recursive_print_dict(dictionary, offset=''):
    for key in dictionary.keys():
        print (offset + key)
        if type(dictionary[key]) == dict:
            recursive_print_dict(dictionary[key], offset+'   ')

def smoothing(n,data, value):
    smoothed=[]
#    time = data['FRANKA_0_STATUS']['utime']
    raw = data['FRANKA_0_STATUS'][value]
    length = len(raw)
    for i in range(length):
        #print (i)
        if i<n:
            smoothed.append(raw[i])
        elif i>(length-n):
            smoothed.append(raw[i])
        else:
            values = raw[(i-n):(i+n+1)]
            #print (len(values))
            #print(values)           
            jointValues = []
            for j in range(7): #for each joing of bot...
                summing = 0
                for k in range(len(values)): #...for each point we grabbed...
                    summing += values[k][j]#...add up that joint's values across the 5...
                jointValues.append(summing/(2*n+1)) #append this joint's average
            smoothed.append(jointValues)#append full set of data for this point to smoothed list
            
                
        
    return smoothed

recursive_print_dict(data)
x = data['FRANKA_0_STATUS']['joint_position_measured']
smoothX = smoothing(12,data,'joint_position_measured')
y = data['FRANKA_0_STATUS']['utime']
start_time= y[0]
time = []
for i in y:
    time.append(i-start_time)


#print(len(data.keys()))
#plt.plot3d(smoothX)
#plt.title("Smoothing attempt @25 sample moving avg")
#plt.plot(time,x)
#plt.title("No smoothing attempt")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
print(smoothX[0])
#ax.plot(smoothX)
#plt.show()
