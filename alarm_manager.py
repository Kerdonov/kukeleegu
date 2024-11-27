import tkinter as tk

class AlarmWidget(tk.Frame):
    def __init__(self, parent, alarm, width=400, height=80):
        tk.Frame.__init__(self, parent, width=width, height=height)
        self.alarm = alarm
        self.alarm.enable()
        self.enabled = True

        alarm_widget = tk.Frame(self, width=400, height=80)
        tk.Label(self, text=f"{alarm.time}", anchor="w").pack()
        tk.Button(self, text="trash", command=lambda: parent.remove_alarm(self)).pack()
        self.toggle_button = tk.Button(self, text="ON", command=self.toggle_alarm)
        self.toggle_button.pack()


    def toggle_alarm(self):
        if self.enabled:
            self.alarm.disable()
            self.enabled = False
            self.toggle_button.config(text="OFF")
        else:
            self.alarm.enable()
            self.enabled = True
            self.toggle_button.config(text="ON")

# https://stackoverflow.com/questions/30489308/creating-a-custom-widget-in-tkinter
class AlarmManager(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, width=400, height=400)
        self.widgets = []
        # todo create alarm creating widget

    
    def new_alarm(self, alarm):
        widget = AlarmWidget(self, alarm)
        widget.pack()
        self.widgets.append(widget)


    def remove_alarm(self, alarm):
        self.widgets.remove(alarm)
        alarm.destroy()