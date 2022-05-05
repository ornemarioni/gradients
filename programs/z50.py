import numpy as np
import bines2

#----------------------------------------------------------------------
# Half-mass scale height
#----------------------------------------------------------------------
def HMSH(R,z,m,nbin):
    
    med, nodos = bines2.rbin1(R, nbin)
    
    z50 = np.zeros(nbin)
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]) & (z>0))
        
        zorder = np.argsort(z[mask])
        
        zsort = z[mask][zorder]
        msort = m[mask][zorder]
        
        if len(msort) == 0:
            continue
        
        mtot   = np.cumsum(msort)
        m_mean, = np.where(mtot < mtot[-1]/2.)
        
        if len(m_mean) == 0:
            continue
            
        z50[i] = zsort[m_mean][-1]
        
    return med, z50