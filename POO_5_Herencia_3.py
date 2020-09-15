class Persona():
	def __init__(self, nombre, edad, lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.residencia=lugar_residencia

	def descripcion(self):
		print("Nombre:",self.nombre,"\nEdad:",self.edad,"\nResidencia:",self.residencia)

class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #le mando esto a la clase que este heredando
		self.salario=salario
		self.antiguedad=antiguedad
	def descripcion(self):
		super().descripcion()
		print("Salario:",self.salario,"\nAntiguedad:",self.antiguedad)

Manuel=Empleado(1500,15,"Manuel",55,"Colombia")
Manuel.descripcion()

print(isinstance(Manuel, Persona))#devuelve true si un objeto pertence a una clase
