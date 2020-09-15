from tkinter import *

root=Tk()

root.title("Contador")
root.iconbitmap("peneico.ico")


def sumar(num):
	num+=1
	pantalla.set(num)

def restar(num):
	num-=1
	pantalla.set(num)

def reset():
	pantalla.set(0)

miFrame=Frame(root)
miFrame.pack()
miFrame.config(width="390", height="35")
miFrame.grid_propagate(False)

pantalla=IntVar()
pantalla.set(0)



texto=Label(miFrame, text="Contador")
texto.grid(row=0, column=0, sticky="e", padx=5, pady=3)

mostrar=Entry(miFrame, state="readonly", textvariable=pantalla)
mostrar.grid(row=0, column=1, padx=3, pady=3)

boton=Button(miFrame, text="Cont Up", width=6, cursor="hand2", command=lambda:sumar(pantalla.get()))
boton.grid(row=0, column=2, padx=3, pady=3)

boton=Button(miFrame, text="Cont Down", width=9, cursor="hand2", command=lambda:restar(pantalla.get()))
boton.grid(row=0, column=3, padx=3, pady=3)

boton=Button(miFrame, text="Reset", width=5, cursor="hand2", command=lambda:reset())
boton.grid(row=0, column=4, padx=3, pady=3)



root.mainloop()