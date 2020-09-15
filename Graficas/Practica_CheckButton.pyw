from tkinter import *

root=Tk()
root.title("CheckButton")
root.iconbitmap("peneico.ico")

playa=IntVar()
montania=IntVar()
turismo=IntVar()

def opcionesViaje():
	
	opcionEscogida=""

	if(playa.get()==1):
		opcionEscogida+= " playa"
	if(montania.get()==1):
		opcionEscogida+= " montaña"
	if(turismo.get()==1):
		opcionEscogida+= " turismo rural"
	textoFinal.config(text=opcionEscogida)

foto=PhotoImage(file="pene_rigati.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destino/s", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesViaje).pack()
Checkbutton(frame, text="Montaña", variable=montania, onvalue=1, offvalue=0, command=opcionesViaje ).pack()
Checkbutton(frame, text="Turiso rural", variable=turismo, onvalue=1, offvalue=0, command=opcionesViaje).pack()

textoFinal=Label(frame)
textoFinal.pack()

root.mainloop()