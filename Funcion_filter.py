'''def numero_par(num):
	if num % 2==0:
		return True

numeros=[18,17,25,24,29,65,62]

print(list(filter(numero_par,numeros)))'''

#numeros=[18,17,25,24,29,65,62]
#print(list(filter(lambda num_par: num_par%2==0,numeros)))

class empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

listaEmpleado=[
empleado("Juan", "Director",75000),
empleado("Lorenzo", "Presidente",85000),
empleado("Sara", "Administrativo",25000),
empleado("Kiko", "Secretario",27000),
empleado("Marito", "Botones",21000),

]

salarios_altos=filter(lambda empleado:empleado.salario>50000, listaEmpleado)

for empleado_salario in salarios_altos:
	print(empleado_salario)