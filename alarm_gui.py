import tkinter as tk
from questioner import Questioner

class AlarmGui:
    def __init__(self, alarm):
        self.alarm = alarm
        self.questioner = Questioner()
        self.answer_value = tk.StringVar()
        self.win = tk.Toplevel()
        self.win.wm_title(self.questioner.text)

        question = tk.Label(self.win, text=self.questioner.text)
        answerbox = tk.Entry(self.win, width=15, textvariable=self.answer_value)
        submit = tk.Button(self.win, width=5, command=self.answer)
        
        question.pack()
        answerbox.pack()
        submit.pack()
        self.win.mainloop()
    
    def answer(self):
        if self.questioner.answer_question(self.answer_value):
            self.alarm.disable()
            self.win.destroy()