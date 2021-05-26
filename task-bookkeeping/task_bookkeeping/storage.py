SQL_ADD_PAYMENT = 'INSERT INTO schetovod (namepay, price, timepoint, count) VALUES (?, ?, ?, ?)'

SQL_UPDATE_PAYMENT = 'UPDATE schetovod SET namepay=?, price=?, timepoint=?, count=? WHERE id=?'

SQL_SELECT_ALL_PAYMENT = 'SELECT id, namepay, price, timepoint, count FROM schetovod'

SQL_SELECT_PAYMENT_BY_PK = f'{SQL_SELECT_ALL_PAYMENT} WHERE id=?'

SQL_SELECT_PAYMENT_ON_PERIOD =f'{SQL_SELECT_ALL_PAYMENT} WHERE timepoint BETWEEN ? AND ?'

SQL_SELECT_TOP_PAYMENT = f'{SQL_SELECT_ALL_PAYMENT} ORDER BY price DESC' 
# SQL_SELECT_TOP_PAYMENT = 'SELECT price FROM schetovod ORDER BY price' 

__all__ = (
    'initialize',
    'sql_add_payment',
    'update_payment',
    'select_all_payments',
    'select_payments_on_period',
    'select_payments_by_pk',
    'select_top_payments',
)

def initialize(conn, creation_schema):
    with open(creation_schema) as f:
        conn.executescript(f.read())


def sql_add_payment(conn, namepay, price, timepoint, count):
    conn.execute(SQL_ADD_PAYMENT, (namepay, price, timepoint, count))


def update_payment(conn, pk, namepay, price, timepoint, count): # вызову в init__.py в фунции edit_payments
    conn.execute(SQL_UPDATE_PAYMENT, (namepay, price, timepoint, count, pk))


def select_all_payments(conn): # а она мне вообще нужна?
    return conn.execute(SQL_SELECT_ALL_PAYMENT).fetchall()


def select_payments_on_period(conn, dt_start, dt_end):
    return conn.execute(SQL_SELECT_PAYMENT_ON_PERIOD, (dt_start, dt_end)).fetchall()


def select_payments_by_pk(conn, pk):
	return conn.execute(SQL_SELECT_PAYMENT_BY_PK, (pk,)).fetchall()


def select_top_payments(conn):
	return conn.execute(SQL_SELECT_TOP_PAYMENT).fetchall()




