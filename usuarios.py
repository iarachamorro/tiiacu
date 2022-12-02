from tkinter import *
from tkinter import messagebox
import sqlite3
import db_utils
import juegobanderas 


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
        self.bd = db_utils.Base("base_juego.db")
        Button (text = "Agregar", command = self.guardar).pack()
        self.ventana.mainloop()


    def login(self):
        self.usuario = self.caja1.get()
        self.contra = self.caja2.get()
        respuesta = self.bd.login(self.contra, self.usuario)
        if not respuesta:
            self.ventana.withdraw()
            self.juego = juegobanderas.Juego()
        else:   
            messagebox.showinfo("Error",self.bd.respuestas_login[respuesta])
     
    def guardar(self):
        self.usuario = self.caja1.get()
        self.contra = self.caja2.get()
        resp = self.bd.alta_usuario(self.contra, self.usuario)
        messagebox.showinfo("Error",self.bd.respuestas_alta_usuarios[resp])
        
        
     
b = Vent_usuario()