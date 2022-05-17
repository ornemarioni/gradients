FILES INFORMATION

DOCUMENTACION AREPO : https://arepo-code.org/wp-content/userguide/snapshotformat.html
DOCUMENTACION ILLUSTRIS: https://www.tng-project.org/data/docs/specifications/

1 - read_HESTIA_test.ipynb:
	> We have snapshots directory
    > Vemos que hay dentro de los snapshots y cómo leerlos.
	> We read the z=0 snapshot and concatenate different outputs to get position of the particles
	> Miramos que tienen adentro los archivos del FoF (para usarlo en [3])
    > Veo donde estan posicionados los halos y grupos mas masivos
    > Grafico los 3 halos mas masivos (los roto respecto del momento ang) -- Aca todavia no miro si hay particulas low-res en los halos.
    > Veo la masa de las diferentes particulas
     - Esto de aca ya no es necesario porque miro los datos de Amiga con fMhires
    > Saco los 100 subhalos mas masivos con las masas y cant de particulas de cada tipo: **subhalos.dat**
    > Miro cuales de esos 100 no tienen particulas low o int-res.
    > Grafico los subhalos que no tienen particulas low/int-res **subhalos.png**
    
2 - virial_mass.ipynb
    > Leo los archivos de los subhalos, saco masas, posiciones y radios.
    > Calculo masa y radio virial de los 8 halos mas masivos que no tienen particulas low/int-res. **Mvir_Rvir.dat**
    
3 - read_HESTIA.ipynb:
	> Vemos la info de los halos adentro de los archivos de Amiga *.AHF_halos
    > Extraemos los datos necesarios del archivo (ID, Mvir, Rvir, Pos, fMhires)
    > Usando fMhires sacamos los halos que contengan particulas low-res
    > Nos quedamos los los 15 halos mas masivos.
    > Guardo los datos de estos 15 halos mas masivos **'../_data/my_halos.dat'**
	> We read the z=0 snapshot and concatenate different outputs to get position of the particles
	> We save the 15 most massive halos in other outputs (sin particulas low/int-res).
	> We plot the 3 most massive galaxy with sphviewer.
    > Grafico las estrellas de los 15 halos.
    > Miro que hay dentro de cada archivo de subhalo guardado.
	
4 - density_plots.ipynb:
	> Plots of mass density in stars, gas and dark matter. (z=0)
    > Tengo los minimos y maximos de densidad para cada plot.
    > Guardo los plots en **'../_imagenes/mass_density/subhalo*.png'**
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
    > Guardo los archivos **'../_imagenes/test_ages/127*002/sh_*_age_*.png'**
    > Se puede hacer con los otros halos, esta hecho solo con el primero
    
7 - metalicidad_perfiles.ipynb
    > Calculo los perfiles radiales de metalicidad en bines de edad
    > Guardo los archivos **'../_imagenes/met_perfil/met_subh_*.png'**
    > Calculo los perfiles radiales de metalicidad del gas

8 - z50_perfiles.ipynb
    > Calculo los perfiles de z50 (Half-mass scale height) para todos los halos
    > Guardo el archivo **'../_imagenes/z50_perfil.png'**
    > Calculo los perfiles de z50 (Half-mass scale height) para todos los halos en bines de edad
      (entre 4 y 10Gyr)
    > Guardo los archivos **'../_imagenes/z50_perfil/z50_subh_*.png'**
    > Calculo los perfiles de z50 (Half-mass scale height) para todos los halos en bines de edad
      (entre 0 y 14Gyr)
    > Guardo los archivos **'../_imagenes/z50_perfil/all_ages/z50_subh_*.png'**
    
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
    
13 - merger_tree.ipynb
    > Guardo los archivos para los 15 subhalos mas masivos a z=0 para todos los snapshots.
        - **'../_simulations/snap_*/subhalo_*.h5py'**
        - **'../simulations/snapshot_output.txt'** --> tiene la salida del guardado de archivos
    > Grafico uno de los halos para ver como quedo.
    
14 - age_star_particles.ipynb
    > Hago los plots de densidad estelar separando en edades de las estrellas 
    > Guardo los plots en **'../_imagenes/ages_stars/starages_sh_*.png'**
    > Hice un nuevo bineado (reemplace 8 por 7Gyr en realidad)
    > Guardo los plots en **'../_imagenes/ages_stars/new_bins/starages_sh_*.png'**
    > Veo que snapshots caen dentro de cada bin de edad
    > Saco los ID de las particulas que nacieron en cada bin de edades
    > Guardo '../_data/ID_partxagebin/ID_pxab_sh_*.dat' los ID de las part en cada bin de edad
    > Guardo '../_data/ID_partxagebin/npxab_sh*.dat' el num de ctas particulas nacieron en ese bin de edad.
    > Guardo '../_data/snap_sft/sft_snap_sh*.dat' el snapshot donde se formaron las part.
    > Guardo masas y posiciones de las particulas en su snapshot de formacion
        - '../_data/pos_part_age/sft_snap_sh_*.dat'
        - '../_data/pos_part_age/output_data.dat'
    > Grafico las estrellas en su tiempo de formación
        - '../_imagenes/ages_stars_ft/strages_ft_sh_*.png'

15 - time.ipynb
    > Guardo el archivo **'../_data/time.dat'** 
        - #snap    a    z    time
        
16 - age_gas_particles.ipynb
    > Me fijo que snapshot es representativo de los bines de edad
    > Elijo los snapshots 127, 103,84 y 64 para los bines 0, 4, 7, 10Gyr respectivamente
    > Guardo las posiciones y masa de las part de gas en los dif snapshots
        - '../_data/pos_gas_age/gas_pos_(<SNAP>)_sh_*.dat'
    > Grafico las particulas de gas en los diferentes snapshots
        - '../_imagenes/ages_gas/gas_ages_sh_*.png'

   - circularidad.ipynb
    > archivo viejo
    
    