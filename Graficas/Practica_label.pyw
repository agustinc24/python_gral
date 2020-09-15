from tkinter import *
root=Tk()
root.title("El pene saludador")
root.iconbitmap("peneico.ico")
miFrame=Frame(root, width=750, height=550)
miFrame.pack()

miImagen=PhotoImage(file="pene_rigati.png")

Label(miFrame, text="Hola perrisssss", fg="red", font=("Comic Sans MS", 20)).place(x=150, y=100)
Label(miFrame, image=miImagen).place(x=105, y=140)


root.mainloop()