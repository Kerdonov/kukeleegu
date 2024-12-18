import tkinter as tk
from tkinter import font
from tkinter import filedialog
from alarm import Alarm, RandomAlarm

class AlarmWidget(tk.Frame):
    def __init__(self, parent, alarm, width=360, height=40, time_label=None):
        # random alarm -> red background, else normal background
        is_random = time_label != None # defined in AlarmManager::new_alarm()
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
        tk.Label(self, text=f"{self.alarm.name} @ {time_label}", anchor="w").place(x=0, y=0, height=40, width=240)
        self.toggle_button = tk.Button(self, text="  ", command=self.toggle_alarm, bg=background)
        self.toggle_button.place(x=240, y=0, height=40, width=60)
        tk.Button(self, text=" ", command=self.remove_alarm, bg=background).place(x=300, y=0, height=40, width=60)


    # sudo_mode == True => called from AlarmGui class
    # sudo_mode == False => otherwise
    # (see Alarm::disable() for more)
    def toggle_alarm(self, sudo_mode=False):
        if self.enabled:
            if self.alarm.disable(sudo_mode=sudo_mode):
                self.enabled = False
                self.toggle_button.config(text="  ")
        else:
            self.alarm.enable()
            self.enabled = True
            self.toggle_button.config(text="  ")
    
    # if alarm disabling is successful, then calls parent
    # (AlarmManager) class method to remove itself
    def remove_alarm(self) -> bool:
        if self.alarm.disable():
            self.parent.remove_alarm(self)

# https://stackoverflow.com/questions/30489308/creating-a-custom-widget-in-tkinter
class AlarmManager(tk.Frame):
    def __init__(self, parent, width=360, height=760):
        # unhinged hack to change default font (very fun)
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(size=15)

        # initialize parent
        tk.Frame.__init__(self, parent, width=height, height=height)
        self.widgets = [] # holds child widgets (for each alarm)
        self.new_alarm_is_random = False

        self.alarm_hour_var = tk.StringVar()
        self.alarm_minute_var = tk.StringVar()
        self.alarm_name_var = tk.StringVar()
        self.alarm_file_name = "wakey-wakey.mp3" # default value

        # create-new-alarm widget
        new_alarm_widget = tk.Frame(self, width=360, height=80)
        hour_input = tk.Entry(new_alarm_widget, width=5, textvariable=self.alarm_hour_var)
        minute_input = tk.Entry(new_alarm_widget, width=5, textvariable=self.alarm_minute_var)
        name_input = tk.Entry(new_alarm_widget, width=10, textvariable=self.alarm_name_var)
        self.choose_audio_button = tk.Button(new_alarm_widget, text="󰝚 ", command=self.open_music_file)

        self.is_random_button = tk.Button(new_alarm_widget, text="󰒞 ", command=self.toggle_random)
        new_alarm_button = tk.Button(new_alarm_widget, text=" ", command=self.new_alarm)

        self.choose_audio_button.place(x=0, y=40, width=360, height=40)
        hour_input.place(x=0, y=0, height=40, width=60)
        minute_input.place(x=60, y=0, height=40, width=60)
        name_input.place(x=120, y=0, height=40, width=120)
        self.is_random_button.place(x=240, y=0, height=40, width=60)
        new_alarm_button.place(x=300, y=0, height=40, width=60)

        new_alarm_widget.place(x=0, y=0)
    
    def open_music_file(self):
        filetypes = [('mp3 files', '*.mp3')]
        self.alarm_file_name = filedialog.askopenfilename(title='Choose alarm', filetypes=filetypes)
        # shortname is displayed in GUI
        # this syntax ensures that it works on both Unix-based
        # and Windows filepaths (didn't want to use os.path)
        shortname = min(self.alarm_file_name.split("/")[-1], \
            self.alarm_file_name.split("\\")[-1], \
            key=lambda x: len(x))
        self.choose_audio_button.config(text=f"󰝚 {shortname}")


    def toggle_random(self):
        if self.new_alarm_is_random:
            self.is_random_button.config(text="󰒞 ")
            self.new_alarm_is_random = False
        else:
            self.is_random_button.config(text="󰒝 ")
            self.new_alarm_is_random = True
    
    def new_alarm(self):
        hour = int(self.alarm_hour_var.get())
        minute = int(self.alarm_minute_var.get())
        if self.new_alarm_is_random:
            alarm = RandomAlarm(hour, minute, name=self.alarm_name_var.get(), alarm_file_name=self.alarm_file_name)
            label = f"{int(self.alarm_hour_var.get()):02d}:{int(self.alarm_minute_var.get()):02d}"
        else:
            alarm = Alarm(hour, minute, name=self.alarm_name_var.get(), alarm_file_name=self.alarm_file_name)
            label = None

        widget = AlarmWidget(self, alarm, time_label=label)
        widget.pack()
        self.widgets.append(widget)

    # called from AlarmWidget class
    def remove_alarm(self, alarm):
        self.widgets.remove(alarm)
        alarm.destroy()