from config.config import config
from lib.irc import Irc
import time
import datetime


class Bot:

    def __init__(self):
        self.config = config
        self.irc = Irc(config)

    def run(self):
        throttle_timers = {button: 0 for button
                           in config['throttled_buttons'].keys()}

        i = 0
        while True:
            t1 = datetime.datetime.now()
            i += 1
            new_messages = self.irc.recv_messages(1024)
            if not new_messages:
                continue
            for message in new_messages:
                button = message['message'].lower()
                username = message['username'].lower()
                d_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                if button in self.config['throttled_buttons']:
                    if (time.time() - throttle_timers[button]
                            < self.config['throttled_buttons'][button]):
                        continue

                    throttle_timers[button] = time.time()
                print d_time, username, button
                if i == 10000:
                    output = open(t1.strftime("%Y%m%d%H%M%S") + ".log", "wb")
                    output.write("%s <%s> %s \n" % (d_time, username, button))
                    i = 0
                    output.close()
