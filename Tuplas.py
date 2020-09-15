tuplaa=("juan", 24,5,2000)#defino tupla
print(tuplaa[2])
lista=list(tuplaa)#casteo la tupla en una lista y se la asigno a una variable
print(lista)
tupli=tuple(lista)#casteo la lista en una tupla y se la asigno a una variable
print(tupli)
print("juan" in tuplaa)#devuelve true si hay un elemento en una tupla y sino devuelve false
print(tuplaa.count(13))#printea cuantas veces se repite un elemento
print(len(tuplaa))#printea cuantos elementos tiene en total una tupla
tuplaa2=("unico_elemento",)#tupla unitaria, tiene que tener la coma esa del final
print(len(tuplaa2))
nombre, dia, mes, anio = tuplaa#le asigne a cada variable que escribi, cada elemento de la tupla que cree
print(nombre, dia, anio, mes)#lokura