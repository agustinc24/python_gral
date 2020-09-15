def generaPares(limite):
	num=1
	
	while  num<limite:
		yield num*2#el generador
		num=num+1

devuelvePares=generaPares(10)

print(next(devuelvePares))#muestra la siguiente iteracion

print("Mas codigo")

print(next(devuelvePares))#no importa donde lo llame, queda en suspension

print("Mas codigo")

print(next(devuelvePares))#y sigue mostrando desde donde se quedo
