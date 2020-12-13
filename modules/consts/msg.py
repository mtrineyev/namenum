"""
This module contains all messages for NameTheNumber bot

NameTheNumber bot v1.1 (c) 2020 Maksym Trineyev
mtrineyev@gmail.com
"""


errors = ('🙃', '🤪', '😮', '🤯', '🥺', 'Таких чисел не буває 🤨',
    'Ти точно знаєш, що таке *«натуральне число»*? 🤭', 'Прошу? 🤔',
    'Навіть не знаю, що сказати 😯', 'Може спробуєш ввести гугол? 😉',
    r'Спробуй ввести 10\*\*308760 🤣🤣🤣')
translate_num_key_err = 'На жаль, даних про назву такого великого числа '\
    '[Вікіпедія](https://uk.wikipedia.org/wiki/Іменні_назви_степенів_тисячі) '\
    'не містить 🙅'
power10_err = 'Одна ⭐ це множення, а не ступень. '\
    'Можливо треба ввести дві зірочки❓'
power10_too_big = 'На жаль, точних даних про назву для 10 у степені {} '\
    '[Вікіпедія](https://uk.wikipedia.org/wiki/Іменні_назви_степенів_тисячі) '\
    'не містить 🙅'

command_interesting = '*Цікавинки про натуральні числа:*\n\n'\
    ' 📍 *«Центильйон»* — до початку ХХ сторічча було '\
    'найбільшим числом, що мало усталену назву. '\
    'Вперше його було згадано у 1746 році, де його прирівнюють '\
    'до майже вічності. У 1805 році воно було визначено та у подальшому '\
    'використовувалось, як одиниця з 600 нулями\n\n'\
    ' 📍 Число, яке складається з одиниці і ста нулів '\
    'називається *«гугол»*. Саме на честь нього (англ. googol) Сергій Брін '\
    'і Ларрі Пейдж хотіли назвати свою компанію, але із-за помилки '\
    'при оформленні засновних документів виникла саме та назва, '\
    'яку зараз знають, напевно, всі у світі — Google\n\n'\
    ' 📍 *«Гуголплекс»* (англ. googolplex) це 10 в ступені гугол, '\
    'найбільше іменоване ціле число сьогодення. '\
    'Назви «гугол» та «гуголплекс» придумав племінник американського '\
    'математика Едварда Каснера, Мілтон Сіротта в 1938 році\n\n'\
    ' 📍 Слово «цифра» в перекладі з арабської означає «нуль»\n\n'\
    ' 📍 Подейкують, що 666 – це сума всіх чисел на рулетці казино\n\n'\
    'До речі, бот має пасхалочку 😉'
command_easter = 'Героям слава! 💛💙'
command_help = 'Бот сприймає лише *натуральні числа* та '\
    'знає декілька систем числення.\n\n'\
    ' 📌 Двійкове число починається з *0b*;\n'\
    ' 📌 Вісімкове число починається з *0o*;\n'\
    ' 📌 Шістнадцяткове — з *0x*.\n\n'\
    'Також бот розуміє степені десятки у вигляді '\
    r'*10*\*\**n*, де _n_ — натуральне число.''\n\n'\
    '❗ Якщо набрати число з *0s* на початку, то буде виведено його '\
    'назву в скороченному варіанті (це не працює зі степенями 10).\n\n'\
    'Найменування багатозначних чисел виконується за правилом '\
    '*«N-1»* (або *«коротким правилом»*), що взяте з '\
    '[Вікіпедії](https://uk.wikipedia.org/wiki/Іменні_назви_степенів_тисячі).'\
    '\n\nПро різноманітні системи числення можна почитати у '\
    '[Вікіпедії](https://uk.wikipedia.org/wiki/Система_числення).'\
    '\n\n⚠ *Натура́льні чи́сла* — числа, '\
    'що виникають природним чином при лічбі.'
command_start = 'Вітаю! Введи будь-яке *натуральне число*. Я назву його, '\
    'а ти спробуй не зламати язика, коли будеш його читати 😉'

decimal = '= {0:,d}\n\n'

sticker_reply = '🗿'
under_construction = '⚠ Наразі в розробці'


if __name__ == '__main__':
    print(__doc__)
