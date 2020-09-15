from tkinter import *
from tkinter import messagebox
import sqlite3
import ctypes #para setear de icono mi .ico

myappid = 'con.esto.puedo.tener.mi.icono' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid) #ahora si lo puse


raiz = Tk()
raiz.title("C . R . U . D")
raiz.iconbitmap("peneico.ico")

barraMenu=Menu(raiz)
raiz.config(menu=barraMenu, width=450, height=400)


#----------------------------------Funciones de menu----------------------------------
def salirApp():
	valor=messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?")
	if valor==True:
		raiz.destroy()


def abrirConexion():
	miConexion=sqlite3.connect("Registro_sumarios")
	miCursor=miConexion.cursor()
	try:
		miCursor.execute('''
			CREATE TABLE datos_sumarios (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(15), 
			PASSWORD VARCHAR(15),
			APELLIDO VARCHAR(15),
			DIRECCION VARCHAR(15),
			COMENTARIOS VARCHAR(50) )
			''')
		messagebox.showinfo("BBDD", "Base de dato creada correctamente.\nRecuerde que el campo ID solo debe llenarse cuando se busque un registro.")
	except sqlite3.OperationalError:
		messagebox.showwarning("¡Atención!", "Base de datos ya existe.\nRecuerde que el campo ID solo debe llenarse cuando se busque un registro.")


def crearRegistro(nombre, passw, apellido, direcc):
	miConexion2=sqlite3.connect("Registro_sumarios")
	miCursor2=miConexion2.cursor()
	comentario=entryComent.get("1.0", "end") #leo el texto del widget text
	if nombre != "" and passw != "" and apellido !="" and entryComent.compare("end-1c", "==", "1.0") == False and direcc !="": #con la linea del entryComent veo que no este vacio
		lista=(nombre, passw, apellido, direcc, comentario)
		crearRegis=miCursor2.execute("INSERT INTO datos_sumarios VALUES ( NULL,?,?,?,?,?)", lista)
		miConexion2.commit()
		vaciarCampos()
		if crearRegis:
			messagebox.showinfo("BBDD", "Registro creado correctamente.")
	else:
		messagebox.showinfo("BBDD", "Todos los campos deben estar completos.")


def leerRegistro(id, nombre, passw, apellido, direcc):
	miConexion4=sqlite3.connect("Registro_sumarios")
	miCursor4=miConexion4.cursor()
	miCursor4.execute("SELECT * FROM datos_sumarios WHERE ID=(?)",str(id))
	varLectura=miCursor4.fetchall()
	if nombre != "" and passw != "" and apellido !="" and entryComent.compare("end-1c", "==", "1.0") == False and direcc !="":
			vaciarCampos()
	for i in varLectura:
		pantallaID.set(""+str(i[0]))
		pantallaNombre.set(""+i[1])
		pantallaPassword.set(""+i[2])
		pantallaApellido.set(""+i[3])
		pantallaDirecc.set(""+i[4])
		entryComent.insert("1.0", i[5])


def updateRegistro(id):
	miConexion5=sqlite3.connect("Registro_sumarios")
	miCursor5=miConexion5.cursor()
	comentario=entryComent.get("1.0", "end")
	miCursor5.execute("SELECT * FROM datos_sumarios")
	nombre=pantallaNombre.get()
	passw=pantallaPassword.get()
	apellido=pantallaApellido.get()
	direcc=pantallaDirecc.get()
	
	lista=(nombre, passw, apellido, direcc, comentario, str(id))
	lista2=(nombre, id)
	miCursor5.execute("UPDATE datos_sumarios SET NOMBRE_USUARIO=(?), PASSWORD=(?), APELLIDO=(?), DIRECCION=(?), COMENTARIOS=(?) WHERE ID =(?)",lista )
	miConexion5.commit()
	


def deleteRegistro(id):
		miConexion3=sqlite3.connect("Registro_sumarios")
		miCursor3=miConexion3.cursor()
		print(id)
		eliminarRegis=miCursor3.execute("DELETE FROM datos_sumarios WHERE ID=(?)",str(id)) #tuve que castear el id a str para que se borre
		miConexion3.commit()
		vaciarCampos()
		if eliminarRegis:
			messagebox.showinfo("BBDD", f"Registro {id} eliminado correctamente.")
	

def vaciarCampos():
	pantallaID.set("")
	pantallaNombre.set("")
	pantallaPassword.set("")
	pantallaApellido.set("")
	pantallaDirecc.set("")
	entryComent.delete("1.0", "end")


#----------------------------------Declaracion de pantallas----------------------------------
pantallaID=IntVar()
pantallaID.set("")
pantallaNombre=StringVar()
pantallaPassword=StringVar()
pantallaApellido=StringVar()
pantallaDirecc=StringVar()


#----------------------------------Menu----------------------------------
menuBBDD=Menu(barraMenu, tearoff=0)
menuBBDD.add_command(label="Conectar", command=abrirConexion)
menuBBDD.add_separator()
menuBBDD.add_command(label="Salir", command=salirApp)

menuBorrar=Menu(barraMenu, tearoff=0)
menuBorrar.add_command(label="Borrar campos", command=vaciarCampos)
menuCRUD=Menu(barraMenu, tearoff=0)
menuCRUD.add_command(label="Create",command=lambda:crearRegistro(pantallaNombre.get(), pantallaPassword.get(), pantallaApellido.get(), pantallaDirecc.get() ))
menuCRUD.add_command(label="Read", command=lambda:leerRegistro(pantallaID.get(),pantallaNombre.get(), pantallaPassword.get(), pantallaApellido.get(), pantallaDirecc.get() ))
menuCRUD.add_command(label="Update", command=lambda:updateRegistro(pantallaID.get()))
menuCRUD.add_command(label="Delete", command=lambda:deleteRegistro(pantallaID.get() ))
menuAyuda=Menu(barraMenu, tearoff=0)
menuAyuda.add_command(label="Licencia")
menuAyuda.add_command(label="Acerca de...")


barraMenu.add_cascade(label="BBDD", menu=menuBBDD)
barraMenu.add_cascade(label="Borrar", menu=menuBorrar)
barraMenu.add_cascade(label="CRUD", menu=menuCRUD)
barraMenu.add_cascade(label="Ayuda", menu=menuAyuda)


#----------------------------------Frame superior----------------------------------
frameSup=Frame(raiz)
frameSup.pack()

#----------------------------------Entrys----------------------------------
entryID=Entry(frameSup, textvariable=pantallaID, justify="center")
entryID.grid(row=0, column=1, padx=10, pady=10)

entryPass=Entry(frameSup, textvariable=pantallaPassword, justify="center")
entryPass.grid(row=2, column=1, padx=10, pady=10)
entryPass.config(show="*")

entryNombre=Entry(frameSup, textvariable=pantallaNombre, justify="center")
entryNombre.grid(row=1, column=1, padx=10, pady=10)

entryApellido=Entry(frameSup, textvariable=pantallaApellido, justify="center")
entryApellido.grid(row=3, column=1, padx=10, pady=10)

entryDirecc=Entry(frameSup, textvariable=pantallaDirecc, justify="center")
entryDirecc.grid(row=4,column=1,padx=10, pady=10)

entryComent=Text(frameSup, width=16, height=5)
entryComent.grid(row=5, column=1, padx=10, pady=10)

scrollVertical=Scrollbar(frameSup, command=entryComent.yview)
scrollVertical.grid(row=5, column=2, sticky="nsew")

entryComent.config(yscrollcommand=scrollVertical.set)


#----------------------------------Texts----------------------------------
textoID=Label(frameSup, text="ID")
textoID.grid(row=0,column=0, sticky="e", padx=10, pady=10)

textoNombre=Label(frameSup, text="Nombre")
textoNombre.grid(row=1,column=0, sticky="e", padx=10, pady=10)

textoPass=Label(frameSup, text="Password")
textoPass.grid(row=2,column=0, sticky="e", padx=10, pady=10)

textoApellido=Label(frameSup, text="Apellido")
textoApellido.grid(row=3,column=0, sticky="e", padx=10, pady=10)

textoDirecc=Label(frameSup, text="Direccion")
textoDirecc.grid(row=4,column=0, sticky="e", padx=10, pady=10)

textoComent=Label(frameSup, text="Comentarios")
textoComent.grid(row=5,column=0, sticky="e", padx=10, pady=10)


#----------------------------------Frame inferior----------------------------------
frameInf=Frame()
frameInf.pack()


#----------------------------------Botones----------------------------------
botonCreate=Button(frameInf, text="Create", command=lambda:crearRegistro(pantallaNombre.get(), pantallaPassword.get(), pantallaApellido.get(), pantallaDirecc.get() ) )
botonCreate.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonRead=Button(frameInf, text="Read", command=lambda:leerRegistro(pantallaID.get(),pantallaNombre.get(), pantallaPassword.get(), pantallaApellido.get(), pantallaDirecc.get() ))
botonRead.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonUpdate=Button(frameInf, text="Update", command=lambda:updateRegistro(pantallaID.get()))
botonUpdate.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonDelete=Button(frameInf, text="Delete", command=lambda:deleteRegistro(pantallaID.get() ))
botonDelete.grid(row=0,  column=3, sticky="e", padx=10, pady=10)


raiz.mainloop()