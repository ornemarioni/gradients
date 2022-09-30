import numpy as np

#-------------------------------------------------------------------------------------------------
# VELOCITY DISPERTION 1-D
#-------------------------------------------------------------------------------------------------

def vel_disp(v):
    
    v_mean = np.mean(v)

    v_sqdiff = (v - v_mean)**2
    v_disp2 = np.sum(v_sqdiff/(len(v)-1))
    v_disp = np.sqrt(v_disp2)
        
    return v_disp
