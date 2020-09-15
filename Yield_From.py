def devciudades(*ciudades):#con el asterisco le digo que va a recibir x cantidad de elementos y que va a recibirlos en forma de tupla
	for elemento in ciudades:
		#for subElemento in elemento:
			yield from elemento

ciudades_devueltas=devciudades("Madrid","Bacelona", "Castelar", "Moron")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

