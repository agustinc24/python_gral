def divide():
	try:#trata de hacer esto
		op1=(float(input("Introduce el primer numero: ")))
		op2=(float(input("Introduce el segundo numero: ")))
		print("La division es: " + str(op1/op2))
	except ValueError:#si falla por este error, ejecuta esto
		print("El valor introducido es erroneo")
	except ZeroDivisionError:#si falla por este otro error, ejecuta estp
		print("No se puede divir entre 0")
	print("Calculo finalizado")

divide()