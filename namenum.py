"""
Main application for Name the Number Telegram game bot

Sets break handler and keeps game running

Stopped by Control-C

NameTheNumberBot v1.0 (c) 2020 Maksym Trineyev
mtrineyev@gmail.com
"""

import logging
from src.bot import bot


def main():
    logging.info("Bot started and waiting for users input...")
    bot.infinity_polling()


if __name__ == "__main__":
    main()
