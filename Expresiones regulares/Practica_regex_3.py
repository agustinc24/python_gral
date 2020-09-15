import re

lista_nombres=['Ana', 
			'Pedro',
			'Maria',
			'Rosa',
			'Sandra',
			'Celia']


for elemeto in lista_nombres:
	if re.findall('[o-t]', elemeto): #contienen alguna letra entre la 'o' y la 't', distingue las mayusculas
		print(elemeto)

print("--------------")

lista_nombres=['Ma.1', 
			'Se1',
			'Ma2',
			'Ba1',
			'Ma:3',
			'Va1',
			'Va2',
			'Ma4',
			'Ma.5',
			'MaB',
			'Ma:C',
			'MaA']


for elemeto in lista_nombres:
	#if re.findall('Ma[^0-3]', elemeto):lo niego, busca al que no cumple con eso
	#if re.findall('Ma[0-3A-B]', elemeto):#busca del 0 al 3, y de A a B
	if re.findall('Ma[.:]', elemeto): #busca los que tenga un '.' o ':'
		print(elemeto)
