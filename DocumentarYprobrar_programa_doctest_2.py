import math

def raizCuadrada(listaNumeros):
	"""
	La funcion devuelve una lista con la 
	raiz cuadrada de los elementos numericos
	pasados por parametros en otra lista
	
	>>> lista=[]
	>>> for i in [4, 9, 16]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	[2.0, 3.0, 4.0]
	
	>>> lista=[]
	>>> for i in [4, 9, 16, 50, 78, -90, 125]:
	...		lista.append(i)
	>>> raizCuadrada(lista)
	Traceback (most recent call last):
  		...
	ValueError: math domain error

	"""
	#con los ... es como una sangria, en vez de tab uso eso en la documentacion
	return [math.sqrt(n) for n in listaNumeros]#sqrt siempre devuelve un double

#print (raizCuadrada([9,16,25,36]))

import doctest
doctest.testmod()