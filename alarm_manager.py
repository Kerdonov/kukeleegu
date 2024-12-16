import tkinter as tk
from tkinter import font
from tkinter import filedialog
from alarm import Alarm, RandomAlarm

class AlarmWidget(tk.Frame):
    def __init__(self, parent, alarm, width=400, height=80, time_label=None):
        # random alarm -> red background, else normal background
        is_random = time_label != None
        background = "red1" if is_random else "white"

        # initialize parent widget
        tk.Frame.__init__(self, parent, width=width, height=height, bg=background)
        self.alarm = alarm
        self.parent = parent
        self.alarm.enable()
        self.enabled = True

        # set correct time label for alarm
        if not is_random:
            time_label = f"{alarm.time.hour:0>2d}:{alarm.time.minute:0>2d}"

        # set widgets
        tk.Label(self, text=f"{self.alarm.name} @ {time_label}", anchor="w").pack(side=tk.LEFT)
        tk.Button(self, text=" ", command=self.remove_alarm, bg=background).pack(side=tk.RIGHT)
        self.toggle_button = tk.Button(self, text="  ", command=self.toggle_alarm, bg=background)
        self.toggle_button.pack(side=tk.RIGHT)


    def toggle_alarm(self):
        if self.enabled:
            self.alarm.disable()
            self.enabled = False
            self.toggle_button.config(text="  ")
        else:
            self.alarm.enable()
            self.enabled = True
            self.toggle_button.config(text="  ")
        
    def remove_alarm(self) -> bool:
        if self.alarm.disable():
            self.parent.remove_alarm(self)

# https://stackoverflow.com/questions/30489308/creating-a-custom-widget-in-tkinter
class AlarmManager(tk.Frame):
    def __init__(self, parent):
        # unhinged hack to change default font (kill me now)
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(size=12)

        # initialize parent
        tk.Frame.__init__(self, parent, width=400, height=400)
        self.widgets = [] # holds child widgets (for each alarm)
        self.new_alarm_is_random = False

        self.alarm_hour_var = tk.IntVar()
        self.alarm_minute_var = tk.IntVar()
        self.alarm_name_var = tk.StringVar()
        self.alarm_file_name = "wakey-wakey.mp3" # default value

        new_alarm_widget = tk.Frame(self, width=400, height=80)
        hour_input = tk.Entry(new_alarm_widget, width=5, textvariable=self.alarm_hour_var)
        minute_input = tk.Entry(new_alarm_widget, width=5, textvariable=self.alarm_minute_var)
        name_input = tk.Entry(new_alarm_widget, width=10, textvariable=self.alarm_name_var)
        self.choose_audio_button = tk.Button(new_alarm_widget, text="󰝚 ", command=self.open_music_file)

        self.is_random_button = tk.Button(new_alarm_widget, text="󰒞 ", command=self.toggle_random)
        new_alarm_button = tk.Button(new_alarm_widget, text=" ", command=self.new_alarm)

        self.choose_audio_button.pack(side=tk.BOTTOM)
        hour_input.pack(side=tk.LEFT)
        minute_input.pack(side=tk.LEFT)
        name_input.pack(side=tk.LEFT)
        self.is_random_button.pack(side=tk.LEFT)
        new_alarm_button.pack(side=tk.RIGHT)

        new_alarm_widget.pack()
    
    def open_music_file(self):
        filetypes = [('mp3 files', '*.mp3')]
        self.alarm_file_name = filedialog.askopenfilename(title='Choose alarm', filetypes=filetypes)
        # I'm so sorry :(
        shortname = min(self.alarm_file_name.split("/")[-1], \
            self.alarm_file_name.split("\\")[-1], \
            key=lambda x: len(x))
        self.choose_audio_button.configure(text=f"󰝚 {shortname}")


    def toggle_random(self):
        if self.new_alarm_is_random:
            self.is_random_button.config(text="󰒞 ")
            self.new_alarm_is_random = False
        else:
            self.is_random_button.config(text="󰒝 ")
            self.new_alarm_is_random = True
    
    def new_alarm(self):
        if self.new_alarm_is_random:
            alarm = RandomAlarm(self.alarm_hour_var.get(), \
                self.alarm_minute_var.get(), \
                name=self.alarm_name_var.get(), \
                alarm_file_name=self.alarm_file_name)
            label = f"{self.alarm_hour_var.get():02d}:{self.alarm_minute_var.get():02d}"
        else:
            alarm = Alarm(self.alarm_hour_var.get(), \
                self.alarm_minute_var.get(), \
                name=self.alarm_name_var.get(), \
                alarm_file_name=self.alarm_file_name)
            label = None

        widget = AlarmWidget(self, alarm, time_label=label)
        widget.pack()
        self.widgets.append(widget)


    def remove_alarm(self, alarm):
        if self.widgets.remove(alarm):
            alarm.destroy()