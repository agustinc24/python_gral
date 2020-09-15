import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor() #cursor o puntero

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miCursor.execute("INSERT INTO PRODUCTOS VALUES('Balon', 15, 'Deportes')")

miConexion.commit()




miConexion.close()