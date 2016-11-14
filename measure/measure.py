# -*- coding: utf-8 -*-

import os.path
import pandas.io.sql as psql
import sqlite3


DB_PATH = os.path.expanduser('~/Documents/measurements.db')


def record(number):
    with sqlite3.connect(DB_PATH) as db:
        try:
            insert(db, number)
        except sqlite3.OperationalError:
            create_table(db)
            insert(db, number)


def insert(db, number):
    db.execute(
        'INSERT INTO measurements (value) VALUES (?)',
        (number,)
    )


def create_table(db):
    # Don't "drop if exists" unless you like losing all data for any bug
    db.execute(
        'CREATE TABLE measurements ('
        '   id INTEGER PRIMARY KEY, '
        '   taken_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL, '
        '   value FLOAT NOT NULL'
        ')'
    )


def get_data():
    with sqlite3.connect(DB_PATH) as db:
        data = psql.read_sql_query(
            """SELECT
                    datetime(taken_at, 'localtime') AS taken_at,
                    value
                FROM measurements
                ORDER BY 1
            """,
            index_col='taken_at',
            con=db,
            parse_dates=['taken_at']
        )
    return data.value
