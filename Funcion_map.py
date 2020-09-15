class empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{} que trabaja como {} tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)

listaEmpleado=[
empleado("Juan", "Director",6700),
empleado("Lorenzo", "Presidente",7500),
empleado("Sara", "Administrativo",2100),
empleado("Kiko", "Secretario",2150),
empleado("Marito", "Botones",1800),
]

def calculo_comision(empleado):
	if(empleado.salario<=3000):
		empleado.salario=empleado.salario*1.03
	return empleado

listaEmpleadosComision=map(calculo_comision, listaEmpleado)

for empleado in listaEmpleadosComision:
	print(empleado)