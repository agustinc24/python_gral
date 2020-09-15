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

class Moto(vehiculos):
	hcaballito=""
	def caballito(self):
		self.hcaballito="Voy haciendo el caballito"
	def estado(self): #sobreescribo el estado que heredo
		print("Marca: ", self.marca, "\nModelo: ",self.modelo,"\nEn marcha: ",self.enmarcha,"\nAcelerando: ",self.acelerar,"\nFrenando: ",self.frena,"\n",self.hcaballito)

class Furgoneta(vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if(self.cargado):
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta no esta cargada"

class VElectricos():
	def __init__(self):
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True


miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()
print("---------------")
miFurgoneta=Furgoneta("Renault","Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class BicicletaElectrica(vehiculos,VElectricos): #tiene multi herencia, hereda el constructor de la primer clase que ponga
	pass

miBici=BicicletaElectrica("BMX","HQ1430")
miBici.estado()