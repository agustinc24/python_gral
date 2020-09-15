def areaTriangulo(base, altura):
	"""
	Calcula el area de un triangulo dadas la base y la altura
	#con los 3 > le digo que tiene que probar y justo abajo pongo el resultado que deberia de darme
	>>> areaTriangulo(3,6)
	'El area del triangulo es: 9.0'
	
	Calcula el area de un triangulo dadas la base y la altura
	#con los 3 > le digo que tiene que probar y justo abajo pongo el resultado que deberia de darme
	>>> areaTriangulo(4,5)
	'El area del triangulo es: 10.1'
	
	Calcula el area de un triangulo dadas la base y la altura
	#con los 3 > le digo que tiene que probar y justo abajo pongo el resultado que deberia de darme
	>>> areaTriangulo(9,3)
	'El area del triangulo es: 13.5'
	"""

	return "El area del triangulo es: "+str((base*altura)/2)


import doctest
doctest.testmod() # con esto hago que lo pruebe, si hace las cosas bien no va a devolver nada, si hay un error dice algo
