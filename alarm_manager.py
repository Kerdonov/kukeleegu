import tkinter as tk
from alarm import Alarm, RandomAlarm

class AlarmWidget(tk.Frame):
    def __init__(self, parent, alarm, is_random, label="", width=400, height=80):
        background = "#FF0000" if is_random else "#000000"
        tk.Frame.__init__(self, parent, width=width, height=height, bg=background)
        self.alarm = alarm
        self.parent = parent
        self.alarm.enable()
        self.enabled = True

        if label == "":
            label = f"{alarm.name}: {alarm.time.hour}:{alarm.time.minute}"

        alarm_widget = tk.Frame(self, width=400, height=80, bg=background)
        tk.Label(self, text=label, anchor="w").pack(side=tk.LEFT)
        self.toggle_button = tk.Button(self, text="ON", command=self.toggle_alarm, bg=background)
        self.toggle_button.pack(side=tk.RIGHT)
        tk.Button(self, text="trash", command=self.remove_alarm, bg=background).pack(side=tk.RIGHT)


    def toggle_alarm(self):
        if self.enabled:
            self.alarm.disable()
            self.enabled = False
            self.toggle_button.config(text="OFF")
        else:
            self.alarm.enable()
            self.enabled = True
            self.toggle_button.config(text="ON")
        
    def remove_alarm(self):
        self.alarm.disable()
        self.parent.remove_alarm(self)

# https://stackoverflow.com/questions/30489308/creating-a-custom-widget-in-tkinter
class AlarmManager(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=400, height=400)
        self.widgets = []
        # todo create alarm creating widget
        self.new_alarm_is_random = False

        self.alarm_hour_var = tk.IntVar()
        self.alarm_minute_var = tk.IntVar()
        self.alarm_name_var = tk.StringVar()

        new_alarm_widget = tk.Frame(self, width=400, height=80)
        hour_input = tk.Entry(new_alarm_widget, width=5, textvariable=self.alarm_hour_var)
        minute_input = tk.Entry(new_alarm_widget, width=5, textvariable=self.alarm_minute_var)
        name_input = tk.Entry(new_alarm_widget, width=10, textvariable=self.alarm_name_var)

        self.is_random_button = tk.Button(new_alarm_widget, text="NORMAL", command=self.toggle_random)
        new_alarm_button = tk.Button(new_alarm_widget, text="+", command=self.new_alarm)

        hour_input.pack(side=tk.LEFT)
        minute_input.pack(side=tk.LEFT)
        name_input.pack(side=tk.LEFT)
        self.is_random_button.pack(side=tk.LEFT)
        new_alarm_button.pack(side=tk.RIGHT)

        new_alarm_widget.pack()

    def toggle_random(self):
        if self.new_alarm_is_random:
            self.is_random_button.config(text="NORMAL")
            self.new_alarm_is_random = False
        else:
            self.is_random_button.config(text="RANDOM")
            self.new_alarm_is_random = True
    
    def new_alarm(self):
        if self.new_alarm_is_random:
            alarm = RandomAlarm(self.alarm_hour_var.get(), self.alarm_minute_var.get(), name=self.alarm_name_var.get())
        else:
            alarm = Alarm(self.alarm_hour_var.get(), self.alarm_minute_var.get(), name=self.alarm_name_var.get())

        widget = AlarmWidget(self, alarm, self.new_alarm_is_random, label=f"{self.alarm_name_var.get()}: {self.alarm_hour_var.get()}:{self.alarm_minute_var.get()}")
        widget.pack()
        self.widgets.append(widget)


    def remove_alarm(self, alarm):
        self.widgets.remove(alarm)
        alarm.destroy()