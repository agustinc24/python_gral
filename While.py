import math
edad=int(input("Ingrese su edad: "))
while edad<0 or edad>100:
	print("La cagaste brou")
	edad=int(input("Ingrese tu edad bien pajero: "))	
print("Sabes hace cuantos años les cagaste la vida a tus viejos? Bueno, hace: "+str(edad))

print("Ahora podes calcular una raiz cuadrada")
numero=int(input("Introduce un numero: "))

while numero<0:
	print("No se puede hallar la raiz de un numero negativo")
	numero=int(input("Introduce un numero: "))

solucion=math.sqrt(numero)#math.sqrt es para hallar la raiz cuadrada
print("La raiz cuadrada de " + str(numero) +" es " + str(solucion))