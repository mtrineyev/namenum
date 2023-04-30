"""
Game logic for Telegram bot

bot - Telegram bot variable

NameTheNumberBot v2.0 (c) 2020-2023 Maksym Trineyev
mtrineyev@gmail.com
"""

import logging
from telebot import TeleBot

from settings import BOT_TOKEN
from src.thesaurus.commands import HELP, EASTER, START, INTERESTING
from src.thesaurus.messages import (
    INTERESTING_MSG, START_MSG, HELP_MSG, EASTER_MSG, STICKER_REPLY
)
from src.utils import get_ten_power, my_eval, parse, words

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
    parsed, short, uah = parse(message.text)
    ten, _, power = parsed.rpartition("@")
    if parsed.isdecimal():
        reply = words(int(parsed), short, uah)
    elif ten == "10":
        reply = get_ten_power(power)
    else:
        reply = my_eval(parsed, short, uah)
    bot.send_message(message.chat.id, reply)


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
