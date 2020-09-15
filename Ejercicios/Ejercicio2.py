print("Ingrese una contraseña de al menos 8 caracteres")
contraseña=input("Ingrese la contraseña: ")
while len(contraseña)<8:
	contraseña=input("Ingrese la contraseña, debe contener al menos 8 caracteres: ")

print("Cantidad de letras: " + str(len(contraseña)))	
print("La contraseña es: "+contraseña)