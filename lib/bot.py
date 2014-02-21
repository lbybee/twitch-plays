from config.config import config
from lib.irc import Irc
import time


class Bot:

    def __init__(self):
        self.config = config
        self.irc = Irc(config)

    def run(self):
        throttle_timers = {button: 0 for button
                           in config['throttled_buttons'].keys()}

        while True:
            new_messages = self.irc.recv_messages(1024)
            if not new_messages:
                continue
            for message in new_messages:
                button = message['message'].lower()
                username = message['username'].lower()
                if button in self.config['throttled_buttons']:
                    if (time.time() - throttle_timers[button]
                            < self.config['throttled_buttons'][button]):
                        continue

                    throttle_timers[button] = time.time()
                print username, button
