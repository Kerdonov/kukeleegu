from datetime import datetime, timedelta
from time import sleep
from threading import Thread



class Alarm:
    def __init__(self, hr, min):
        self.time = datetime.now().replace(hour=hr, minute=min, second=0, microsecond=0)

        print(f"New alarm for {self.time}")
        self.__timerthread = Thread(target=self.run, args=())
        self.__timerthread.daemon = False
    
    def enable(self):
        self.time_to_alarm = self.time - datetime.now()
        
        if self.time_to_alarm < timedelta(minutes=0):
            print("added day")
            self.time_to_alarm += timedelta(days=1)
        
        self.__timerthread.start()
    
    def wake_up(self):
        print("BEEP BEEP BEEP")

    def run(self):
        print(f"thread: Alarm {self.time_to_alarm} from now")

        sleep(self.time_to_alarm.seconds)
        self.wake_up()


if __name__ == "__main__":
    examplealarm = Alarm(11, 53)
    examplealarm.enable()
