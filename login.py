from tkinter import *
from tkinter import messagebox
import sqlite3

ventana_login = Tk()
ventana_login.title("Crear usuario")
ventana_login.geometry("500x500")

Label(ventana_login, text= "Crear nombre de usuario").pack()
username = Entry(ventana_login)
username.pack()

Label(ventana_login, text= "Crear contraseña").pack()
password = Entry(ventana_login, show= "*")
password.pack()
entrar = Button(text="Login", command=login)
entrar.pack()


def login():
    db = sqlite3.connect("/home/alumno/Documentos/tiiacu/base_juego")
    c = db.cursor()
    
    usuario = Usuario.get()
    contra = contraseña.get()
    
    c.execute('SELECT * FROM usuarios WHERE usuario = ? AND pass = ?', (usuario,contra))
    
    resultado= c.fetchone()
    print(resultado)
    
    if c.fetchall():
            showinfo(title="Listo!", message="Ingresaste correctamente")
    else:  
            showerror(title="Ocurrio un error", message="La contraseña o usuario ingresado son incorrectos")
            
    c.close()
        


ventana_login.mainloop()