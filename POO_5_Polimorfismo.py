class Coche():
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

class Moto():
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")


def desplazamientoVehiculo(vehiculo):#va a ejecutar el metodo del objeto, el objeto en señala cual metodo accionar asiq es indistinto el que le mande, se ejecuta el propio
	vehiculo.desplazamiento()

miVehiculo=Coche()
desplazamientoVehiculo(miVehiculo)