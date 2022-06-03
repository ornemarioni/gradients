import numpy as np
import bines2

#----------------------------------------------------------------------
# Half-mass scale height
#----------------------------------------------------------------------
def met(R,z,FeH,nbin):
    
    med, nodos = bines2.rbin1(R, nbin)
    
    Fe_H = np.zeros(nbin)
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i])) #& (z>0))
        
        if len(mask)==0:
            print('Me falta un bin! (FeH)')
            continue
        
        Fe_H[i] = np.median(FeH[mask])
        
    return med, Fe_H

#----------------------------------------------------------------------
def met_esf(r,FeH,nbin):
    
#     nodos = np.linspace(0,r.max(),nbin+1)
    
#     med = nodos[:-1] + np.diff(nodos)/2.

    med, nodos = bines2.rbin1(r, nbin)
    
    Fe_H = np.zeros(nbin)
    
    for i in range(nbin):
        
        mask, = np.where((r < nodos[i+1]) & (r > nodos[i]))
        
        if len(mask)==0:
            print('Me falta un bin! (FeH)')
            continue
        
        Fe_H[i] = np.median(FeH[mask])
        # Fe_H[i] = np.mean(FeH[mask])
        
    return med, Fe_H