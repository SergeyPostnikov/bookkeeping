from datetime import datetime
import sqlite3
from prettytable import PrettyTable

SQL_SELECT_ALL_PAYMENT = 'SELECT id, namepay, price, timepoint, count FROM schetovod'

def make_connection():
    sqlite3.register_converter('DATE', lambda value: datetime.strptime(value.decode(), '%Y-%m-%d'))
    sqlite3.register_converter('DATETIME', lambda value: datetime.strptime(value.decode(), '%Y-%m-%d %H:%M:%S'))
    conn = sqlite3.connect('schetovod.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    return conn

def select_all_payments(conn): # а она мне вообще нужна?
    return conn.execute(SQL_SELECT_ALL_PAYMENT).fetchall()


def print_table(headers, iterable):

    table = PrettyTable(headers)

    for row in iterable:
        table.add_row(row)

    print(table)


def print_all_payments():
    """Вывести все платежи"""
    with make_connection() as conn:
        payments = select_all_payments(conn)
        print_table(
        [
            'ID', 'Название', 'Цена',
            'Время внесения', 'Количество'
        ],
        payments
    )

print_all_payments()


# a = datetime.strptime('2020/04/20 01:10:48', '%Y-%m-%d %H:%M:%S')
# print(a, type(a))