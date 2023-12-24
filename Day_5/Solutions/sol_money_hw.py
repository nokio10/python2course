"""
class Money

Напишите класс для работы с денежными суммами.

Реализовать:
*   сложение
*   вычитание
*   умножение на целое число
*   сравнение (больше, меньше, равно, не равно)

==========================================================================================
from functools import total_ordering
Описываемый декоратор, позволяет для классов, в которых определён __eq__(), а также один из
__lt__(), __gt__(), __le__(), __ge__(), сгенерировать остальные методы автоматически.

    @total_ordering
    class Student:

        def __eq__(self, other):
            return self.last_name == other.last_name

        def __lt__(self, other):
            return self.last_name < other.last_name

=========================================================================================

При всех операциях, сумма должна преобразовываться к сумме с минимальным количеством копеек.

Примеры:
# Создаем сумму из 20 рублей и 120 копеек
money1 = Money(20, 120)  # в конструктор можно передать два любых натуральных числа

# Выводим сумму, с учетом минимального кол-ва копеек <= 99 коп
print(money1) # 21руб 20коп


# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(10, 45)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 5коп



Примечание: список всех методов для перегрузки операций: (https://pythonworld.ru/osnovy/peregruzka-operatorov.html).


#### Дополнительные задания **

Добавьте операцию - вычисление процента от суммы. %

Пример:

# Создаем две денежные суммы
money1 = Money(20, 60)

# Находим 21% от суммы
percent_money = money1 % 21

print(percent_money)  # 4руб 33коп

__mod__()
Пояснение: % (процент от суммы) - должна являться новая денежная сумма.
После вычисления процента, используем округление (функция round())


### Конвертация валют

Доработайте класс Money, добавив ему метод .convert("EUR"), для конвертации суммы в рублях в евро и доллары(*любую валюту).
Актуальные значения можно взять, сделав запрос на: https://www.cbr-xml-daily.ru/daily_json.js

#### Отправка запроса на url-адрес

pip install requests
py -m pip install requests
import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)

, где url - адрес сайта, на который отправляете запрос.

В переменную response получите ответ сайта.

Для преобразования ответа из json-формата используйте функцию:

import json
data_dict = json.loads(response.text)

Модуля json

print(data_dict['Valute']['EUR']['Value'])
"""
import math
from functools import total_ordering
import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
RATES = json.loads(response.text)


@total_ordering
class Money:
    def __init__(self, rub, kop):
        self.total_kop = rub * 100 + kop

    def __repr__(self):
        rub, kop = divmod(self.total_kop, 100)
        return f'Money({rub}руб {kop:02}коп)'

    def __str__(self):
        rub, kop = divmod(self.total_kop, 100)
        return f'Money({rub}руб {kop:02}коп)'

    def __eq__(self, other):
        return self.total_kop == other.total_kop

    def __lt__(self, other):
        return self.total_kop < other.total_kop

    def __add__(self, other):
        return Money(0, self.total_kop + other.total_kop)

    def __sub__(self, other):
        return Money(0, self.total_kop - other.total_kop)

    def __mod__(self, percent: int):
        total = round(self.total_kop * percent / 100)
        return Money(0, total)

    def convert(self, currency):
        name = RATES['Valute'][currency]['Name']
        nominal = RATES['Valute'][currency]['Nominal']
        conv = (self.total_kop / 100 * nominal) / (RATES['Valute'][currency]['Value'])
        return f'{name}: {math.floor(conv * 100) / 100}{currency}'


money1 = Money(20, 120)
print(money1)  # 21руб 20коп


# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(10, 45)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 05коп

# Вычитаем суммы
money4 = money1 - money2
print(money4)  #

# Создаем две денежные суммы
money1 = Money(20, 60)

# Находим 20% от суммы
percent_money = money1 % 20

print(percent_money)  # 4руб 12коп

print('Операции сравнения')
print(money1 == money2)
print(money1 != money2)
print(money1 < money2)
print(money1 <= money2)
print(money1 > money2)
print(money1 >= money2)

money1 = Money(2000, 0)
print(money1.convert('EUR'))
print(money1.convert('USD'))
print(money1.convert('AUD'))
print(money1.convert('AZN'))
print(money1.convert('GBP'))
print(money1.convert('HUF'))
print(money1.convert('INR'))
