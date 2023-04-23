"""
Game logic for Telegram bot

bot - Telegram bot variable

NameTheNumberBot v2.0 (c) 2020-2023 Maksym Trineyev
mtrineyev@gmail.com
"""

import logging
import random
import telebot

from settings import BOT_TOKEN
from src.thesaurus.commands import HELP, EASTER, START, INTERESTING
from src.thesaurus.messages import (
    INTERESTING_MSG, ERRORS, START_MSG, HELP_MSG, DECIMAL, FLOAT, EASTER_MSG,
    STICKER_REPLY, EVAL_ERR, POWER10_WRONG_POWER
)
from src.utils import words, translate_10power


bot = telebot.TeleBot(BOT_TOKEN, parse_mode="MarkdownV2")


@bot.message_handler(commands=START)
def start_command(message) -> None:
    bot.send_message(
        message.from_user.id, START_MSG.format(message.from_user.first_name))


@bot.message_handler(commands=HELP)
def help_command(message) -> None:
    bot.send_message(
        message.from_user.id, HELP_MSG, disable_web_page_preview=True)


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
    if need_short := user_input[:2] == "0s":
        user_input = message.text[2:]
    ten, _, power = user_input.rpartition("@")
    if user_input.isdecimal():
        reply = words(int(user_input), need_short)
    elif ten == "10":
        try:
            reply = translate_10power(int(power))
        except ValueError:
            reply = POWER10_WRONG_POWER
    else:
        try:
            value = eval(user_input)
            if isinstance(value, int):
                reply = DECIMAL.format(value) + words(value, need_short)
            elif isinstance(value, float):
                bot.send_message(
                    message.from_user.id,
                    FLOAT.format(value) +
                    words(int(round(value, 0)), need_short),
                    parse_mode="HTML")
                return
            else:
                reply = EVAL_ERR
        except (SyntaxError, NameError, ValueError):
            reply = random.choice(ERRORS)
    bot.send_message(
        message.from_user.id, reply, disable_web_page_preview=True)
    logging.info(f"{message.from_user.first_name=}, {message.text=}")


@bot.message_handler(content_types=[
    "audio", "document", "photo", "sticker",
    "video", "voice", "location", "contact"])
def sticker_reply(message):
    bot.send_message(message.from_user.id, STICKER_REPLY)


if __name__ == "__main__":
    print(__doc__)
