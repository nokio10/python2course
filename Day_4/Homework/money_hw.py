import requests
import json
from functools import total_ordering
@total_ordering
class Money:
    def __init__(self, main_part: int, minor_part: int):
        if main_part >= 0 and minor_part >= 0:
            if minor_part >= 100:
                self.main_part = main_part + minor_part // 100
                self.minor_part = minor_part % 100
            else:
                self.main_part = main_part
                self.minor_part = minor_part
        else:
            raise ValueError("Натуральные числа вводим по тз")

    def __float__(self):
        return float(str(self.main_part) + '.' + str(self.minor_part))

    def __str__(self):
        return f'{self.main_part}руб {self.minor_part}коп'

    def __lt__(self, other):
        if self.main_part == other.main_part:
            return self.minor_part < other.minor_part

    def __gt__(self, other):
        if self.main_part == other.main_part:
            return self.minor_part > other.minor_part

    def __le__(self, other):
        if self.main_part < other.main_part:
            return True
        elif self.main_part == other.main_part and self.minor_part <= other.minor_part:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.main_part > other.main_part:
            return True
        elif self.main_part == other.main_part and self.minor_part >= other.minor_part:
            return True
        else:
            return False

    def __add__(self, other):
        if self.minor_part + other.minor_part >= 100:
            return f'{self.main_part + other.main_part + ((self.minor_part + other.minor_part) // 100)}руб {(self.minor_part + other.minor_part) % 100}коп'
        else:
            return f'{self.main_part + other.main_part}руб {self.minor_part + other.minor_part}коп'

    def __sub__(self, other):
        if self.main_part > other.main_part:
            if self.minor_part >= other.minor_part:
                return f'{self.main_part - other.main_part}руб {self.minor_part - other.minor_part}коп'
            else:
                return f'{self.main_part - other.main_part -1}руб {self.minor_part + 100 - other.minor_part}коп'
        else:
            if self.main_part == other.main_part and self.minor_part >= other.minor_part:
                return f'{self.main_part - other.main_part}руб {self.minor_part - other.minor_part}коп'
            else:
                return f'Недостаточно средств'

    def __mul__(self, mul):
        return f'{(self.main_part * mul) + ((self.minor_part * mul) // 100)}руб {(self.minor_part * mul) % 100}коп'

    def __mod__(self, percentage):
        total_kopecks = self.main_part * 100 + self.minor_part
        percent_amount = total_kopecks * percentage / 100
        rounded_kopecks = round(percent_amount)
        return Money(rounded_kopecks // 100, rounded_kopecks % 100)

    def convert(self, valuta):
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data_dict = json.loads(response.text)
        result = round((float(self) / (data_dict['Valute'][valuta]['Value'] / data_dict['Valute'][valuta]['Nominal'])), 2)
        return f'{result} {valuta}'
