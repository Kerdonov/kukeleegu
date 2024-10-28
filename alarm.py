from datetime import datetime, timedelta
from time import sleep
from multiprocessing import Process

class Alarm:
    def __init__(self, hr, min, sec=0, name=""):
        self.time = datetime.now().replace(hour=hr, minute=min, second=sec, microsecond=0)
        self.name = name

        print(f"New alarm for {self.time}")
    

    def enable(self):
        self.__alarmproc = Process(target=self.__run)
        self.time_to_alarm = self.time - datetime.now()
        
        if self.time_to_alarm < timedelta(minutes=0):
            print("added day")
            self.time_to_alarm += timedelta(days=1)
        
        self.__alarmproc.start()
    

    def disable(self):
        self.__alarmproc.terminate()
        print(f"Alarm {self.name} at {self.time} disabled!!!")



    
    def __wake_up(self):
        print(f"BEEP BEEP BEEP {self.name}")


    def __run(self):
        print(f"proc: Alarm {self.time_to_alarm} from now")

        sleep(self.time_to_alarm.seconds)
        self.__wake_up()


if __name__ == "__main__":
    examplealarm = Alarm(16, 59, name="tere hommikust")
    examplealarm.enable()
    sleep(5)
    examplealarm.disable()
    sleep(5)
    examplealarm.enable()