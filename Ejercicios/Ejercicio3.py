email=input("Ingrese un email: ")
arrob=0
punto=0
for i in email:
	if i == "@":
		arrob = arrob+1
	if i == ".":
		punto=punto+1

if arrob == 1 and punto>=1:
	print("Email correcto.")
else:
	print("Email incorrecto.")