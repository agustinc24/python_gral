print("Asignaturas optativas 2020")
print("Informatica gráfica - Pruebas de software - Usabilidad y accesibilidad")
opcion=input("Escribe la asignatura escogida: ")
asignatura=opcion.lower()#casteo lo que entre y lo pongo en minusculas
if asignatura in ("informatica gráfica", "pruebas de software", "usabilidad y accesibilidad"):#el in evalua si lo que entre esta entre las opciones que le de como validas
	print("Asignatura escogida: " + asignatura)
else:
	print("La asignatura escogida no esta contemplada")
