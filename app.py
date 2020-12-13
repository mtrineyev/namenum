"""
Main application for Name the Number Telegram game bot

Sets break handler and keeps game running

Stopped by Control-C

NameTheNumberBot v1.0 (c) 2020 Maksym Trineyev
mtrineyev@gmail.com
"""

from os import path
import signal
import sys

sys.path.insert(0,
    path.abspath(path.join(path.dirname(__file__), './modules')))
from modules.namenum import NameTheNumber

LISTEN = True


def signal_handler(sig: int, frame) -> None:
    """Sets reaction to interrupt from keyboard"""
    global LISTEN
    if LISTEN:
        print(' SIGINT received.\n Terminating...')
        LISTEN = False
    else:
        print(f' It\'s can take some time due connection delay, '\
            'please be patient')


def bot() -> None:
    """Sets signal handler and keeps game running"""
    signal.signal(signal.SIGINT, signal_handler)

    with NameTheNumber() as game:
        while LISTEN:
            game.listen()


if __name__ == '__main__':
    bot()
