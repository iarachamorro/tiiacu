import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

class Juego:
    
    def __init__(self):
        self.root = tk.Tk()
        self.URL = 'http://flagcdn.com/256x192/ar.png'
        self.URL2 = 'http://flagcdn.com/256x192/es.png'
        self.nombre1 = "ar"
        self.nombre2 = "uy"
        #file = self.obtenerFoto(self.URL, self.nombre1)
        ima = Image.open(f"{self.nombre1}.png")
        img = ImageTk.PhotoImage(ima)
        self.panel = tk.Label(self.root, image=img)
        self.panel.pack(side="bottom", fill="both", expand="yes")
        self.b1 = tk.Button(self.root, text="cambiar", command=self.callback)
        b2 = tk.Button(self.root, text="cerrar", command=self.cambiar)
        b2.pack()
        self.b1.pack()
        self.root.mainloop()
    
    def obtenerFoto(self, url, nombre):
        response = requests.get(url)
        file = open(f"{nombre}.png", "wb")
        file.write(response.content)
        file.close()

       
  
    def callback(self):
        self.panel.destroy()
        #self.obtenerFoto(self.URL2, self.nombre2)
        ima = Image.open(f"{self.nombre2}.png")
        img = ImageTk.PhotoImage(ima)
        self.panel = tk.Label(self.root, image=img)
        self.panel.pack(side="bottom", fill="both", expand="yes")


    def cambiar(self):
        self.b1.config(text="listo")


j = Juego()