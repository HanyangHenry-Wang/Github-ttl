from model.my_model import simple
import numpy as np

def aa():
    res = simple()
    np.savetxt('files.csv', res, delimiter=',')
    
    
if __name__=='__main__':
    aa()