MODULE energia
    IMPLICIT NONE
    CONTAINS
    
    
!Calcula la energia potencial de cada una de las particulas
!eps = long de softening [kpc]
!m = masas [Msol]
!x,y,z = posiciones [kpc]
!p = potencial (salida) [Msol (km/s)^2]

    SUBROUTINE epot(eps,m,x,y,z,n,p)
    
    USE OMP_LIB
    
    INTEGER, INTENT (IN)    :: n
    REAL(8), INTENT (IN)    :: x(n), y(n), z(n), m(n), eps
    REAL(8), INTENT (OUT)   :: p(n)
!f2py INTENT (HIDE)         :: n
!f2py INTENT (IN)           :: x, y, z , m, eps
!f2py INTENT (OUT)          :: p
    REAL, PARAMETER         :: G = 4.299e-6 !!!!kpc (km/s)^2 Msol^-1
!!! REAL(8), PARAMETER      :: G = 6.674e-11
    REAL(8)                 :: aux, dist, dx, dy, dz
    INTEGER                 :: i, j      
       
    DO i = 1, n  
       p(i) = 0.
    END DO
    
!!!!!CALL OMP_SET_NUM_THREADS(48)
!$OMP PARALLEL DEFAULT(NONE) &
!$OMP SHARED (n,x,y,z,eps,m,p) &
!$OMP PRIVATE(i,j,dx,dy,dz,dist,aux)
!$OMP DO SCHEDULE(DYNAMIC)

    DO i = 1, n
        DO j = 1, n
            dx = x(j)-x(i)
            dy = y(j)-y(i)
            dz = z(j)-z(i)
            dist = sqrt(dx**2 + dy**2 + dz**2 + eps**2)
            IF (i /= j) THEN     
                   aux = G*m(i)*m(j) / dist    
                   p(i) = aux + p(i)
            END IF
        END DO
    END DO
    
!$OMP END DO
!$OMP END PARALLEL

    END SUBROUTINE
END MODULE