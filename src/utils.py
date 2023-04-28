"""
Translates natural NUMBERS as well as powers of 10 into their nominal names

Functions:
    detect(text: str, patterns: list | tuple) -> bool
        Find any pattern in the text

    prune(text: str, patterns: list | tuple) -> str
        Deletes all patterns from the text

    words(value: int, short=False, uah=False) -> str
        To convert integer to its nominal name
    
    translate_10power(value: int) -> str:
        To return power of 10 name

NameTheNumberBot v2.0 (c) 2020-2023 Maksym Trineyev
mtrineyev@gmail.com
"""

from src.thesaurus.messages import TRANSLATE_NUM_KEY_ERR, POWER10_TOO_BIG


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


def words(value: int, short=False, uah=False) -> str:
    """To convert big integer to its nominal name"""
    result = ""
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
    return result.capitalize()


def _correct_small_plural(text: str, word1: str, word2: str) -> str:
    return text.replace(f"один {word1}", f"одна {word1}")\
        .replace(f"два {word2}", f"дві {word2}")


def translate_10power(value: int) -> str:
    """To return power of 10 nominal name"""
    if value in POWERS10:
        result = f"{POWERS10[value][0]}"
    elif value - 1 in POWERS10:
        result = f"{NUMBERS[10]} {POWERS10[value - 1][2]}"
    elif value - 2 in POWERS10:
        result = f"{NUMBERS[100]} {POWERS10[value - 2][2]}"
    else:
        return POWER10_TOO_BIG.format(value)
    return result.capitalize()


def detect(text: str, patterns: list | tuple) -> bool:
    return any([p in text.lower() for p in patterns])


def prune(text: str, patterns: list | tuple) -> str:
    stripped = text.lower()
    for pattern in patterns:
        stripped = stripped.replace(pattern, "")
    return stripped


def decimal_str(number: int, uah: bool) -> str:
    result = f"\\= {number:,d}"
    return _add_uah(result, uah) + "\n\n"


def float_str(number: float, uah: bool) -> str:
    result = f"\\= {int(number):,d}"
    result += f"{number-int(number):.2f}".replace(".", r"\.")[1:]
    return _add_uah(result, uah) + "\n\n"


def _add_uah(text: str, uah: bool) -> str:
    return text + (r" грн\." if uah else "")


if __name__ == "__main__":
    print(__doc__)
