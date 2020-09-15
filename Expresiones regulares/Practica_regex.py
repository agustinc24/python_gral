import re

cadena="Vamos a tomar merca regular en Python. Desde el culo de un enano que sabe Python"

#print(re.search("merca", cadena)

textoBuscar="Python"

'''if re.search(textoBuscar, cadena) is not None:
	print("He encontrado el texto")
else:
	print("No he encontrado el texto")'''

textoEncontrado=re.search(textoBuscar, cadena)

print(textoEncontrado.start()) #numero de caracter donde arranca el texto

print(textoEncontrado.end()) #numero de caracter donde termina el texto

print(textoEncontrado.span()) #hace ambas cosas a la vez y lo devuelve en una tupla

#------------

print(re.findall(textoBuscar, cadena)) #devuelve una lista con las veces que aparece un string que le de

