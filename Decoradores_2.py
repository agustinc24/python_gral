def funcion_decoradora(funcion_parametro):
	def funcion_interior(*args, **kwargs):#con el *args le digo que puede recibir cualquier cantidad de parametros

		print("Vamos a realizar un calculo: ")

		funcion_parametro(*args, **kwargs) #kwargs es un argumento con clave

		print("Terminamos el calculo")

	return funcion_interior


@funcion_decoradora
def suma(num1, num2, num3):
	print(num1+num2+num3)

@funcion_decoradora
def resta(num1, num2):
	print(num1-num2)

@funcion_decoradora
def portencia(base, exponente):
	print(pow(base, exponente))

suma(7,5,8)
resta(12,10)
portencia(base=5,exponente=3) #clave=valor, son para kwargs