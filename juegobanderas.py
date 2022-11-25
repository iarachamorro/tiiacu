import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import Request, urlopen, urlretrieve
import requests
import json
import random
from functools import partial

class Juego:

    def __init__(self):
        self.root = tk.Tk()
        self.palabras = 0
        self.root.title("Banderas")
        self.f1 = tk.Frame(self.root)
        self.f1.grid(column=0, row=0)
        self.f2 = tk.Frame(self.root)
        self.f2.grid(column=0, row=1)
        self.f3 = tk.Frame(self.root)
        self.f3.grid(column=0, row=2)
        self.label = tk.Label(self.f1)
        self.label.grid(column=0, row=0)
        self.lista = []
        self.sortear_bandera()
        self.ponerImagen()           
        b_guardar = tk.Button(self.f3, text="listo", command=partial(self.valorar))
        b_guardar.grid(column=0, row=0)
        self.lista[0].focus_set()
        
        self.root.mainloop()

    def valorar(self):
        nombre = ""
        for i in self.lista:
            letra = i.get()
            nombre += letra
        if nombre.upper() == self.nombre_pais.upper():
            print("Ganaste, sumaste un punto")
        else:
            print("Perdiste")
        self.f2.destroy()
        self.f2 = tk.Frame(self.root)
        self.f2.grid(column=0, row=1)
        self.palabras += len(self.nombre_pais)
        print(self.palabras)
        self.sortear_bandera()
        self.ponerImagen()
        

    def limitador(self, *entry_text):
        print(entry_text)
        pos = int(entry_text[1][6:]) - self.palabras
        if(self.lista[pos].get()):
            if pos < len(self.lista)-1:
                self.lista[pos+1].focus_set()
        else:
            self.lista[pos-1].focus_set()
        if len(entry_text[0].get()) > 0:
            entry_text[0].set(entry_text[0].get()[:1].upper())

    def sortear_bandera(self):
        url = 'https://flagcdn.com/256x192/{}.png'
        resp = requests.get("https://flagcdn.com/es/codes.json", headers={'User-Agent': 'Mozilla/5.0'})
        flags = json.loads(resp.text)
        a = 0
        num = random.randint(0,len(flags))
        for i in flags:
            a += 1
            if a == num:
                self.nombre_pais = flags[i].replace(" ", "")
                url_final = url.format(i)
                response = requests.get(url_final)
                file = open("fotoJuego.png", "wb")                     
                file.write(response.content)
                file.close()
                print(self.nombre_pais)
                #print(url_final)
        req = Request(url_final, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(req).read()
        #print(len(nombre_pais)*"_ ")
        self.photo = ImageTk.PhotoImage(data=raw_data, master=self.label)
        



    def ponerImagen(self):
        self.lista = []
        for i in range(len(self.nombre_pais)):
            entry_text = tk.StringVar()  
            i_nombre = tk.Entry(self.f2, width=2, textvariable = entry_text,  justify=tk.CENTER)
            entry_text.trace("w", partial(self.limitador,entry_text))
            self.lista.append(i_nombre)
            i_nombre.grid(column=i,row=0)
        self.label.image = self.photo
        self.label.config(image = self.photo)


if __name__ == "__main__":
    j = Juego()