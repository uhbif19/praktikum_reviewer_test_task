# Ваш код не соответвует стандартам оформления кода PEP8.
# Например, не хватает пробелов перед операторами и пустых строк между
# определениями функций. Несколько строк превышают лимит длинны в 79 символов.

# Пожалуйста используйте, например, линтер pycodestyle.
# https://github.com/PyCQA/pycodestyle#installation
# При запуске следующей коммандой `pycodestyle --show-source --show-pep8`
# он не только перечислит ошибки, но и подскажет как их лучше исправить.

import datetime as dt
import json

class Record:
    def __init__(self, amount, comment, date=''):
        self.amount=amount
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        self.comment=comment
class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records=[]
    def add_record(self, record):
        self.records.append(record)
    def get_today_stats(self):
        today_stats=0
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                today_stats = today_stats+Record.amount
        return today_stats
    def get_week_stats(self):
        week_stats=0
        today = dt.datetime.now().date()

        # Возможно написать это чуть проще:
        # sum(
        #     record.amount for record in self.records
        #     if 0 <= (today -  record.date).days < 7
        # )

        for record in self.records:
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                week_stats +=record.amount
        return week_stats
class CaloriesCalculator(Calculator):
    # Комментарии к функции пишутся в docstring
    def get_calories_remained(self): # Получает остаток калорий на сегодня
        # Лучше вынести `self.limit-self.get_today_stats()` в отдельную функцию класса
        # Calculator. Этот код повторяется в двух методах. При этом он (в теории)
        # может поменяется именно при изменении устройства класса Calculator - например,
        # если изменится метод подсчета.


        x=self.limit-self.get_today_stats()
        if x > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        else:
            return 'Хватит есть!'
class CashCalculator(Calculator):
    # Деньги нельзя хранить в float. Тип данных float весьма специфично округляет
    # числа, это может приводить к странным результатам.

    # Есть сайт освещающий этот вопрос: https://0.30000000000000004.com/

    # Для точных вычислений нужно использовть тип decimal. Он округляет в соответвии
    # с обычной, школьной, арифметикой
    # https://docs.python.org/3/library/decimal.html

    USD_RATE=float(60) #Курс доллар США.
    EURO_RATE=float(70) #Курс Евро.
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        currency_type=currency
        cash_remained = self.limit - self.get_today_stats()

        # Блок с if следует логически отделить пустыми строками. Это предписанно
        # требованиями к оформлению кода этого курса.

        if currency=='usd':
            cash_remained /= USD_RATE
            currency_type ='USD'
        elif currency_type=='eur':
            cash_remained /= EURO_RATE
            currency_type ='Euro'
        elif currency_type=='rub':

            # Строка `cash_remained == 1.00` ничего не делает. Ее нужно убрать.

            cash_remained == 1.00
            currency_type ='руб'
        if cash_remained > 0:
            return f'На сегодня осталось {round(cash_remained, 2)} {currency_type}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        elif cash_remained < 0:
            # Необходимо использовать один способ форматирования внутри вашей программы.
            # Это предписанно требованиями к оформлению кода этого курса.

            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)

    def get_week_stats(self):
        # Эта функция и так наследуется, вызов ее через `super()` ничего не делает.
        # Этот код лишний, и его нужно убрать.
        super().get_week_stats()
