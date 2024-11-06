from datetime import datetime, timedelta
from time import sleep
from multiprocessing import Process, Event


class Alarm:
    def __init__(self, hr, min, sec=0, name="äratus"):
        self.time = datetime.now() \
            .replace(hour=hr, minute=min, second=sec, microsecond=0)
        self.name = name

        print(f"New alarm for {self.time}")

    def enable(self):
        self.ringing = Event()  # ? use this for event binding in gui
        self.finished = Event()
        self.__proc = Process(target=self.__run)
        self.time_to_alarm = self.time - datetime.now()

        if self.time_to_alarm < timedelta(minutes=0):
            print("added day")
            self.time_to_alarm += timedelta(days=1)

        self.__proc.start()
    
    # ? bind snooze button to this method
    def snooze(self, snooze_minutes):
        # todo change seconds to minutes (after testing is complete)
        self.time = datetime.now() + timedelta(seconds=snooze_minutes)
        print(f"snoozed {snooze_minutes} minutes")
        self.finished.set()
        self.__proc.join()
        self.enable()

    def __ring(self):
        # todo start playing alarm
        print(f"BEEP BEEP BEEP {self.name}")
        self.finished.wait()
        # * stop alarm playing

    # ? bind alarm disable to this method
    def disable(self):
        if self.ringing.is_set():
            # todo question to disable alarm
            self.finished.set()
            self.__proc.join()
        else:
            self.__proc.terminate()
            print(f"Alarm {self.name} at {self.time} disabled!!!")

    def __run(self):
        print(f"proc: Alarm {self.time_to_alarm} from now")
        sleep(self.time_to_alarm.seconds)
        self.ringing.set()
        self.__ring()
        self.ringing.clear()
        print("proc: process exited")


if __name__ == "__main__":
    t = datetime.now() + timedelta(seconds=5)
    examplealarm1 = Alarm(t.hour, t.minute, sec=t.second, name="tere hommikust")
    examplealarm1.enable()

    t += timedelta(seconds=10)
    examplealarm2 = Alarm(t.hour, t.minute, sec=t.second, name="tere õhtust")
    examplealarm2.enable()
    
    sleep(7)
    examplealarm1.disable()
    sleep(6)
    examplealarm2.snooze(5)
    sleep(8)
    examplealarm2.disable()