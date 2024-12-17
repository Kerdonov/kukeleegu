from datetime import datetime, timedelta
from time import sleep
from multiprocessing import Process, Event
from random import randrange
import vlc
from alarm_gui import AlarmGui


class Alarm:
    def __init__(self, hr, min, alarm_file_name="wakey-wakey.mp3", sec=0, name="äratus"):
        self.time = datetime.now() \
            .replace(hour=hr, minute=min, second=sec, microsecond=0)
        self.name = name
        self.alarm_file_name = alarm_file_name

        print(f"New alarm for {self.time}")

    def enable(self):
        self.ringing = Event()  # ? use this for event binding in gui (not needed internally)
        self.finished = Event() # ! needed internally
        self.__proc = Process(target=self.__run)
        self.time_to_alarm = self.time - datetime.now()

        if self.time_to_alarm < timedelta(minutes=0):
            print("added day")
            self.time_to_alarm += timedelta(days=1)

        self.__proc.start()
    
    # ? bind snooze button to this method
    def snooze(self, snooze_minutes):
        self.time = datetime.now() + timedelta(minutes=snooze_minutes)
        print(f"snoozed {snooze_minutes} minutes")
        self.finished.set()
        self.__proc.join()
        self.enable()

    def __ring(self):
        player = vlc.Instance()
        media_list = player.media_list_new()
        media_player = player.media_list_player_new()
        media = player.media_new(self.alarm_file_name)
        media_list.add_media(media)
        media_player.set_media_list(media_list)
        media_player.set_playback_mode(vlc.PlaybackMode(1))
        media_player.play()
        print(f"{self.name} alarm")
        self.finished.wait()
        media_player.stop()

    # ? bind alarm disable to this method (use sudo_mode)
    def disable(self, sudo_mode=False) -> bool:
        if self.ringing.is_set():
            if sudo_mode:
                self.ringing.clear()
                self.finished.set()
                self.__proc.join()
                return True
            else:
                return False
        else:
            self.__proc.terminate()
            print(f"Alarm {self.name} at {self.time} disabled!!!")
            return True

    def __run(self):
        print(f"proc: Alarm {self.time_to_alarm} from now")
        sleep(self.time_to_alarm.seconds)
        self.ringing.set()
        self.__ring()
        self.ringing.clear()
        print("proc: process exited")



class RandomAlarm(Alarm):
    def __init__(self, hr, min, alarm_file_name="wakey-wakey.mp3", sec=0, name="random äratus"):
        super().__init__(hr, min, alarm_file_name, sec, name)
        delta = datetime.now().replace(hour=hr, minute=min, second=sec, microsecond=0) - datetime.now()
        rand_delta_seconds = randrange(delta.seconds)
        self.time = datetime.now() + timedelta(seconds=rand_delta_seconds)


if __name__ == "__main__":
    t = datetime.now().replace(hour=8, minute=30)
    examplealarm1 = RandomAlarm(t.hour, t.minute, sec=t.second)
    examplealarm1.enable()
    sleep(1)
    examplealarm1.disable()