FILES INFORMATION

1 - read_HESTIA_test.ipynb:
	> We have snapshots directory
    > Vemos que hay dentro de los snapshots y cómo leerlos.
	> We read the z=0 snapshot and concatenate different outputs to get position of the particles
	> Miramos que tienen adentro los archivos del FoF (para usarlo en [3])
    > Veo donde estan posicionados los halos y grupos mas masivos
    > Grafico los 3 halos mas masivos (los roto respecto del momento ang) -- Aca todavia no miro si hay particulas low-res en los halos.
    > Veo la masa de las diferentes particulas
    > Saco los 100 subhalos mas masivos con las masas y cant de particulas de cada tipo: **subhalos.dat**
    > Miro cuales de esos 100 no tienen particulas low o int-res.
    > Grafico los subhalos que no tienen particulas low/int-res **subhalos.png**
    
2 - virial_mass.ipynb
    > Leo los archivos de los subhalos, saco masas, posiciones y radios.
    > Calculo masa y radio virial de los 8 halos mas masivos que no tienen particulas low/int-res. **Mvir_Rvir.dat**
    
3 - read_HESTIA.ipynb:
	> We have snapshots directory
    > Tenemos la informacion de los grupos FoF y los subhalos dentro de cada grupo.
    > Sacamos los 10 halos mas masivos con sus posiciones.
	> We read the z=0 snapshot and concatenate different outputs to get position of the particles
	> We save the 8 most massive halos in other outputs (sin particulas low/int-res).
	> We plot the 3 most massive galaxy with sphviewer.
    > Grafico las estrellas de los 8 halos.
    > Miro que hay dentro de cada archivo de subhalo guardado.
	
4 - density_plots.ipynb:
	> Plots of mass density in stars, gas and dark matter.
    > Tengo los minimos y maximos de densidad para cada plot.
    > Guardo los plots en **'../_imagenes/mass_density/subhalo*.png'**
    > Hago los plots de densidad estelar separando en edades de las estrellas 
    > Guardo los plots en **'../_imagenes/ages_stars/starages_sh_*.png'**
    > Hago el plot **'../_imagenes/ages_stars/subhalo_000.pdf'** para el boletin de la AAA.
    
5 - metallicity_gradients.ipynb:
    > Leo los archivos de los subhalos que guarde
    > Veo que porcentage de partículas tengo con Formation Time (FT) < 0 (ver documentacion Illustris)
    > Veo cuantas particulas tienen metalicidades negativas.
    > Hago los plots de distribucion de edades y metalicidades **'../_imagenes/metallicity_ages/Rz_met_s*.png'**
    > Veo como se distribuyen radialmente las metalicidades en bines de edad
    > Hago histogramas de metalicidades y edades
    > Corroboro que los tiempos que calculo me den igual a los calculados con un paquete de astropy (a --> Gyr)
    
  
6 - ages_distribution.ipynb:
    > Veo la distribucion radial de las edades en el subhalo mas masivo en bines de edad
    > Guardo los archivos **'../_imagenes/test_ages/subh000/sh_000_age_*.png'**
    > Se puede hacer con los otros halos, esta hecho solo con el primero
    
7 - metalicidad_perfiles.ipynb
    > Calculo los perfiles radiales de metalicidad en bines de edad
    > Guardo los archivos **'../_imagenes/met_perfil/met_subh_*.png'**

8 - z50_perfiles.ipynb
    > Calculo los perfiles de z50 (Half-mass scale height) para todos los halos
    > Guardo el archivo **'../_imagenes/z50_perfil.png'**
    > Calculo los perfiles de z50 (Half-mass scale height) para todos los halos en bines de edad
    > Guardo los archivos **'../_imagenes/z50_perfil/z50_subh_*.png'**
    
9 - surface_density.ipynb
    > Calculo los perfiles radiales de densidad superficial (de masa) para todos los halos
    > Guardo el archivo **'../_imagenes/surf_density.png'**
    > Calculo los perfiles de densidad superficial en bines de masa
    > Guardo los archivos **'../_imagenes/surf_density/sd_subh_*.png'**
    
10 - circular_velocity.ipynb
    > Calculo las curvas de veloc circular para los 8 halos mas masivos
    > Guardo los archivos: (solo el 1% de las particulas)
        - **'../_data/velocity/sh*_Vtot.dat'**
        - **'../_data/velocity/sh*_Vstr.dat'**
        - **'../_data/velocity/sh*_Vgas.dat'**
        - **'../_data/velocity/sh*_Vdrk.dat'**
    > Grafico las curvas y las guardo: **'../_imagenes/velocities/Vcirc_sh_*.png'**
    > Verifico que se lean bien los archivos

11 - SFR.ipynb
    > Calculo la tasa de formacion estelar
    > Guardo el la imagen: **'../_imagenes/SFR.png'**
    
12 - abundance_matching.ipynb
    > Grafico la curva de abundance matching
    > Guardo la imagen: **'../_imagenes/Mvir_vs_Mgal.png'**
    > Me fijo cuanta es la proporcion de masa que aportan las particulas con SFT<0