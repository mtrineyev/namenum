"""
This module contains all messages for NameTheNumber bot

NameTheNumberBot v2.0 (c) 2020-2023 Maksym Trineyev
mtrineyev@gmail.com
"""

START_MSG = (
    r"Вітаю, {0}\!""\n\n"
    r"Введи будь\-яке *натуральне число*\ або *арифметичний вираз* і "
    "я назву його, а ти спробуй не зламати язика, коли будеш це вимовляти 😉"
)
HELP_MSG = (
    r"Бот розпізнає *натуральні числа* \(тобто числа, "
    r"що виникають природним чином при лічбі\), або "
    "*арифметичні вирази*, навіть з використанням різних "
    r"[систем числення](https://uk.wikipedia.org/wiki/Система_числення)\."
    "\n\n 🔹 _Двійкове_ число починається з *0b*;\n"
    " 🔹 _Вісімкове_ число починається з *0o*;\n"
    r" 🔹 _Шістнадцяткове_ — з *0x*\."
    "\n\nТакож бот розуміє степені десятки у вигляді "
    r"*10\@n*, де _n_ — натуральне число \(напр\. 10\@100\)\."
    "\n\n||ℹ️ Якщо до виразу додати слово *short*, то буде виведено назву "
    "числа в скороченому варіанті\n"
    "ℹ️ Якщо до виразу додати слово *uah*, то результат буде інтерпретовано "
    r"як гривні\. Це може бути зручно для пересилання "
    "фінансового розрахунку іншим користувачам\n"
    "ℹ️ Вищевказані опції не працюють зі степенями 10||"
    "\n\nНайменування багатозначних чисел виконується за "
    "[коротким правилом]"
    r"(https://uk.wikipedia.org/wiki/Іменні_назви_степенів_тисячі)\."
    "\n\nБот підтримує такі команди:\n"
    "😺 /interesting — цікавинки про числа"
)
INTERESTING_MSG = (
    "*Цікавинки про натуральні числа:*\n\n"
    " 📍 *«Центильйон»* — до початку ХХ сторіччя було "
    r"найбільшим числом, що мало усталену назву\. "
    "Вперше його було згадано у 1746 році, де його прирівнюють "
    r"до майже вічності\. У 1805 році воно було визначено та у подальшому "
    "використовувалось, як одиниця з 600 нулями\n\n"
    " 📍 Число, яке складається з одиниці і ста нулів називається "
    r"*«гугол»*\. Саме на честь нього \(англ\. googol\) Сергій Брін "
    r"і Ларрі Пейдж хотіли назвати свою компанію, але із\-за помилки "
    "при оформленні засновних документів виникла саме та назва, "
    "яку зараз знають, напевно, всі у світі — Google\n\n"
    r" 📍 *«Гуголплекс»* \(англ\. googolplex\) це 10 в ступені гугол, "
    r"найбільше іменоване ціле число сьогодення\. "
    "Назви «гугол» та «гуголплекс» придумав племінник американського "
    "математика Едварда Каснера, Мілтон Сіротта в 1938 році\n\n"
    " 📍 *«Число Шеннона»*, це приблизна мінімальна кількість "
    r"неповторюваних шахових партій — новемтрігінтильйон \(10\*\*120\), "
    "це більше, ніж атомів у спостережуваному Всесвіті, що за середніми "
    r"оцінками складає сто квінвігінтильйонів \(10\*\*80\)\!""\n\n"
    " 📍 Тіло 70 кг людини в середньому складається з шестисот октильйонів "
    r"семисот септильйонів \(6,7×10\*\*27\) атомів""\n\n"
    " 📍 Подейкують, що 666 — це сума всіх чисел на рулетці казино 😈\n\n"
    "||До речі, бот має пасхалочки, спробуй їх відшукати 😉||"
)
EASTER_MSG = r"Героям слава\! 💙💛"

ERRORS = (
    "🙃", "🤪", "😮", "🤯", "👄", "Таких чисел не буває 🤨",
    r"Ти точно знаєш, що таке *«натуральне число»*\? 🤭", r"Прошу\? 🤔",
    "Навіть не знаю, що сказати 😯", r"Може спробуєш ввести *гугол*\? 😉",
    r"Спробуй ввести *10\*\*308760* 🤣",
)
EVAL_ERR = "Не можу обчислити арифметичний вираз 🥺"
TRANSLATE_NUM_KEY_ERR = (
    "На жаль, даних про назву такого великого числа "
    "[Вікіпедія](https://uk.wikipedia.org/wiki/Іменні_назви_степенів_тисячі) "
    "не містить 🙅"
)
POWER10_WRONG_POWER = r"Неправильний ступень десяти\.\.\."
POWER10_TOO_BIG = (
    "На жаль, точних даних про назву для 10 у степені {} "
    "[Вікіпедія](https://uk.wikipedia.org/wiki/Іменні_назви_степенів_тисячі) "
    "не містить 🙅"
)

STICKER_REPLY = "🗿"
UNDER_CONSTRUCTION = "⚠ Наразі в розробці"


if __name__ == "__main__":
    print(__doc__)
