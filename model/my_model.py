import numpy as np
import GPy
import math

def simple():
    holder = np.zeros(10)
    for i in range(10):
        holder[i] = i
        
    print(holder)
        
    return holder
