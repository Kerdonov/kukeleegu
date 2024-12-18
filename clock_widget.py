from tkinter import *
from tkinter import ttk
import time
import math



class AnalogClock(Canvas):
    
    def __init__(self, parent, *args, **kwargs):
        
        Canvas.__init__(self, parent, *args, **kwargs)
        self.WIDTH = self.winfo_reqwidth() - 10 # returns canvas width
        self.HEIGHT = self.winfo_reqheight() - 10 # returns canvas height
        self.x_center = self.WIDTH / 2
        self.y_center = self.HEIGHT / 2
        self.clock_update()
        
    # draw background, clock and clock hands
    def draw_analog_clock(self):
        t_current = time.localtime(time.time())
        
        hour, minute, sec = t_current.tm_hour % 12, t_current.tm_min, t_current.tm_sec
    
        angle_h = 2*math.pi*((hour*60+minute)/(12*60)) - math.pi/2
        angle_m = 2*math.pi*(minute/60)- math.pi/2
        angle_s = 2*math.pi*(sec/60)- math.pi/2

        self.create_oval(10, 10, self.WIDTH, self.HEIGHT, fill = 'white', width = 3)
        
        # draw hour hand
        x_hour = self.x_center + 0.25 * self.WIDTH * math.cos(angle_h)
        y_hour = self.y_center + 0.25 * self.HEIGHT * math.sin(angle_h)
        self.create_line(self.x_center, self.y_center, x_hour, y_hour, fill = 'black')
        
        # draw minute hand
        x_minute = self.x_center + 0.35 * self.WIDTH * math.cos(angle_m)
        y_minute = self.y_center + 0.35 * self.HEIGHT * math.sin(angle_m)
        self.create_line(self.x_center, self.y_center, x_minute, y_minute, fill = 'black')
        
        # draw second hand
        x_second = self.x_center + 0.45 * self.WIDTH * math.cos(angle_s)
        y_second = self.y_center + 0.45 * self.HEIGHT * math.sin(angle_s)
        self.create_line(self.x_center, self.y_center, x_second, y_second, fill = 'black')
        
        # draw numberplate
        for i in range(1,13):
            angle_text = 2*math.pi*((i%12)/12) - math.pi/2
            x_text = self.x_center + self.x_center * 0.75 * math.cos(angle_text)
            y_text = self.y_center + self.y_center * 0.75 * math.sin(angle_text)
            self.create_text(x_text, y_text, text = i, font = ('Comic Sans MS', 16), fill = 'black')
    
    def clock_update(self):
        self.delete('all')
        self.draw_analog_clock()
        self.after(1000, self.clock_update)
        
