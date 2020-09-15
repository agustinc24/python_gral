def evaluacion(nota):#declaro funcion
	valoracion="Aprobado"
	if nota<5:#el if cierra en el :
		valoracion="Suspenso"#todo lo que este identado va a ser parte de la accion o el if, identacion es el tab xd
	return valoracion
print("Programa de evaluacion de notas")
notass=input("Ingrese la nota:")

print(evaluacion(int(notass)))#casteo el valor para hacerlo int y asi funcione
