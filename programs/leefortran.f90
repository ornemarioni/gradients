PROGRAM lee_posiciones
    IMPLICIT NONE
    
    INTEGER                 :: istr, idrk, igas, NSTR, NGAS, NDRK, NTOT
    REAL*8, DIMENSION(NSTR) :: xstr, ystr, zstr, mstr
    REAL*8, DIMENSION(NGAS) :: xgas, ygas, zgas, mgas
    REAL*8, DIMENSION(NDRK) :: xdrk, ydrk, zdrk, mdrk
    REAL*8, DIMENSION(NTOT) :: xtot, ytot, ztot, mtot
    
    OPEN (90, FILE='/mnt/sersic2/omarioni/vale/hestia/str.dat', STATUS='OLD')
    OPEN (80, FILE='/mnt/sersic2/omarioni/vale/hestia/gas.dat', STATUS='OLD')
    OPEN (70, FILE='/mnt/sersic2/omarioni/vale/hestia/drk.dat', STATUS='OLD')
    
    DO i = 1, NSTR:
        READ (90,*) istr, xstr, ystr, zstr, mstr
    END DO
    
    DO i = 1, NGAS:
        READ (90,*) igas, xgas, ygas, zgas, mgas
    END DO
    
    DO i = 1, NDRK:
        READ (90,*) idrk, xdrk, ydrk, zdrk, mdrk
    END DO
    
    NTOT = NSTR + NGAS + NDRK
    
    CALL epot(0.34,mt,xt,yt,zt,n,p)