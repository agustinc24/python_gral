for letra in "Python":
	if letra == "h":
		continue#salta a la siguiente iteracion
	print("Viendo la letra: " + letra)

email=input("Introduce tu email: ")
for i in email:
	if i == "@":
		arroba=True
		break;

else:#es un else del for
	arroba=False

print(arroba)