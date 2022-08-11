import numpy as np
import bines2

#----------------------------------------------------------------------
# Half-mass scale height
#----------------------------------------------------------------------
def HMSH(R,z,m,nbin):
    
    med, nodos = bines2.rbin1(R, nbin)
    
    z50 = np.zeros(nbin)+1e-10
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]) & (z>0))
        
        if len(mask) == 0:
            # print('Me falta un bin! (z50)')
            continue
        
        zorder = np.argsort(z[mask])
        
        zsort = z[mask][zorder]
        msort = m[mask][zorder]
        
        mtot   = np.cumsum(msort)
        m_mean, = np.where(mtot < mtot[-1]/2.)
            
        z50[i] = zsort[m_mean][-1]
        
    return med, z50

#----------------------------------------------------------------------
def HMSH_log(R,z,m,nbin,nodo_min=np.log10(0.2)):
    
    if len(R)!=len(z) or len(R)!=len(m) or len(z)!=len(m):
        raise ValueError('vectors must have the same length')
        
    nodos = np.logspace(nodo_min,np.log10(R.max()),nbin+1)
    
    med = nodos[:-1] + np.diff(nodos)/2.
    
    z50 = np.ones(nbin)*np.nan
    p25 = np.ones(nbin)*np.nan
    p75 = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]) & (z>0))
        
        if (len(mask) == 0 or len(mask) == 1):
            # print('Me falta un bin! (z50)')
            continue
        
        zorder = np.argsort(z[mask])
        
        zsort = z[mask][zorder]
        msort = m[mask][zorder]
        
        mtot   = np.cumsum(msort)
        m_mean, = np.where(mtot < mtot[-1]/2.)
        # print(len(z[mask]))
        if (len(m_mean)==0 or len(m_mean)==1):
            # print('Me falta un bin! (z50)')
            continue

        z50[i] = zsort[m_mean][-1]
     
        p25[i],p75[i] = np.percentile(zsort,[25,75])
        
    return med, z50, nodos, p25, p75

#--------------------------------------------------------------------

def HMSH_log_a(R,z,m,age,nbin,nodo_min=np.log10(0.2)):
    
    if len(R)!=len(z) or len(R)!=len(m) or len(z)!=len(m) or len(R)!=len(age) or len(z)!=len(age) or len(m)!=len(age):
        raise ValueError('vectors must have the same length')
    
    nodos = np.logspace(nodo_min,np.log10(R.max()),nbin+1)
    
    med = nodos[:-1] + np.diff(nodos)/2.
    
    z50 = np.ones(nbin)*np.nan
    charac_age = np.ones(nbin)*np.nan
    p25 = np.ones(nbin)*np.nan
    p75 = np.ones(nbin)*np.nan
    
    for i in range(nbin):
        
        mask, = np.where((R < nodos[i+1]) & (R > nodos[i]) & (z>0))
        
        if (len(mask) == 0 or len(mask) == 1):
            # print('Me falta un bin! (z50)')
            continue
        
        zorder = np.argsort(z[mask])
        
        zsort = z[mask][zorder]
        msort = m[mask][zorder]
        
        mtot   = np.cumsum(msort)
        m_mean, = np.where(mtot < mtot[-1]/2.)
        
        if (len(m_mean)==0 or len(m_mean)==1):
            # print('Me falta un bin! (z50)')
            continue

        z50[i] = zsort[m_mean][-1]
        charac_age[i] = np.median(age[mask])
        p25[i],p75[i] = np.percentile(zsort,[25,75])
        
    return med, z50, charac_age, nodos, p25, p75