diccionario={"Alemania":"Berlin", 1.32:"Buenos Aires", "Reino unido":25}#declaro una pareja CLAVE:VALOR
print(diccionario["Alemania"])#pongo la clave entre [] y me devuelve el valor asociado a esta
print(diccionario)#imprime todo el diccionario
diccionario["España"]="Jujuy"#añado un elemento al diccionario ya creado
print(diccionario)
diccionario["España"]="Madrid"#sobreescribe el valor ya creado
print(diccionario)
del diccionario["Alemania"]#elimino un elemento de un diccionario
print(diccionario)

tupla=["España", "Jujuy", "Algo"]#declaro una tupla
diccionario2={tupla[0]:"Madrid",tupla[1]:"altos bolitas", tupla[2]:"no se bro"}#le asigno a cada elemento de una tupla, un valor
print(diccionario2)
diccionario2={23:"Jordan", "Equipo":"Chicago", "anillos":[1991, 1992, 1993, 1996, 1997, 1998]}#le agrego como valor una tupla a una clave
print(diccionario2)

print(diccionario2.keys())#imprime los nombres de las claves
print(diccionario2.values())#imprime los valores
print(len(diccionario2))#imprime la cantidad de claves:valores