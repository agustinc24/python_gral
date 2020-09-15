#Funciones que a su vez añaden funcionalidades a otras funciones
'''Estructura:
		3 funciones (A, B y C) donde A recibe como parametro a B para devolver C
		Un decorador devuelve una funcion
		ej: def funcion_decorador(A)(funcion_parametro(B)):
				def funcion_interna(C)():
					#codigo de la funcion interna
				return funcion_interna'''

def funcion_decoradora(funcion_parametro):
	def funcion_interior():
		#Acciones adicionales que decoran xdxd

		print("Vamos a realizar un calculo: ")

		funcion_parametro()

		#Acciones adicionales que decoran xdxd 2.0
		print("Terminamos el calculo")

	return funcion_interior


@funcion_decoradora #decora a suma
def suma():
	print(15+20)

@funcion_decoradora #decora a resta
def resta():
	print(30-10)

suma()
resta()