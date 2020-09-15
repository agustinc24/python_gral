#documentar un programa es incluir comentarios en clases, metodos, etc
#ayuda al trabajo en equipo, especialmente en apps complejas


class Areas:
	"""Esta clase calcula las areas de diferentes figuras geometricas"""
	def areaCuadrado(lado):
		"""Aca explico que hace la funcion. Calcula el area de un cuadrado
		Elevando al cuadrado el lado pasado por parametro"""
		return "El area del cuadrado es: "+ str(lado*lado)

	def areaTriangulo(base, altura):
		"""calcula el area de un triangulo utilizando los parametros base y altura"""
		return "El area del triangulo es: " +str((base*altura)/2)


#print(areaCuadrado(5))
#print(areaCuadrado.__doc__) #imprime la documentacion de esa funcion

#help(areaCuadrado) #te muestra la documentacion y algunas cosas mas

help(Areas.areaTriangulo) #si pertenece a una clase, tengo que poner primero la clase

help(Areas)