import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
from io import BytesIO

root = tk.Tk()
URL = "http://www.universeofsymbolism.com/images/ram-spirit-animal.jpg"
URL2 = "https://www.cleverfiles.com/howto/wp-content/uploads/2018/03/minion.jpg"


u = urlopen(URL)
raw_data = u.read()
u.close()
im = Image.open(BytesIO(raw_data))
img = ImageTk.PhotoImage(im)

panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")

def callback():
    u2 = urlopen(URL2)
    raw_data2 = u2.read()
    u2.close()
    im2 = Image.open(BytesIO(raw_data2))
    img2 = ImageTk.PhotoImage(im2)
    panel.configure(image=img2)
    panel.image = img2

def cambiar():
    b1.config(text="hola")


b1 = tk.Button(root, text="cambiar", command=callback)
b2 = tk.Button(root, text="cambiar boton", command=cambiar)
b2.pack()
b1.pack()
root.mainloop()