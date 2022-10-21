from tkinter import *
from tkinter import messagebox
import sqlite3

ventana = Tk()
ventana.title ("Usuarios")
ventana.geometry ("350x150+500+250")
Label(ventana, text = "Usuario:").pack()
caja1 = Entry(ventana)
caja1.pack()

Label(ventana, text = "Contraseña:").pack()
caja2 = Entry(ventana, show = "*")
caja2.pack()

def login():
 db = sqlite3.connect('/home/alumno/Documentos/tiiacu/base_usuarios')
 c = db.cursor()
 
 usuario = caja1.get()
 contra = caja2.get()
 
 def guardar():
    text = usuario.get()
    sql = 'Insert into Nombres (Nombre) values ("{}");'
    cur.execute(sql.format(text))
    bd.commit()
 

Button (text = "Login", command = login).pack()


ventana.mainloop()