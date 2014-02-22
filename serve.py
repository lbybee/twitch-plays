#!/usr/bin/env python

from sys import exit
import lib.bot as bot
import os
import sys

# Twitch Plays
# Inpsired by http://twitch.tv/twitchplayspokemon
# Written by Aidan Thomson - <aidraj0 at gmail dot com>

os.chdir(sys.argv[1])
try:
    bot.Bot().run()
except KeyboardInterrupt:
    exit()
