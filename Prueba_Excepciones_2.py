import math

def evaluaEdad(edad):
	if edad<0:
		raise TypeError("No se permiten edades negativas") #creo un tipo de error y ejecuta el msj que le ponga yo 

	if edad<20:
		return "Eres muy joven"
	elif edad<40:
		return "Eres joven"
	elif edad<65:
		return"Eres maduro"
	elif edad<100:
		return "Cuidate..."
op2=(int(input("Ingrese una edad: ")))
print(evaluaEdad(op2))


def calcularaiz(num1):
	if num1<0:
		raise ValueError ("El numero no puede ser negativo")
	else:
		return math.sqrt(num1)

op1=(int(input("Ingrese un numero para calcular su raiz: ")))
try:
	print(calcularaiz(op1))
except ValueError as ErrorDeNumeroNegativo: #Hago que si sale un valueError me tire el msj que pongo aca abajo
	print(ErrorDeNumeroNegativo)
print("Algo")