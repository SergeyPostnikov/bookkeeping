from datetime import datetime
from prettytable import PrettyTable




__all__ = (
    'prompt',
    'input_date',
    'input_datetime',
    'print_table',
    'print_task',
)


def prompt(msg, default=None, type_cast=None):
    """ type_cast -> callback """
    while 1:
        value = input(f'{msg}: ')

        if not value:
            return default

        if type_cast is None:
            return value

        try:
            # int('123')
            return type_cast(value)
        except ValueError as err:
            print(err)


def input_int(msg='Введи число', default=None):
    return prompt(msg, default, type_cast=int)


def input_float(msg='Введите число', default=None):
    return prompt(msg, default, type_cast=float)


def input_datetime(msg='Введите дату', default=None,
                   ftm='%Y-%m-%d %H:%M:%S'):
    return prompt(
        msg,
        default,
        lambda v: datetime.strptime(v, ftm)
    )
    # def to_datetime(v):
    #     return datetime.strptime(v, ftm)
    # return prompt(msg, default, type_cast=to_datetime)


def input_date(msg='Введите дату', default=None, ftm='%Y-%m-%d'):
    """Запрашивает дату от пользователя через STDIN в указанном формате и возвращает ее."""
    value = input_datetime(msg, default, ftm)

    # @fixme: скорее всего упадем если date
    if value is None:
        return default

    return value.date() if isinstance(value, datetime) else value


# def yesterday_date():
#     yesterday = datetime.now - timdelta(days=1)
#     return yesterday.date()

def print_table(headers, iterable):
    """
    Распечатывает таблицу на экран.

    Arguments:
        headers (tuple|list): заголовки колонок таблицы.
        iterable (iterable): строки (данные) таблицы.
    """
    table = PrettyTable(headers)

    for row in iterable:
        table.add_row(row)

    print(table)



if __name__ == '__main__':
    # number = input_int(default=666)
    # print(number, type(number))

    # number = prompt('Введи цену', 0, float)
    # print(number, type(number))


    print(yesterday_date())








