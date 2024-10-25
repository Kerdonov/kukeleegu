from tkinter import *
from tkinter import ttk
import time
import math

raam = Tk()
raam.title('Kell')

c = Canvas(raam, bg='blue', height = 500, width = 500)
ovaal = c.create_oval(0, 0, 100, 100, fill = 'white', width = 5)
c.pack()


class analoogkell:
    def __init__(self, parent, *args, **kwargs):



raam.mainloop()