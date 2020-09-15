class vehiculos():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelerar=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelerar=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelerar,"\nFrenando: ",self.frena)

class Moto(vehiculos): #creo una clase nueva y entre () de la clase que quiero que herede cosas
		pass

miMoto=Moto("Honda", "CBR")
miMoto.arrancar()
miMoto.estado()