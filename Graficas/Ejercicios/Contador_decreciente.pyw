from tkinter import *

root=Tk()
root.title("ContDecreciente")
root.iconbitmap("peneico.ico")


def restar(num):
	num-=1
	pantalla.set(num)

pantalla=IntVar()
pantalla.set(88)

frame=Frame(root)
frame.pack()
frame.config(width="850", height="550")


texto=Label(frame, text="Contador")
texto.grid(row=0, column=0, sticky="e", padx=3, pady=3)
mostrar=Entry(frame, state="readonly", textvariable=pantalla)
mostrar.grid(row=0, column=1, padx=3, pady=3)

boton=Button(frame, text="-", width=3, cursor="hand2", command=lambda:restar(pantalla.get()))
boton.grid(row=0, column=2, padx=3, pady=3)




root.mainloop()