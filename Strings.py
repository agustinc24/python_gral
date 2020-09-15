usuario=input("Introduzca su nombre de Usuario: ")
print("El nombre es:", usuario.upper())


edad=input("Intoduzca la edad:")
while(edad.isdigit()==False):
	print("Por fabor, introduzca un valor numerico")
	edad=input("Intoduzca la edad:")
	
if (int(edad)<18):
	print("No puede pasar")
else:print("Puede pasar")