'''
    Frequently used functions for the AskMate project.
    by StormCoders
'''

import psycopg2
from local_config import *


def db_connection():
    connect_str = "dbname={0} user={1} password={2} host={3}".format(DATABASE, USER, PASSWORD, HOST)
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    return conn

conn = db_connection()


def db_execute(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    return records


