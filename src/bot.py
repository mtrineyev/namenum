"""
Game logic for Telegram bot

bot - Telegram bot variable

NameTheNumberBot v2.0 (c) 2020-2023 Maksym Trineyev
mtrineyev@gmail.com
"""

import logging
import random
from telebot import TeleBot

from settings import BOT_TOKEN
from src.thesaurus.commands import (
    HELP, EASTER, START, INTERESTING, SHORTS, UAH
)
from src.thesaurus.messages import (
    INTERESTING_MSG, ERRORS, START_MSG, HELP_MSG, EASTER_MSG,
    STICKER_REPLY, EVAL_ERR, POWER10_WRONG_POWER
)
from src.utils import (
    words, translate_10power, detect, prune,
    format_num, factorial, is_factorial
)

bot = TeleBot(
    BOT_TOKEN, parse_mode="MarkdownV2", disable_web_page_preview=True)


@bot.message_handler(commands=START)
def start_command(message) -> None:
    bot.send_message(
        message.chat.id, START_MSG.format(message.from_user.first_name))


@bot.message_handler(commands=HELP)
def help_command(message) -> None:
    bot.send_message(message.chat.id, HELP_MSG)


@bot.message_handler(commands=INTERESTING)
@bot.message_handler(
    func=lambda m: any([w == m.text.lower() for w in INTERESTING]))
def interesting_command(message) -> None:
    bot.send_message(message.chat.id, INTERESTING_MSG)


@bot.message_handler(
    func=lambda m: any([w in m.text.lower() for w in EASTER]))
def easter(message) -> None:
    bot.send_message(message.chat.id, EASTER_MSG)


@bot.message_handler(content_types=["text"])
def tell_number(message) -> None:
    bot.send_chat_action(message.chat.id, 'typing')
    user_input = message.text
    if short := detect(user_input, SHORTS):
        user_input = prune(user_input, SHORTS)
    if uah := detect(user_input, UAH):
        user_input = prune(user_input, UAH)
    user_input = user_input.strip()
    ten, _, power = user_input.rpartition("@")
    if user_input.isdecimal():
        reply = words(int(user_input), short, uah)
    elif ten == "10":
        reply = ten_power(power)
    else:
        reply = my_eval(user_input, short, uah)
    bot.send_message(message.chat.id, reply)


def ten_power(power: str) -> str:
    try:
        return translate_10power(int(power))
    except ValueError:
        return POWER10_WRONG_POWER


def my_eval(text: str, short: bool, uah: bool) -> str:
    try:
        value = (factorial(int(text[:-1]))
                 if is_factorial(text) else eval(text))
        if isinstance(value, int) or isinstance(value, float):
            return (format_num(value, uah) +
                    words(int(round(value, 0)), short, uah))
        else:
            raise ValueError
    except (SyntaxError, ZeroDivisionError, TypeError, ValueError):
        return EVAL_ERR
    except NameError:
        return random.choice(ERRORS)


@bot.message_handler(content_types=[
    "audio", "document", "photo", "sticker",
    "video", "voice", "location", "contact"])
def sticker_reply(message):
    bot.send_message(message.chat.id, STICKER_REPLY)


def listener(messages):
    for m in messages:
        if m.content_type == 'text':
            logging.info(f"{m.from_user.first_name=} ({m.chat.id=}): {m.text=}")


if __name__ == "__main__":
    print(__doc__)
