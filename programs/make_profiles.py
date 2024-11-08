import numpy as np
import bines2

#----------------------------------------------------------------------
# Profiles
#----------------------------------------------------------------------
#Equal number bins
def profile_eqn(R, x_in, nbin):
    
    med, nodos = bines2.rbin1(R, nbin) 
    
    x_out = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i])) #& (z>0))
        
        if len(mask)==0:
            # print('Me falta un bin!')
            continue
        
        x_out[i] = np.median(x_in[mask])
        
    return med, x_out

#----------------------------------------------------------------------
# Spheric bins
def profile_esf(r, x_in, nbin):
    
#     nodos = np.linspace(0,r.max(),nbin+1)
    
#     med = nodos[:-1] + np.diff(nodos)/2.

    med, nodos = bines2.rbin1(r, nbin)
    
    x_out = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((r < nodos[i+1]) & (r > nodos[i]))
        
        if len(mask)==0:
            # print('Me falta un bin!')
            continue
        
        x_out[i] = np.median(x_in[mask])
        
    return med, x_out

#---------------------------------------------------------------------------
# Logarithm bins
def profile_log(R, x_in, nbin, nodo_min=np.log10(0.2)):
    
    if len(R)!=len(x_in):
        raise ValueError('vector must have the same length')
    
    nodos = np.logspace(nodo_min, np.log10(R.max()), nbin+1)
    
    med = nodos[:-1] + np.diff(nodos)/2.
    
    x_out = np.ones(nbin)*np.nan
    p25   = np.ones(nbin)*np.nan
    p75   = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]))
        
        if len(mask)<2:
            # print('Me falta un bin!')
            continue
        
        x_out[i]      = np.median(x_in[mask])
        p25[i],p75[i] = np.percentile(x_in[mask],[25,75])
        
    return med, x_out, p25, p75

#-----------------------------------------------------------------------------
#----------------------------------------------------------------------
# Profiles acumulativos (?)
#----------------------------------------------------------------------
#Equal number bins
def cumProfile_eqn(R, x_in, nbin):
    
    med, nodos = bines2.rbin1(R, nbin) 
    
    x_out = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i])) #& (z>0))
        
        if len(mask)==0:
            # print('Me falta un bin!')
            continue
        
        x_out[i] = np.nansum(x_in[mask])
        
    return med, x_out

#---------------------------------------------------------------------------
# Perfil acumulativo (?) Logarithm bins
def cumProfile_log(R, x_in, nbin, nodo_min=np.log10(0.2)):
    
    if len(R)!=len(x_in):
        raise ValueError('vector must have the same length')
    
    nodos = np.logspace(nodo_min, np.log10(R.max()), nbin+1)
    
    med = nodos[:-1] + np.diff(nodos)/2.
    
    x_out = np.ones(nbin)*np.nan
    p25   = np.ones(nbin)*np.nan
    p75   = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]))
        
        if len(mask)<2:
            # print('Me falta un bin!')
            continue
        
        x_out[i] = np.nansum(x_in[mask])
        
    return med, x_out

#-----------------------------------------------------------------------------
