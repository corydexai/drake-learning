import pickle
import matplotlib.pyplot as plt

#i have hardcoded a single file. first rewrite would be to remove the hardcoding
data= pickle.load( open("C:\\Users\Cory's Asus\Documents\Dexai\converted logs\\20181203\T174049.pkd", "rb") )
mass_matrix =
coriolis_matrix = 
trimValues = 

#syler's function for writing out a menu of the contents of the lcm
def recursive_print_dict(dictionary, offset=''):
    for key in dictionary.keys():
        print (offset + key)
        if type(dictionary[key]) == dict:
            recursive_print_dict(dictionary[key], offset+'   ')

#my attempt at a moving average
#provide element of franka 0 status that you want to view.
#i have just realized time values are on the order of ten to the 15th.
#gonna have to zero that out.
#i'm trying to write this in a flexible manner instead of hardcoding and i'm struggling.
#not averaging the very beginning and very end points yet.            
def smoothing(n,data, value):
    smoothed=[]
#    time = data['FRANKA_0_STATUS']['utime']
    raw = data['FRANKA_0_STATUS'][value]
    length = len(raw)
    for i in range(length):
        if i<n:
            smoothed.append(raw[i])
        elif i>(length-n):
            smoothed.append(raw[i])
        else:
            values = raw[(i-n):(i+n)]
            sum(values)
            smoothed.append(values/(2*n+1))
        
    return smoothed
    
#sanity-checking initial and final values for datasests
#where we expect to be returning to neutral
def initialVsFinal(dataset):



#chopping apart the unhelpful spike+oscilation at the beginning of the motion. 
def trimData(   

recursive_print_dict(data)
x = data['FRANKA_0_STATUS']['joint_torque_measured']
y = data['FRANKA_0_STATUS']['utime']
start_time= y[0]
time = []
for i in y:
    time.append(i-start_time)
    
plt.plot(time,x)
plt.show()



smoothingSample = 2 #how many points to use for averaging. 
smoothing(smoothingSample,data[][])
              
