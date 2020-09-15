import re

nombre1="Sandra Lopez"
nombre2="Antonio Gomez"
nombre3="sandra Lopez"

'''if re.match("Sandra", nombre2): #busca coincidencias al principio de una cadena, distingue mayusculas
	print("Hemos encontrado el nombre")
else:
	print("No lo encontre")'''

if re.match("sandra", nombre3, re.IGNORECASE):#con el 3 argumento hago qu edeje de ser case sensitive
	print("Hemos encontrado el nombre")
else:
	print("No lo encontre")

print("------------------")

nombre1="Jara Lopez"
nombre2="Antonio Gomez"
nombre3="Lara Lopez"

if re.match(".ara", nombre3, re.IGNORECASE):#Busca un caracter X y despues 'ara'
	print("Hemos encontrado el nombre")
else:
	print("No lo encontre")


print("------------------")

cadena1="Jara Lopez"
cadena2="384683456"
cadena3="a35168325"

if re.match("\d", cadena2): #busca si hay un numero al principio
	print("Hemos encontrado el numero")
else:
	print("No lo encontre")

print("------------------")

nombre1="Jara Lopez"
nombre2="Antonio Gomez"
nombre3="Lara Lopez"

if re.search("Lopez", nombre3):#search busca en cualquier punto, tambien admite el IGNORECASE
	print("Hemos encontrado el nombre")
else:
	print("No lo encontre")


print("------------------")

codigo1="qwfiuhsiuldfuisdnfansdf71asdjfnalidfna"
codigo2="jkasndjfkads71 ajsnfajsdnf nasdkfna kdnfkadnfkjandfk"
codigo3="asdf kjadsf jasnd fnasdkjfnalksjdnfakljsdnf klajsndfkj"

if re.search("71", codigo2): #devuelve true o false
	print("Hemos encontrado el nombre")
else:
	print("No lo encontre")