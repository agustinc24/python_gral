from tkinter import *
raiz = Tk()
raiz.title("Practica de entry")
raiz.iconbitmap("peneico.ico")

miFrame=Frame(raiz)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red")

cuadroContra=Entry(miFrame)
cuadroContra.grid(row=1, column=1, padx=10, pady=10)
cuadroContra.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion de casa:")
direccionLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

contraseñaLabel=Label(miFrame, text="Password:")
contraseñaLabel.grid(row=1,column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()
