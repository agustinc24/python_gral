from io import open

archivo_texto=open("archivo.txt","r")

archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())

archivo_texto=open("archivo.txt","r+") #lectura y escritura
#print(archivo_texto.readlines())
lista_texto=archivo_texto.readlines();
lista_texto[1]="Te re cabio gato ahora mando yo en esta linea \n"

archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()