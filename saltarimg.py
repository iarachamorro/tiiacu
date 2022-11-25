import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class Juego:
    
    def __init__(self):
        self.root = tk.Tk()
        self.URL = 'home/Documentos/tiiacu/banderas/ar.png'
        self.URL2 = 'home/Documentos/tiiacu/banderas/es.png'
        self.nombre2 = "ar"
        self.nombre1 = "uy"
        file = self.obtenerFoto(self.URL, self.nombre1)
        self.ima = Image.open(f"{self.nombre1}.png")
        self.ima2 = Image.open(f"{self.nombre2}.png")
        self.panel = tk.Label(self.root)
        self.img = ImageTk.PhotoImage(self.ima, master=self.panel)
        self.panel.config(image=self.img)
        self.panel.pack(side="bottom", fill="both", expand="yes")
        self.b1 = tk.Button(self.root, text="cambiar", command=self.callback)
        b2 = tk.Button(self.root, text="cerrar", command=self.root.destroy)
        b2.pack()
        self.b1.pack()
        self.root.mainloop()
    
    def obtenerFoto(self, url, nombre):
        response = requests.get(url)
        file = open(f"{nombre}.png", "wb")
        file.write(response.content)
        file.close()
        

       
  
    def callback(self):
        #self.panel.destroy()
        #self.obtenerFoto(self.URL2, self.nombre2)
        
        self.img = ImageTk.PhotoImage(self.ima2, master=self.panel )
        self.panel.config(image=self.img)
        #self.panel.pack(side="bottom", fill="both", expand="yes")


    def cambiar(self):
        self.b1.config(text="listo")


j = Juego()