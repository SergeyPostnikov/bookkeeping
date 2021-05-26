from configparser import ConfigParser
import sqlite3

from datetime import datetime


def make_config(*config_files):
	config = ConfigParser()
	config.read(config_files)
	return config


config = make_config('config.ini')


def make_connection(name='db'):

	sqlite3.register_converter('DATE', lambda value: datetime.strptime(value.decode(), '%Y-%m-%d'))
	sqlite3.register_converter('DATETIME', lambda value: datetime.strptime(value.decode(), '%Y-%m-%d %H:%M:%S'))
	
	conn = sqlite3.connect(
		config.get(name, 'db_name'),
		detect_types=sqlite3.PARSE_DECLTYPES
	)
	conn.row_factory = sqlite3.Row
	return conn







