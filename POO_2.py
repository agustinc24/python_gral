class coche(): 
	
	def __init__(self): #creo el metodo constructor, es el que va a dar estado inicial a los objetos
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4 #encapsule SOLO a esta variable
		self.__enmarcha=False

	def arrancar(self, arrancamos): #le agrego otro parametro ademas del self
		self.__enmarcha=arrancamos
		if (self.__enmarcha): #si no pongo nada, lo toma como True
			return "El coche esta en marcha"
		else:
			return "El coche esta parado" 
	
	def estado(self):
		print("El coche tiene ", self.__ruedas,"ruedas. Un ancho de ",self.__anchoChasis,"y un largo de ",self.__largoChasis)

miCoche=coche()
print(miCoche.arrancar(True)) #implicitamente le manda el self
miCoche.estado()

print("--------------Creo el segundo objeto--------------")

miCoche2=coche() #cree la segunda instancia
print(miCoche2.arrancar(False)) #aca no hay que poner los __ del encapsulamiento
miCoche2.__ruedas=2 #accedo a la propiedad y la modifico
miCoche2.estado()