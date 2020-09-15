class coche(): #establezco propiedades que van a tener los objetos que van a pertenecer a esta clase
	largoChasis=250
	anchoChasis=120
	ruedas=4
	enmarcha=False

	def arrancar(self):
		self.enmarcha=True #cambio el comportamiento
	def estado(self):
		if (self.enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche esta parado"
miCoche=coche() #instanciar una clase, una instanciacion de clase. Ejemplarice la clase, cree una instancia, es todo lo mismo xddd
print("El largo del coche es: ",miCoche.largoChasis) #veo la propiedad que especifico despues del '.'
print("El coche tiene", miCoche.ruedas, "ruedas")
miCoche.arrancar()
print(miCoche.estado())
#este programa tiene 4 propiedades y 2 comportamientos (o metodos)
