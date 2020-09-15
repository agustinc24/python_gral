from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("Menu")
root.iconbitmap("peneico.ico")

def infoAdicional():
	messagebox.showinfo("Informacion perri", "Version cuarentini 2020")

def avisoLicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def salirApp():
	valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicacion?")
	if valor=="yes":
		root.destroy()


def cerrarDoc():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documento bloqueado")
	if valor==False:
		root.destroy()


barraMenu=Menu(root)
root.config(menu=barraMenu, width=450, height=300)

archivoMenu=Menu(barraMenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDoc)
archivoMenu.add_command(label="Salir", command=salirApp)

archivoEdicion=Menu(barraMenu, tearoff=0)
archivoEdicion.add_command(label="Copiar")
archivoEdicion.add_command(label="Cortar")
archivoEdicion.add_command(label="Pegar")
archivoHerramientas=Menu(barraMenu, tearoff=0)
archivoHerramientas.add_command(label="Exploid")
archivoHerramientas.add_command(label="Macros")
archivoAyuda=Menu(barraMenu, tearoff=0)
archivoAyuda.add_command(label="Licencia", command=avisoLicencia)
archivoAyuda.add_command(label="Acerca de...", command=infoAdicional)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edicion", menu=archivoEdicion)
barraMenu.add_cascade(label="Herramientas", menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda", menu=archivoAyuda)




root.mainloop()