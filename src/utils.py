"""
Translates natural NUMBERS as well as powers of 10 into their nominal names

Functions:
    get_ten_power(text: str) -> str
        Returns power of 10 name

    my_eval(text: str, short: bool, uah: bool) -> str
        Evaluates text, calculates factorial if necessary,
        formats result as short or/and uah

    parse(text: str) -> tuple
        Finds "short" and "uah" in text and delete them
        returns stripped text, short and uah

    words(value: int, short=False, uah=False) -> str
        Converts integer to its nominal name
    
NameTheNumberBot v2.0 (c) 2020-2023 Maksym Trineyev
mtrineyev@gmail.com
"""
from random import choice

from src.thesaurus.commands import SHORTS, UAH
from src.thesaurus.messages import (
    TRANSLATE_NUM_KEY_ERR, POWER10_TOO_BIG, POWER10_WRONG_POWER,
    EVAL_ERR, ERRORS
)


NUMBERS = {
    0: "нуль",
    1: "один",
    2: "два",
    3: "три",
    4: "чотири",
    5: "п'ять",
    6: "шість",
    7: "сім",
    8: "вісім",
    9: "дев'ять",
    10: "десять",
    11: "одинадцять",
    12: "дванадцять",
    13: "тринадцять",
    14: "чотирнадцять",
    15: "п'ятнадцять",
    16: "шістнадцять",
    17: "сімнадцять",
    18: "вісімнадцять",
    19: "дев'ятнадцять",
    20: "двадцять",
    30: "тридцять",
    40: "сорок",
    50: "п'ятдесят",
    60: "шістдесят",
    70: "сімдесят",
    80: "вісімдесят",
    90: "дев'яносто",
    100: "сто",
    200: "двісті",
    300: "триста",
    400: "чотириста",
    500: "п'ятсот",
    600: "шістсот",
    700: "сімсот",
    800: "вісімсот",
    900: "дев'ятсот",
}

POWERS10 = {
    0: ("один", "один", "один"),
    1: ("десять", "десять", "десять"),
    2: ("сто", "сотні", "сотень"),
    3: ("тисяча", "тисячі", "тисяч"),
    6: ("мільйон", "мільйони", "мільйонів"),
    9: ("мільярд", "мільярди", "мільярдів"),
    12: ("трильйон", "трильйони", "трильйонів"),
    15: ("квадрильйон", "квадрильйони", "квадрильйонів"),
    18: ("квінтильйон", "квінтильйони", "квінтильйонів"),
    21: ("секстильйон", "секстильйони", "секстильйонів"),
    24: ("септильйон", "септильйони", "септильйонів"),
    27: ("октильйон", "октильйони", "октильйонів"),
    30: ("нонильйон", "нонильйони", "нонильйонів"),
    33: ("децильйон", "децильйони", "децильйонів"),
    36: ("ундецильйон", "ундецильйони", "ундецильйонів"),
    39: ("дуодецильйон", "дуодецильйони", "дуодецильйонів"),
    42: ("тредецильйон", "тредецильйони", "тредецильйонів"),
    45: ("кваттуордецильйон", "кваттуордецильйони", "кватордецильйонів"),
    48: ("квіндецильйон", "квіндецильйони", "квіндецильйонів"),
    51: ("седецильйон", "седецильйони", "седецильйонів"),
    54: ("септдецильйон", "септдецильйони", "септдецильйонів"),
    57: ("дуодевігінтильйон", "дуодевігінтильйони", "дуодевігінтильйонів"),
    60: ("ундевігінтильйон", "ундевігінтильйони", "ундевігінтильйонів"),
    63: ("вігінтильйон", "вігінтильйони", "вігінтильйонів"),
    66: ("анвігінтильйон", "анвігінтильйони", "анвігінтильйонів"),
    69: ("дуовігінтильйон", "дуовігінтильйони", "дуовігінтильйонів"),
    72: ("тревігінтильйон", "тревігінтильйони", "тревігінтильйонів"),
    75: ("кватторвігінтильйон", "кватторвігінтильйони",
         "кватторвігінтильйонів"),
    78: ("квінвігінтильйон", "квінвігінтильйони", "квінвігінтильйонів"),
    81: ("сексвігінтильйон", "сексвігінтильйони", "сексвігінтильйонів"),
    84: ("септемвігінтильйон", "септемвігінтильйони",
         "септемвігінтильйонів"),
    87: ("октовігінтильйон", "октовігінтильйони", "октовігінтильйонів"),
    90: ("новемвігінтильйон", "новемвігінтильйони", "новемвігінтильйонів"),
    93: ("трігінтильйон", "трігінтильйони", "трігінтильйонів"),
    96: ("антрігінтильйон", "антрігінтильйони", "антрігінтильйонів"),
    99: ("дуотрігінтильйон", "дуотрігінтильйони", "дуотрігінтильйонів"),
    100: ("гугол", "гуголи", "гуголів"),
    102: ("третрігінтильйон", "третрігінтильйони", "третрігінтильйонів"),
    105: ("кваттортрігінтильйон", "кваттортрігінтильйони",
          "кваттортрігінтильйонів"),
    108: ("квінтрігінтильйон", "квінтрігінтильйони", "квінтрігінтильйонів"),
    111: ("секстрігінтильйон", "секстрігінтильйони", "секстрігінтильйонів"),
    114: ("септемтрігінтильйон", "септемтрігінтильйони",
          "септемтрігінтильйонів"),
    117: ("октотрігінтильйон", "октотрігінтильйони", "октотрігінтильйонів"),
    120: ("новемтрігінтильйон", "новемтрігінтильйони",
          "новемтрігінтильйонів"),
    123: ("квадрагінтильйон", "квадрагінтильйони", "квадрагінтильйонів"),
    153: ("квінквагінтильйон", "квінквагінтильйони", "квінквагінтильйонів"),
    183: ("сексагінтильйон", "сексагінтильйони", "сексагінтильйонів"),
    213: ("септуагінтильйон", "септуагінтильйони", "септуагінтильйонів"),
    243: ("октогінтильйон", "октогінтильйони", "октогінтильйонів"),
    273: ("нонагінтильйон", "нонагінтильйони", "нонагінтильйонів"),
    600: ("центильйон", "центильйони", "центильйонів"),
    603: ("дуцентильйон", "дуцентильйони", "дуцентильйонів"),
    606: ("трецентильйон", "трецентильйони", "трецентильйонів"),
    609: ("кватторцентильйон", "кватторцентильйони", "кватторцентильйонів"),
    666: ("😈", "😈", "😈"),
    1991: ("Згинуть наші вороженьки, як роса на сонці\\! ❤️🇺🇦",
           "Згинуть наші вороженьки, як роса на сонці\\! ❤️🇺🇦",
           "Згинуть наші вороженьки, як роса на сонці\\! ❤️🇺🇦",),
    308760: ("дуцентдуоміліанонгентновемдецільйон",
             "дуцентдуоміліанонгентновемдецільйони",
             "дуцентдуоміліанонгентновемдецільйонів"),
}

HRIVNAS = ("гривня", "гривні", "гривень")


def words(value: int, short=False, uah=False) -> str:
    """To convert big integer to its nominal name"""
    result = ""
    minus = ""
    if value < 0:
        minus = "Мінус "
        value = - value
    grades = f"{value:,d}".split(",")
    grade_pow = (len(grades) - 1) * 3
    for grade in grades:
        n = int(grade)
        if n or not result:
            result += _hundreds(n, short)
            if grade_pow:
                try:
                    result += _plural(n, POWERS10[grade_pow])
                except KeyError:
                    return TRANSLATE_NUM_KEY_ERR
        grade_pow -= 3
    result = _correct_small_plural(result, "тисяча", "тисячі")
    if uah:
        result += _plural(int(grades[-1]), HRIVNAS)
        result = _correct_small_plural(result, "гривня", "гривні")
    return f"{minus}{result}".capitalize()


def _plural(amount: int, plurals: tuple) -> str:
    """Returns corresponding plural from the tuple to 1, 2, 5 principal"""
    if amount == 0:
        return ""
    mod = amount % 100
    if mod > 20:
        mod %= 10
    if mod == 1:
        result = plurals[0]
    elif mod in (2, 3, 4):
        result = plurals[1]
    else:
        result = plurals[2]
    return f" {result} "


def _hundreds(value: int, short: bool) -> str:
    """Convert small int to its nominal name or just return str"""
    if short:
        return str(value)
    if not value:
        return NUMBERS[0]
    result = ""
    hundreds, tens = divmod(value, 100)
    if hundreds:
        result = f"{NUMBERS[hundreds * 100]} "
    if 0 < tens <= 20:
        result += NUMBERS[tens]
    elif tens:
        tens, units = divmod(tens, 10)
        result += NUMBERS[tens * 10]
        if units:
            result += f" {NUMBERS[units]}"
    return result.strip()


def _correct_small_plural(text: str, word1: str, word2: str) -> str:
    return text.replace(f"один {word1}", f"одна {word1}")\
        .replace(f"два {word2}", f"дві {word2}")


def get_ten_power(power: str) -> str:
    try:
        value = int(power)
    except ValueError:
        return POWER10_WRONG_POWER
    if value in POWERS10:
        result = f"{POWERS10[value][0]}"
    elif value - 1 in POWERS10:
        result = f"{NUMBERS[10]} {POWERS10[value - 1][2]}"
    elif value - 2 in POWERS10:
        result = f"{NUMBERS[100]} {POWERS10[value - 2][2]}"
    else:
        return POWER10_TOO_BIG.format(value)
    return result.capitalize()


def parse(text: str) -> tuple:
    user_input = text
    if short := _detect(user_input, SHORTS):
        user_input = _prune(user_input, SHORTS)
    if uah := _detect(user_input, UAH):
        user_input = _prune(user_input, UAH)
    return user_input.strip(), short, uah


def _detect(text: str, patterns) -> bool:
    return any([p in text.lower() for p in patterns])


def _prune(text: str, patterns) -> str:
    stripped = text.lower()
    for pattern in patterns:
        stripped = stripped.replace(pattern, "")
    return stripped


def my_eval(text: str, short: bool, uah: bool) -> str:
    try:
        value = (factorial(int(text[:-1]))
                 if is_factorial(text) else eval(text))
        if isinstance(value, int) or isinstance(value, float):
            return (_format_num(value, uah) +
                    words(int(round(value, 0)), short, uah))
        else:
            raise ValueError
    except (SyntaxError, ZeroDivisionError, TypeError, ValueError):
        return EVAL_ERR
    except NameError:
        return choice(ERRORS)


def factorial(n: int) -> int:
    if n < 0 or n > 1000:
        raise ValueError
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_factorial(text: str) -> bool:
    return text[-1] == "!" and text[:-1].isdecimal()


def _format_num(number: float, uah: bool) -> str:
    result = f"\\= {int(number):,d}".replace("-", r"\-")
    if isinstance(number, float):
        result += f"{number-int(number):.2f}".replace(".", r"\.")[1:]
    return _add_uah(result, uah) + "\n\n"


def _add_uah(text: str, uah: bool) -> str:
    return text + (r" грн\." if uah else "")


if __name__ == "__main__":
    print(__doc__)
