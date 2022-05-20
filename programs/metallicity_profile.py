import numpy as np
import bines2

#----------------------------------------------------------------------
# Half-mass scale height
#----------------------------------------------------------------------
def met(R,z,FeH,nbin):
    
    med, nodos = bines2.rbin1(R, nbin)
    
    Fe_H = np.zeros(nbin)
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]) & (z>0))
        
        if len(mask)==0:
            print('Me falta un bin! (FeH)')
            continue
        
        Fe_H[i] = np.median(FeH[mask])
        
    return med, Fe_H