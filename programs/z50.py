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
        
        if len(mask) == 0:
            print('Me falta un bin! (z50)')
        
        zorder = np.argsort(z[mask])
        
        zsort = z[mask][zorder]
        msort = m[mask][zorder]
        
        mtot   = np.cumsum(msort)
        m_mean, = np.where(mtot < mtot[-1]/2.)
            
        z50[i] = zsort[m_mean][-1]
        
    return med, z50