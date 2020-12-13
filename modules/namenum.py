"""
Game logic for Telegram bot

Class:
    NameTheNumber

Method:

    listen(self) -> None:
        Receives updates from the bot and acts

NameTheNumber bot v1.0 (c) 2020 Maksym Trineyev
mtrineyev@gmail.com
"""

from datetime import datetime
import random

import config
import consts.command as commands
import consts.msg as msg
from nominal import translate_num, translate_10power
import telega as tg


class NameTheNumber(object):
    """
    Game 'Name the Number'

    Translates natural numbers as well as powers of 10 into their nominal names
    also can convert binary, octal and hex numbers to decimal
    """
    def __init__(self):
        self.last_update_id = 0
        self.user_input = ''
        self.user_id = ''
        self.user_name = ''


    def __enter__(self):
        print(self._now(), 'Bot started and waiting for user input...')
        return self


    def __exit__(self, type, value, tb):
        print(self._now(), 'Bot stopped')


    def _now(self, end='\n') -> str:
        """To return current data/time string"""
        return f'[{datetime.now():%Y-%m-%d %H:%M:%S}]'


    def _isstart(self) -> bool:
        """Has user inputted the start command?"""
        return self.user_input in commands.start
    
    
    def _start(self) -> None:
        """Sends help message"""
        tg.send_message(self.user_id, msg.command_start)


    def _ishelp(self) -> bool:
        """Has user inputted the help command?"""
        return self.user_input in commands.helping
    
    
    def _help(self) -> None:
        """Sends help message"""
        tg.send_message(self.user_id, msg.command_help)


    def _isinteresting(self) -> bool:
        """Has user inputted the interesting command?"""
        return self.user_input in commands.interesting


    def _interesting(self) -> None:
        """Sends interesting message"""
        tg.send_message(self.user_id, msg.command_interesting)


    def _iseaster(self) -> bool:
        """Has user inputted the easter egg command?"""
        return self.user_input in commands.easter


    def _easter(self) -> None:
        """Sends easter egg message"""
        tg.send_message(self.user_id, msg.command_easter)


    def _tell_number(self) -> None:
        """To evaluate user input and send result"""
        bases = {'0b': 2, '0o': 8, '0x': 16}
        base = self.user_input[:2]
        short = base == '0s'
        if short:
            self.user_input = self.user_input[2:]
            base = self.user_input[:2]
        message = random.choice(msg.errors)

        if self.user_input.isdecimal():
            message = translate_num(int(self.user_input), short)
        elif base in bases:
            try:
                dec = int(self.user_input, bases[base])
                message = msg.decimal.format(dec) +\
                    translate_num(dec, short)
            except ValueError: pass
        else:
            ten, _, power = self.user_input.rpartition('*')
            try:
                if ten == '10*':
                    message = translate_10power(int(power))
                elif ten == '10':
                    message = msg.power10_err
            except ValueError: pass
        tg.send_message(self.user_id, message)


    def _get_update_info(self, update: dict) -> None:
        """To set basic self variables"""
        self.last_update_id = update['update_id']
        self.user_id = update['message']['chat']['id']
        self.user_name = update['message']['from']['first_name']
    
    
    def _proceed_text(self) -> None:
        """To analyze text command from user and to act"""
        if self._isstart(): self._start()
        elif self._ishelp(): self._help()
        elif self._isinteresting(): self._interesting()
        elif self._iseaster(): self._easter()
        else: self._tell_number()
            

    def _idle(self) -> None:
        """To react to the non text event"""
        tg.send_message(self.user_id, msg.sticker_reply)


    def listen(self) -> None:
        """To receive updates from the bot and to act"""
        data = tg.get_updates(self.last_update_id + 1)
        if not data: return
        for update in data['result']:
            self._get_update_info(update)
            if 'text' in update['message']:
                self.user_input = update['message']['text']\
                    .lower().strip('/ -!')
                print(self._now(), self.user_name, '-->', self.user_input)
                self._proceed_text()
            else:
                self._idle()


if __name__ == '__main__':
    print(__doc__)
