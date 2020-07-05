import numpy as np

path = '/mnt/sersic2/omarioni/vale/hestia/'

STR = np.loadtxt(path+'str.dat')
xstr = STR[:,1]
ystr = STR[:,2]
zstr = STR[:,3]
mstr = STR[:,4]

GAS = np.loadtxt(path+'gas.dat')
xgas = GAS[:,1]
ygas = GAS[:,2]
zgas = GAS[:,3]
mgas = GAS[:,4]

DRK = np.loadtxt(path+'drk.dat')
xdrk = DRK[:,1]
ydrk = DRK[:,2]
zdrk = DRK[:,3]
mdrk = DRK[:,4]

xt = np.concatenate([xstr, xgas, xdrk])    
yt = np.concatenate([ystr, ygas, ydrk])
zt = np.concatenate([zstr, zgas, zdrk])
mt = np.concatenate([mstr, mgas, mdrk])

from potential import*
pot = energia.epot(0.34,mt,xt,yt,zt)

path2 = '/home/omarioni/gradients/_data/'
np.savetxt(path2+'subh_000_potential.dat',pot,fmt='%12.8f')
