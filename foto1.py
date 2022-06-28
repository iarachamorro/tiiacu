import tkinter as tk
from PIL import Image, ImageTk
from urllib.request import urlopen
import requests
import json
import random

imageUrl = "https://flagcdn.com/256x192/ai.png"
u = urlopen(imageUrl)
raw_data = u.read()
u.close()

photo = ImageTk.PhotoImage(data=raw_data)
label = tk.Label(image = photo)
label.image = photo
label.pack()

root.mainloop()
