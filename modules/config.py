"""
Settings for Telegram bot

Constants:

    TOKEN - bot token
    TG_API - Telegram API url adress

NameTheNumberBot v1.0 (c) 2020 Maksym Trineyev
mtrineyev@gmail.com
"""

tg_setname = """
🗣 Назви число
"""

tg_setabouttext = """
🤖 "Назви Число" 🗣
автор @mtrineyev
"""

tg_setdescription = """
Розважально-навчальний 🤖 назве будь-яке натуральне число, а також переведе двійкове, вісімкове чи шістнадцяткове число у десяткове. Тисни /start і переконайся 😉
"""

tg_setcommands = """
interesting - Цікавинки про числа
help - Додаткова інформація
"""

import prod

TOKEN = prod.token
# @NameTheNumberBot


TG_API = f'https://api.telegram.org/bot{TOKEN}'
# Telegram API url adress


if __name__ == "__main__":
    print(__doc__)
