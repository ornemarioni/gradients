import numpy as np
import bines2

#----------------------------------------------------------------------
# Metalicities profiles
#----------------------------------------------------------------------
def met(R,FeH,nbin):
    
    med, nodos = bines2.rbin1(R, nbin)
    
    Fe_H = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i])) #& (z>0))
        
        if len(mask)==0:
            # print('Me falta un bin! (FeH)')
            continue
        
        Fe_H[i] = np.median(FeH[mask])
        
    return med, Fe_H

#----------------------------------------------------------------------
def met_esf(r,FeH,nbin):
    
#     nodos = np.linspace(0,r.max(),nbin+1)
    
#     med = nodos[:-1] + np.diff(nodos)/2.

    med, nodos = bines2.rbin1(r, nbin)
    
    Fe_H = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((r < nodos[i+1]) & (r > nodos[i]))
        
        if len(mask)==0:
            # print('Me falta un bin! (FeH)')
            continue
        
        Fe_H[i] = np.median(FeH[mask])
        # Fe_H[i] = np.mean(FeH[mask])
        
    return med, Fe_H

#---------------------------------------------------------------------------
def met_log(R,met,nbin,nodo_min=np.log10(0.2)):
    
    if len(R)!=len(met):
        raise ValueError('vector must have the same length')
    
    nodos = np.logspace(nodo_min,np.log10(R.max()),nbin+1)
    
    med = nodos[:-1] + np.diff(nodos)/2.
    
    metal = np.ones(nbin)*np.nan
    p25 = np.ones(nbin)*np.nan
    p75 = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]))
        
        if len(mask)<2:
            # print('Me falta un bin! (FeH)')
            continue
        
        metal[i] = np.median(met[mask])
        p25[i],p75[i] = np.percentile(met[mask],[25,75])
        
    return med, metal, p25, p75
