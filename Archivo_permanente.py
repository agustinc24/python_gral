import pickle

class Persona:
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre",self.nombre)
	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class ListaPersonas:
	personas=[]
	def __init__(self):
		listadepersonas=open("FicheroExterno","ab+")
		listadepersonas.seek(0)
		try:
			self.personas=pickle.load(listadepersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero esta vacio")
		finally:
			listadepersonas.close()
			del(listadepersonas)


	def agregarPersona(self, p):
		self.personas.append(p)
		self.guardarPersonasEnFicheroExterno()
	def mostrarPersonas(self):
		for scasc in self.personas:
			print(scasc)

	def guardarPersonasEnFicheroExterno(self):
		listadepersonas=open("FicheroExterno", "wb")
		pickle.dump(self.personas, listadepersonas)
		listadepersonas.close()
		del(listadepersonas)
	def mostrarInfoFicheroExterno(self):
		print("La informacion del fichero externo es la siguiente:")
		for p in self.personas:
			print(p)
miLista=ListaPersonas()

p=Persona("Sandra","Femenino", 28)
miLista.agregarPersona(p)
p=Persona("Juan","Masculino", 18)
miLista.agregarPersona(p)
p=Persona("Melina","Femenino", 53)
miLista.agregarPersona(p)
miLista.mostrarInfoFicheroExterno()