import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
import requests
import json
import random

url = 'https://flagcdn.com/w80/{}.jpg'
resp = requests.get("https://flagcdn.com/en/codes.json")
flags = json.loads(resp.text)
a = 0
num = random.randint(0,len(flags))

for i in flags:
    a += 1
    if a == num:
        bandera = flags[i]
        url_final = url.format(i)
        print(url)
root = tk.Tk()

imageUrl = "https://flagcdn.com/256x192/ai.png"
u = urlopen(Url)
raw_data = u.read()
u.close()

photo = ImageTk.PhotoImage(data=raw_data)
label = tk.Label(image = photo)
label.image = photo
label.pack()

root.mainloop()