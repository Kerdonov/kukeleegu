import tkinter as tk
from questioner import Questioner

class AlarmGui(tk.Frame):
    def __init__(self, parent, alarm_manager, width=400, height=340):
        tk.Frame.__init__(self, parent, width=width, height=height)
        self.alarm_manager = alarm_manager
        self.answer_value = tk.StringVar()

        self.questionbox = tk.Message(self, text="No alarms ringing", relief=tk.RAISED)
        answerbox = tk.Entry(self, width=15, textvariable=self.answer_value)
        submit = tk.Button(self, width=5, text="Vasta", command=self.answer)
        
        self.questionbox.place(x=0, y=0, height=300, width=400)
        answerbox.place(x=0, y=300, height=40, width=300)
        submit.place(x=300, y=300, height=40, width=100)
        self.reset()
    
    def reset(self):
        self.questioner = Questioner()
        print(self.questioner.true_answer)
        self.questionbox.config(text=self.questioner.text)

    
    def answer(self):
        if self.questioner.answer_question(self.answer_value.get()):
            # toggle all ringing alarms off (scuffed)
            for widget in self.alarm_manager.widgets:
                if widget.alarm.ringing.is_set():
                    widget.toggle_alarm(sudo_mode=True)
            
            self.reset()