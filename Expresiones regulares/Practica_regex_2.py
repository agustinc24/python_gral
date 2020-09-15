import re

lista_nombres=['Sandra Gomez', 
			'Maria Martin',
			'Sandra Lopez',
			'Santiago Martin']


for elemeto in lista_nombres:
	if re.findall('^Sandra', elemeto): #busca el que empieze con lo que le diga gracias al ^
		print(elemeto)

print("-----------------")

for elemeto in lista_nombres:
	if re.findall('Martin$', elemeto): #busca el que termine con lo que le diga gracias al $
		print(elemeto)

print("-----------------")

lista_nombres=['http://pildorasinformaticasenespaña.es', 
			'ftp://pildorasinformaticas.es',
			'http://pildorasinformaticas.com',
			'ftp://pildorasinformaticasenespaña.com']


for elemeto in lista_nombres:
	if re.findall('es$', elemeto):
		print(elemeto)

print("-----------------")

for elemeto in lista_nombres:
	if re.findall('[ñ]', elemeto): #devuelve donde este la ñ gracias a los []
		print(elemeto)

print("-----------------")

lista_nombres=['hombres', 
			'mujeres',
			'niños',
			'niñas']


for elemeto in lista_nombres:
	if re.findall('niñ[oa]s', elemeto): #busca con la O o con la A
		print(elemeto)

print("-----------------")

lista_nombres=['hombres', 
			'mujeres',
			'camión',
			'camion']


for elemeto in lista_nombres:
	if re.findall('cami[oó]n', elemeto): #busca la O con y sin tilde
		print(elemeto)