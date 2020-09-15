import pickle
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

coche1=vehiculos("Mazda","MX5")
coche2=vehiculos("Volkswagen","Gol")
coche3=vehiculos("Renault","Megane")

coches=[coche1, coche2, coche3]

fichero=open("LosCoches","wb")
pickle.dump(coches, fichero)
fichero.close()
del(fichero)

ficheroApertura=open("LosCoches","rb")
misCoches=pickle.load(ficheroApertura)
ficheroApertura.close()
for c in misCoches:
	print(c.estado())