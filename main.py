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
# ! NB! dependencies.txt
# todo leida mugavam viis jooksutamiseks (a.la kukeleegu.desktop fail)
##################################################

from tkinter import *

from clock_widget import AnalogClock
from alarm_manager import AlarmManager
from alarm_gui import AlarmGui

def main():
    root = Tk()
    root.title('kukeleegu')
    root.geometry('760x740')
    AnalogClock(root, width=400, height=400).place(x=0, y=0)

    alarm_manager = AlarmManager(root)
    alarm_manager.place(x=400, y=0)

    alarm_gui = AlarmGui(root, alarm_manager)
    alarm_gui.place(x=0, y=400)

    root.mainloop()

if __name__ == '__main__':
    main()