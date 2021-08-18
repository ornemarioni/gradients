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
    > Veo que porcentage de partículas tengo con Formation Time (FT) menor que cero (estas son celdas de gas o algo asi, ver documentacion Illustris)
    > Hago los plots de distribucion de edades y metalicidades **'../_imagenes/metallicity_ages/Rz_met_s*.png'**
    

	