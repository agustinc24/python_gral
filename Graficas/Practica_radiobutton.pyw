from tkinter import *

root=Tk()
root.title("Radiobutton")
root.iconbitmap("peneico.ico")

varOpcion=IntVar()

def imprimir():
	if varOpcion.get()==1:
		etiqueta.config(text="Elegiste masculino bro")
	else:
		etiqueta.config(text="Elegiste femenino re mariquita bro")

Label(root, text="Genero:").pack()

Radiobutton(root, text="Masculino", variable=varOpcion, value=1, command=imprimir).pack()

Radiobutton(root, text="Femenino", variable=varOpcion, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()