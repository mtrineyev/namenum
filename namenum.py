"""
Main application for Name the Number Telegram game bot

NameTheNumberBot v2.0 (c) 2020-2023 Maksym Trineyev
mtrineyev@gmail.com
"""

import logging
from src.bot import bot, listener


if __name__ == "__main__":
    logging.info("Bot started and waiting for users input...")
    bot.set_update_listener(listener)
    bot.infinity_polling()
