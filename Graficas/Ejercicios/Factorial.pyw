from tkinter import *

root=Tk()
root.title("Factorial")
root.iconbitmap("peneico.ico")


def restar(num):
	num-=1
	pantalla.set(num)

def sumar(num):
	num+=1
	pantalla.set(num)

def factorial(num):
	total=1
	while num>1:
		total*=num
		num-=1

	pantalla2.set(total)

pantalla=IntVar()
pantalla.set(1)

pantalla2=IntVar()
pantalla2.set(1)
frame=Frame(root)
frame.pack()
frame.config(width="850", height="550")


texto=Label(frame, text="n")
texto.grid(row=0, column=0, sticky="e", padx=3, pady=3)
mostrar=Entry(frame, state="readonly", textvariable=pantalla)
mostrar.grid(row=0, column=1, padx=3, pady=3)
texto2=Label(frame, text="Factorial (n)")
texto2.grid(row=0, column=2, sticky="e", padx=3, pady=3)
mostrar2=Entry(frame, state="readonly", textvariable=pantalla2)
mostrar2.grid(row=0, column=4, padx=3, pady=3)


boton=Button(frame, text="Siguiente", width=10, cursor="hand2", command=lambda:[sumar(pantalla.get()), factorial(pantalla.get())])
boton.grid(row=0, column=5, padx=3, pady=3)


root.mainloop()