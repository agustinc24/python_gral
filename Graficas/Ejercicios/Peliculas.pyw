from tkinter import *

root=Tk()
root.title("Peliculas")
root.iconbitmap("peneico.ico")

cont=0

def añadir(contenido):
	global cont

	liss.insert(cont,""+contenido)
	cont+=1
	pantalla.set("")

miFrame=Frame(root)
miFrame.pack(fill="both", expand="True")
miFrame.config(width="450", height="300")
miFrame.grid_propagate(False)

pantalla=StringVar()

texto=Label(miFrame, text="Escribe el titulo de una pelicula")
texto.grid(row=3, column=0, padx=5)

insertar=Entry(miFrame, textvariable=pantalla, justify="center")
insertar.grid(row=4, column=0, padx=3)

boton=Button(miFrame, text="Añadir", width=6, cursor="hand2", command=lambda:añadir(pantalla.get()))
boton.grid(row=5, column=0, padx=3)

liss=Listbox(miFrame)
liss.config(width=40, height=15)
liss.grid(row=1, rowspan=10, column=2, padx=5, pady=10)


texto2=Label(miFrame, text="Escribe el titulo de una pelicula")
texto2.grid(row=0, column=2, padx=5, pady=3)



root.mainloop()