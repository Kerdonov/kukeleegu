from tkinter import *
from tkinter import ttk
import time
import math
from clock_widget import AnalogClock

def main():
    root = Tk()
    root.title('kukeleegu')
    root.geometry('900x410')
    AnalogClock(root, width=400, height=400).place(x=0, y=0)

    root.mainloop()

if __name__ == '__main__':
    main()