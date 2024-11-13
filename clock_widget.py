from tkinter import *
from tkinter import ttk
import time
import math



class analog_clock(Canvas):
    
    def __init__(self, parent, *args, **kwargs):
        
        Canvas.__init__(self, parent, *args, **kwargs)
        self.WIDTH = self.winfo_reqwidth() - 10#tagastab canvas'i laiuse
        self.HEIGHT = self.winfo_reqheight() - 10#tagastab canvasi kõrguse
        self.x_center = self.WIDTH / 2
        self.y_center = self.HEIGHT / 2
        self.clock_update()
        
    def draw_analog_clock(self):
        
        # Seierite ja kella tausta joonistamine
        t_current = time.localtime(time.time())
        
        hour, minute, sec = t_current.tm_hour % 12, t_current.tm_min, t_current.tm_sec
    
        angle_h = 2*math.pi*((hour*60+minute)/(12*60)) - math.pi/2
        angle_m = 2*math.pi*(minute/60)- math.pi/2
        angle_s = 2*math.pi*(sec/60)- math.pi/2

        self.create_oval(10, 10, self.WIDTH, self.HEIGHT, fill = 'white', width = 3)
        
        # tunniseieri joonistamine
        x_hour = self.x_center + 0.25 * self.WIDTH * math.cos(angle_h)
        y_hour = self.y_center + 0.25 * self.HEIGHT * math.sin(angle_h)
        self.create_line(self.x_center, self.y_center, x_hour, y_hour, fill = 'red')
        
        # minutiseieri joonistamine
        x_minute = self.x_center + 0.35 * self.WIDTH * math.cos(angle_m)
        y_minute = self.y_center + 0.35 * self.HEIGHT * math.sin(angle_m)
        self.create_line(self.x_center, self.y_center, x_minute, y_minute, fill = 'green')
        
        # sekundiseieri joonistamine
        x_second = self.x_center + 0.45 * self.WIDTH * math.cos(angle_s)
        y_second = self.y_center + 0.45 * self.HEIGHT * math.sin(angle_s)
        self.create_line(self.x_center, self.y_center, x_second, y_second, fill = 'blue')
        
        # kellale numbrite joonistamine
        for i in range(1,13):
            angle_text = 2*math.pi*((i%12)/12) - math.pi/2
            x_text = self.x_center + self.x_center * 0.75 * math.cos(angle_text)
            y_text = self.y_center + self.y_center * 0.75 * math.sin(angle_text)
            self.create_text(x_text, y_text, text = i, font = ('Arial', 16), fill = 'black')
    
    def clock_update(self):
        
        self.delete('all')
        self.draw_analog_clock()
        self.after(1000, self.clock_update)
        
        
root = Tk()
analog_clock = analog_clock(root, width = 400, height = 400)
analog_clock.pack()
root.mainloop()


