import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()


#miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION = 'confeccion'")

#miCursor.execute("UPDATE PRODUCTOS SET PRECIO=350 WHERE ID=1")

miCursor.execute("DELETE FROM PRODUCTOS WHERE ID=4")


miConexion.commit()

miConexion.close()

