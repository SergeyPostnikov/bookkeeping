import sys

from datetime import datetime, date, timedelta
from textwrap import dedent

from . import helpers as h
from . import storage
from .services import make_connection

def add_payment():
    """Добавить платеж"""
    with make_connection() as conn:
        namepay = input('Введите наименование платежа: ').strip()
        price = h.input_float('Введите стоимость единицы товара')
        count = h.input_int('Введите количество товара', default=1)
        timepoint = h.input_date(default=datetime.date(datetime.today()))
        storage.sql_add_payment(conn, namepay, price, timepoint, count)

def edit_payment():
    """Отредактировать платеж"""
    with make_connection() as conn:
        namepay = input('Введите наименование платежа: ').strip()
        price = h.input_float('Введите стоимость единицы товара: ')
        count = h.input_int('Введите количество товара', default=1)
        timepoint = h.input_date(default=datetime.date(datetime.today()))
        pk = h.input_int('Введите Id платежа')
        storage.update_payment(conn, pk, namepay, price, timepoint, count)

def print_payments():
    """Вывести все платежи за указанный период"""
    dt_start = h.input_date(msg='Введите дату начала периода', default=datetime.date(datetime.today()))
    dt_end = h.input_date(msg='Введите дату окончания периода')
    if dt_end is None:
        dt_end = dt_start + timedelta(days=1)
    with make_connection() as conn:
        payments = (storage.select_payments_on_period(conn, dt_start, dt_end))
        h.print_table(
        [
            'ID', 'Название', 'Цена',
            'Дата внесения', 'Количество'
        ],
        payments
    )


def print_top_payments():
    """Вывести топ самых крупных платежей"""
    with make_connection() as conn:
        top_payments = storage.select_top_payments(conn)
        h.print_table(
        [
            'ID', 'Название', 'Цена',
            'Дата внесения', 'Количество'
        ],
        top_payments
    )

def print_all_payments():
    """Вывести все платежи"""
    with make_connection() as conn:
        payments = storage.select_all_payments(conn)
        h.print_table(
        [
            'ID', 'Название', 'Цена',
            'Дата внесения', 'Количество'
        ],
        payments
    )


def show_menu():
    """Показать меню"""
    print(dedent(''' 
    Attention!1 'Schetovod' working in progress:
    make choice, to execut a command.

    1. Добавить платеж
    2. Отредактировать платеж
    3. Вывести все платежи
    4. Вывести все платежи за указанный период
    5. Вывести топ самых крупных платежей
    m. Показать меню
    q. Закрыть программу
    '''))

    
def action_exit():
    """Выйти"""
    sys.exit(0)


    

actions = {
    '1': add_payment,
    '2': edit_payment,
    '3': print_all_payments,
    '4': print_payments,
    '5': print_top_payments,
    'm': show_menu,
    'q': action_exit,
}


def main():
    with make_connection() as conn:
        storage.initialize(conn, 'schema.sql')

    show_menu()

    while 1:
        cmd = input('\nВведите команду: ').strip()
        action = actions.get(cmd)

        if action:
            action()
        else:
            print('Вы ввели неверную команду')
