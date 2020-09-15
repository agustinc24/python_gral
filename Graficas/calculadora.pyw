from tkinter import *
root=Tk()
root.title("Calculadora")
root.iconbitmap("peneico.ico")
root.config(bg="#2DCCD3")

miFrame=Frame(root)
miFrame.config(bg="#2DCCD3")
miFrame.pack()

operacion=""
reset_pantalla=False
resultado=0

numeroPantalla=StringVar()

#------Pulsaciones teclado--------

def numeroPulsado(num):

	global operacion

	global reset_pantalla

	if reset_pantalla!=False:

		numeroPantalla.set(num)

		reset_pantalla=False

	else:
	
		numeroPantalla.set(numeroPantalla.get() + num)

#------Funcion suma--------

def suma(num):
	global operacion

	global resultado

	global reset_pantalla

	resultado+=float(num) #resultado=resultado+int(num)

	operacion="suma"

	reset_pantalla=True

	numeroPantalla.set(resultado)

#------Funcion restar--------

num1=0

contador_resta=0

def restar(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=float(num)

		resultado=num1

	else:

		if contador_resta==1:

			resultado=num1-float(num)

		else:

			resultado=float(resultado)-float(num)	

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()


	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla
	
	if contador_divi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_divi=contador_divi+1

	operacion="division"

	reset_pantalla=True

#------Funcion igual--------

def igual():

	global resultado

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi
	

	if operacion=="suma":

		numeroPantalla.set(resultado+float(numeroPantalla.get()))

		resultado=0

	elif operacion=="resta":

		numeroPantalla.set(float(resultado)-float(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(float(resultado)*float(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(float(resultado)/float(numeroPantalla.get()))

		resultado=0

		contador_divi=0

#------Funcion multiplicar--------

contador_multi=0

def multiplica(num):

	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla
	
	if contador_multi==0:

		num1=float(num)
		
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*float(num)

		else:

			resultado=float(resultado)*float(num)	

		numeroPantalla.set(resultado)
		
		resultado=numeroPantalla.get()


	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True

#------Funcion borrar--------

def borrar():
	global resultado
	resultado=0
	operacion=""
	numeroPantalla.set(resultado)

#------pantalla-------
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, pady=3, padx=3, columnspan=5, sticky="nsew")
pantalla.config(bg="black", fg="#03f943", justify="right")

#------fila 1--------

boton7=Button(miFrame, text="7", width=3, fg="white", command=lambda:numeroPulsado("7"))
boton7.config(bg="#67A9AC")
boton7.grid(row=2, column=1, pady=3, padx=3)
boton8=Button(miFrame, text="8", width=3, fg="white", command=lambda:numeroPulsado("8"))
boton8.config(bg="#67A9AC")
boton8.grid(row=2, column=2, pady=3, padx=3)
boton9=Button(miFrame, text="9", width=3, fg="white", command=lambda:numeroPulsado("9"))
boton9.config(bg="#67A9AC")
boton9.grid(row=2, column=3, pady=3, padx=3)
botonDiv=Button(miFrame, text="/", width=3, fg="white", command=lambda:divide(numeroPantalla.get()))
botonDiv.config(bg="#67A9AC")
botonDiv.grid(row=2, column=4, pady=3, padx=3)

#------fila 2--------

boton4=Button(miFrame, text="4", width=3, fg="white", command=lambda:numeroPulsado("4"))
boton4.config(bg="#67A9AC")
boton4.grid(row=3, column=1, pady=3, padx=3)
boton5=Button(miFrame, text="5", width=3, fg="white", command=lambda:numeroPulsado("5"))
boton5.config(bg="#67A9AC")
boton5.grid(row=3, column=2, pady=3, padx=3)
boton6=Button(miFrame, text="6", width=3, fg="white", command=lambda:numeroPulsado("6"))
boton6.config(bg="#67A9AC")
boton6.grid(row=3, column=3, pady=3, padx=3)
botonMult=Button(miFrame, text="x", width=3, fg="white", command=lambda:multiplica(numeroPantalla.get()))
botonMult.config(bg="#67A9AC")
botonMult.grid(row=3, column=4, pady=3, padx=3)

#------fila 3--------

boton1=Button(miFrame, text="1", width=3, fg="white", command=lambda:numeroPulsado("1"))
boton1.config(bg="#67A9AC")
boton1.grid(row=4, column=1, pady=3, padx=3)
boton2=Button(miFrame, text="2", width=3, fg="white", command=lambda:numeroPulsado("2"))
boton2.config(bg="#67A9AC")
boton2.grid(row=4, column=2, pady=3, padx=3)
boton3=Button(miFrame, text="3", width=3, fg="white", command=lambda:numeroPulsado("3"))
boton3.config(bg="#67A9AC")
boton3.grid(row=4, column=3, pady=3, padx=3)
botonRest=Button(miFrame, text="-", width=3, fg="white", command=lambda:restar(numeroPantalla.get()))
botonRest.config(bg="#67A9AC")
botonRest.grid(row=4, column=4, pady=3, padx=3)

#------fila 4--------

boton0=Button(miFrame, text="0", width=3, fg="white", command=lambda:numeroPulsado("0"))
boton0.config(bg="#67A9AC")
boton0.grid(row=5, column=2, pady=3, padx=3)
botonComa=Button(miFrame, text=",", width=3, fg="white", command=lambda:numeroPulsado("."))
botonComa.config(bg="#67A9AC")
botonComa.grid(row=5, column=1, pady=3, padx=3)
botonIgual=Button(miFrame, text="c", width=3, fg="white", command=lambda:borrar())
botonIgual.config(bg="#67A9AC")
botonIgual.grid(row=5, column=3, pady=3, padx=3)
botonSum=Button(miFrame, text="+", width=3, fg="white", command=lambda:suma(numeroPantalla.get()))
botonSum.config(bg="#67A9AC")
botonSum.grid(row=5, column=4, pady=3, padx=3)
botonSum=Button(miFrame, text="=", width=3, fg="white", command=lambda:igual())
botonSum.config(bg="#67A9AC")
botonSum.grid(row=2, column=5, pady=3, padx=3, rowspan=4,sticky="nsew")






root.mainloop()