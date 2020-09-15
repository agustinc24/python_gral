print("Programa de becas 2020")
distancia=int(input("Introduce la distancia en km: "))
print(distancia)
hermanos=int(input("Introduce la cantidad de hermanos: "))
print(hermanos)
salario=int(input("Introduce el salario anual bruto: "))
print(salario)

if distancia>40 and hermanos >2 or salario <=20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")