from tkinter import *
from tkinter import messagebox
import sqlite3

class Vent_usuario:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title ("Usuarios")
        self.ventana.geometry ("350x150+500+250")
        Label(self.ventana, text = "Usuario:").pack()
        self.caja1 = Entry(self.ventana)
        self.caja1.pack()

        Label(self.ventana, text = "Contraseña:").pack()
        self.caja2 = Entry(self.ventana, show = "*")
        self.caja2.pack()
        Button (text = "Login", command = self.login).pack()

    def login(self):
        self.usuario = self.caja1.get()
        self.contra = self.caja2.get()
        print(self.usuario)
        print(self.contra)
     
    def guardar(self):
        self.text = self.usuario.get()
        self.sql = 'Insert into Nombres (Nombre) values ("{}");'
        self.cur.execute(sql.format(text))
        self.bd.commit()
     
if __name__ == '__main__':
    print("CHAU")
    #ventana.mainloop()

