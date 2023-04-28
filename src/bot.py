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
    words, translate_10power, detect, prune, decimal_str, float_str
)


bot = TeleBot(
    BOT_TOKEN, parse_mode="MarkdownV2", disable_web_page_preview=True)


@bot.message_handler(commands=START)
def start_command(message) -> None:
    bot.send_message(
        message.from_user.id, START_MSG.format(message.from_user.first_name))


@bot.message_handler(commands=HELP)
def help_command(message) -> None:
    bot.send_message(
        message.from_user.id, HELP_MSG)


@bot.message_handler(commands=INTERESTING)
@bot.message_handler(
    func=lambda m: any([w == m.text.lower() for w in INTERESTING]))
def interesting_command(message) -> None:
    bot.send_message(message.from_user.id, INTERESTING_MSG)


@bot.message_handler(
    func=lambda m: any([w in m.text.lower() for w in EASTER]))
def easter(message) -> None:
    bot.send_message(message.from_user.id, EASTER_MSG)


@bot.message_handler(content_types=["text"])
def tell_number(message) -> None:
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
        try:
            reply = translate_10power(int(power))
        except ValueError:
            reply = POWER10_WRONG_POWER
    else:
        try:
            value = eval(user_input)
            if isinstance(value, int):
                reply = decimal_str(value, uah) + words(value, short, uah)
            elif isinstance(value, float):
                reply = (float_str(value, uah) +
                         words(int(round(value, 0)), short, uah))
            else:
                reply = EVAL_ERR
        except (SyntaxError, NameError, ValueError):
            reply = random.choice(ERRORS)
    bot.send_message(
        message.from_user.id, reply)
    logging.info(f"{message.from_user.first_name=}, {message.text=}")


@bot.message_handler(content_types=[
    "audio", "document", "photo", "sticker",
    "video", "voice", "location", "contact"])
def sticker_reply(message):
    bot.send_message(message.from_user.id, STICKER_REPLY)


if __name__ == "__main__":
    print(__doc__)
