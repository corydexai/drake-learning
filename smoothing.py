
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
