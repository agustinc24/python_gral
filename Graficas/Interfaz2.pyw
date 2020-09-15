from tkinter import *

raiz=Tk()

raiz.title("El Peneador")
#raiz.geometry("650x450")
raiz.iconbitmap("pene.ico")
raiz.config(bg="black")
miFrame=Frame()
miFrame.pack()
miFrame.config(bg="pink")
miFrame.config(width="650", height="450")
miFrame.config(bd=35)#cambio el tamaño del borde
miFrame.config(relief="sunken")#cambio el diseño del borde
miFrame.config(cursor="pirate")



raiz.mainloop()