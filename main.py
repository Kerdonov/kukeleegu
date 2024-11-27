################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
# Teema: Äratuskell naljakate lisafunktsioonidega
#
#
# Autorid: Kert Jalukse, Tristan Šaraškin
#
# mõningane eeskuju: 
# kella loomisel: https://github.com/siri-n-shetty/Analog-Clock
#
# Lisakommentaar (nt käivitusjuhend):
# Hetkel käivita käsuga python3 main.py
# todo leida mugavam viis jooksutamiseks (a.la kukeleegu.desktop fail)
##################################################

from tkinter import *
from tkinter import ttk
import time
import math

from clock_widget import AnalogClock
from alarm import Alarm, RandomAlarm
from alarm_manager import AlarmManager

def main():
    root = Tk()
    root.title('kukeleegu')
    root.geometry('900x410')
    AnalogClock(root, width=400, height=400).place(x=0, y=0)

    # todo new alarm button/popup
    alarms = AlarmManager(root)
    alarms.place(x=500, y=0)

    root.mainloop()

if __name__ == '__main__':
    main()