email=False

for i in [1,2,3]:
	print("Hola", end=" ")#el end es lo que aparece al final de cada printeada, en este caso un espacio

for i in "juansito@gmail.com":#recorre caracter por caracter
	if(i=="@" ):
		email=True

if email == True:
	print("Email es correcto")
else:
	print("Email incorrecto")


for i in range(5):
	print("Range")