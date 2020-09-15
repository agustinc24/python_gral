import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor() #cursor o puntero

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")


#variosProductos=[
#("Camiseta", 10, "Deportes"),
#("Jarron", 90, "Ceramica"),
#("Camion", 20, "Jugueteria")
#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS WHERE PRECIO=10")

varLectura=miCursor.fetchall()

for producto in varLectura:

	print("Articulo:", producto[0],"Seccion:",producto[2],"\nPrecio:",producto[1])


miConexion.commit()




miConexion.close()