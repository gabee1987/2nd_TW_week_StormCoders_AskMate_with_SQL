'''
    Frequently used functions for the AskMate project.
    by StormCoders
'''

import psycopg2
from local_config import *


def database_manager(query, select_type_query):
    connect_str = "dbname={0} user={1} password={2} host={3}".format(DATABASE, USER, PASSWORD, HOST)
    conn = psycopg2.connect(connect_str)
    # set autocommit option, to do every query when we call it
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute(query)
    if select_type_query is True:
        records = cursor.fetchall()
        conn.close()
        return records
    conn.close()
