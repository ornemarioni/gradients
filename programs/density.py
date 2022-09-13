import numpy as np
import bines2

#----------------------------------------------------------------------
# Densidad superficial de masa
#----------------------------------------------------------------------
def surf_density(R,m,nbin):
    
    if len(R)!=len(m):
        raise ValueError('vector must have the same length')
    
    med, nodos = bines2.rbin1(R, nbin)
    
    sigma = np.zeros(nbin)
    
    for i in range(nbin):
        area = np.pi*(nodos[i+1]**2 - nodos[i]**2)
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]))
        
        if len(mask) == 0:
            print('Me falta un bin! (SurfDen)')
            continue
        
        sigma[i] = np.sum(m[mask])/area
        
    return sigma, med
        
    
#----------------------------------------------------------------------
# Densidad volumetrica de masa
#----------------------------------------------------------------------    
def vol_density(r, m, nbin):
    
    med, nodos = bines2.rbin1(r, nbin)
    
    rho = np.zeros(nbin)
    
    for i in range(nbin):
        vol = (4/3.)*np.pi*(nodos[i+1]**3 - nodos[i]**3)
        
        mask, = np.where((r < nodos[i+1]) & (r > nodos[i]))
        
        rho[i] = np.sum(m[mask])/vol
        
    return rho, med

#----------------------------------------------------------------------
# Densidad superficial de masa log bin
#----------------------------------------------------------------------
def surf_density_log(R,m,nbin,nodo_min=np.log10(0.2)):
    
    if len(R)!=len(m):
        raise ValueError('vector must have the same length')
    
    nodo_max = np.log10(R[~np.isnan(R)].max())
    nodos = np.logspace(nodo_min,nodo_max,nbin+1)
    
    med = nodos[:-1] + np.diff(nodos)/2.
    
    sigma = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        area = np.pi*(nodos[i+1]**2 - nodos[i]**2)
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]))
        
        if len(mask) == 0:
            # print('Me falta un bin! (SurfDen)')
            continue
        
        sigma[i] = np.sum(m[mask])/area
        
    return sigma, med