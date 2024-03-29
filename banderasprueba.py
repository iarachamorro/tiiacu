import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import Request, urlopen, urlretrieve
import requests
import json
import random
from functools import partial

class banderas:
    def __init__(self):
        partes = construir_pantalla()
        self.f1 = partes[0]
        self.f2 = partes[1]
        self.f3 = partes[2]
        self.label = partes[3]
        self.ventana = partes[4]

        datos_bandera = sortear_bandera()
        nombre_pais = datos_bandera[0]
        fotoJuego = datos_bandera[1]
        photo = datos_bandera[2]
        label.image = photo
        label.config(image = photo)

        lista = []
        b_guardar = tk.Button(f3, text="listo", command=partial(valorar, lista))

        b_guardar.grid(column=0, row=0)
        lista[0].focus_set()
        ventana.mainloop()

        
    

    def valorar(lista):
        nombre = ""
        for i in lista:
            letra = i.get()
            nombre += letra
        if nombre.upper() == nombre_pais.upper():
            print("Ganaste, sumaste un punto")
        else:
            print("Perdiste")


    def limitador(*entry_text):
        
        print(entry_text)
        pos = int(entry_text[1][6:])
        if(lista[pos].get()):
            if pos < len(lista)-1:
                lista[pos+1].focus_set()
        else:
            lista[pos-1].focus_set()
        if len(entry_text[0].get()) > 0:
            entry_text[0].set(entry_text[0].get()[:1].upper())

        for i in flags:
            a += 1
            if a == num:
                nombre_pais = flags[i].replace(" ", "")
                url_final = url.format(i)
                response = requests.get(url_final)
                file = open("fotoJuego.png", "wb")                     
                file.write(response.content)
                file.close()
                print(nombre_pais)
                print(url_final)
        req = Request(url_final, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(req).read()
        print(len(nombre_pais)*"_ ")
        photo = ImageTk.PhotoImage(data=raw_data)
        return (nombre_pais, url_final, photo)

    def sortear_bandera():
        url = 'https://flagcdn.com/256x192/{}.png'
        resp = requests.get("https://flagcdn.com/es/codes.json", headers={'User-Agent': 'Mozilla/5.0'})
        flags = json.loads(resp.text)
        a = 0
        num = random.randint(0,len(flags))

        for i in flags:
            a += 1
            if a == num:
                nombre_pais = flags[i].replace(" ", "")
                url_final = url.format(i)
                response = requests.get(url_final)
                file = open("fotoJuego.png", "wb")
                file.write(response.content)
                file.close()
                ima = Image.open("fotoJuego.png")
                img = ImageTk.PhotoImage(ima,master=ventana)
                print(nombre_pais)
                print(url_final)
        req = Request(url_final, headers={'User-Agent': 'Mozilla/5.0'})
        raw_data = urlopen(req).read()
        print(len(nombre_pais)*"_ ")
        photo = ImageTk.PhotoImage(data=raw_data)
        return (nombre_pais, img , photo)


    def construir_pantalla(self):
        ventana = tk.Tk()
        ventana.title("Banderas")
        self.f1 = tk.Frame(ventana)
        self.f1.grid(column=0, row=0)
        self.f2 = tk.Frame(ventana)
        self.f2.grid(column=0, row=1)
        self.f3 = tk.Frame(ventana)
        self.f3.grid(column=0, row=2)
        self.label = tk.Label(f1)
        self.label.grid(column=0, row=0)
        return (f1,f2,f3, label, ventana)


        for i in range(len(nombre_pais)):
            entry_text = tk.StringVar()  
            i_nombre = tk.Entry(f2, width=2, textvariable = entry_text,  justify=tk.CENTER)
            entry_text.trace("w", partial(limitador,entry_text))
            lista.append(i_nombre)
            i_nombre.grid(column=i,row=0)
    
