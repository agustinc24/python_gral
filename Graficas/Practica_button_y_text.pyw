from tkinter import *
raiz = Tk()
raiz.title("Practica de entry")
raiz.iconbitmap("peneico.ico")

miFrame=Frame(raiz)
miFrame.config(width=250, height=275)
miFrame.grid_propagate(False)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red")

cuadroContra=Entry(miFrame)
cuadroContra.grid(row=1, column=1, padx=10, pady=10)
cuadroContra.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textoComentarios=Text(miFrame, width=16, height=5)
textoComentarios.grid(row=4, column=1, padx=10, pady=10)

scrollVertical=Scrollbar(miFrame, command=textoComentarios.yview)
scrollVertical.grid(row=4, column=2, sticky="nsew")

textoComentarios.config(yscrollcommand=scrollVertical.set)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10)

contraseñaLabel=Label(miFrame, text="Password:")
contraseñaLabel.grid(row=1,column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4,column=0, sticky="e", padx=10, pady=10)

def codigoBoton():
	minombre.set("Agustin")

botonEnvio=Button(raiz, text="Enviar", command=codigoBoton)

botonEnvio.pack()

raiz.mainloop()



texto1=Label(miFrame, text="ID")
texto1.grid(row=0, column=2, padx=4, pady=4)
entry1=Entry(miFrame)
entry1.grid(row=0, column=3)

texto2=Label(miFrame, text="Nombre")
texto2.grid(row=1, column=2, padx=4, pady=4)
entry2=Entry(miFrame)
entry2.grid(row=1, column=3)

texto3=Label(miFrame, text="Password")
texto3.grid(row=2, column=2, padx=4, pady=4)
entry3=Entry(miFrame)
entry3.grid(row=2, column=3)

texto4=Label(miFrame, text="Apellido")
texto4.grid(row=3, column=2, padx=4, pady=4)
entry4=Entry(miFrame)
entry4.grid(row=3, column=3)

texto5=Label(miFrame, text="Direccion")
texto5.grid(row=4, column=2, padx=4, pady=4)
entry5=Entry(miFrame)
entry5.grid(row=4, column=3, padx=4, pady=4)

texto6=Label(miFrame, text="Comentarios")
texto6.grid(row=5, column=2, padx=4, pady=4)
entry6=Entry(miFrame)
entry6.grid(row=5, column=3)

button1=Button(miFrame, text="Create")
button1.grid(row=7, column=2)

button2=Button(miFrame, text="Read")
button2.grid(row=7, column=3)

button3=Button(miFrame, text="Update")
button3.grid(row=7, column=4)

button4=Button(miFrame, text="Delete")
button4.grid(row=7, column=6)