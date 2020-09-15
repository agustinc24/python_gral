lista=["Agustin", 25, "Meli", 78.98]
print(lista[:])#printeo todo
print(lista[2])#printeo solo el tercer elemento
print(lista[-3])#empieza desde el final a contar(el -1 es el ultimo)
print(lista[0:3])#imprime desde el 0 hasta el 3, excluye al ultimo
print(lista[:3])#sobreentiende que vas desde el principio hasta el 3 y lo excluye
print(lista[2:])#sobreentiende que vas desde el segundo hasta el final
lista.append("Culito")#agrega un elemento al final del array
print(lista[:])
lista.insert(3,"Algo")#agrego un elemento en la posicion que yo le indique
print(lista[:])
lista.extend(["Pito","Algo",False])#le concateno otra lista al final
print(lista[:])
print(lista.index("Meli"))#printea en que posicion esta el elemento que le indiqueb, si se repite un elemento devuelve la primera vez que aparece
print("Meli" in lista)#printea "true" si un elemento aparece en la lista que le diga o "false" si no esta
lista.remove("Agustin")#elimina el elemento que le indique
print(lista[:])
lista.pop()
print(lista[:])


lista2=["Jujuy", "Alpargata"]
lista3=lista+lista2#concatena lista y lista2
print(lista3)

lista4=["hola", "holanda"]*  2 #repite la lista las veces que le indique
print(lista4)