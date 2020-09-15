val=0
email=input("Ingrese su email: ")
arroba=email.count('@')
if (arroba==1):
	for i in email:
		if i[0]=="@" or i[-1]=="@":
			val=1		

if(val==1 and arroba==1):
		print("La dirección",email,"es valida.")
else:
	print("La dirección",email,"es invalida.")