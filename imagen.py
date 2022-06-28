from tkinter import *
ventana=Tk()
ventana.title("tizi lindo")
ventana.geometry("568x516")
imagen=PhotoImage (file='pompompurin.png')
fondo=Label (ventana, image=imagen) .place(x=0 , y=0)
ventana.mainloop()