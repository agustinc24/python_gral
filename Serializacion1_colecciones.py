import pickle 
#lista_nombre=["Agustin","Meli","Juan","Alejo"]
#fichero_binario=open("Lista_nombres","wb")
#pickle.dump(lista_nombre, fichero_binario)
#fichero_binario.close()
#del(fichero_binario)

fichero=open("Lista_nombres", "rb")

lista=pickle.load(fichero)

print(lista)