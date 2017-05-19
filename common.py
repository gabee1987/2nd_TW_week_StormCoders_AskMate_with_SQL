'''
    Frequently used functions for the AskMate project.
    by StormCoders
'''

import psycopg2
from local_config import *


def database_manager(query, select_type_query, values=None):
    """ Set the connection with the database,
    and execute the orders in it. After the
    process, it closes the connection. """

    connect_str = "dbname={0} user={1} password={2} host={3}".format(DATABASE, USER, PASSWORD, HOST)
    conn = psycopg2.connect(connect_str)
    conn.autocommit = True
    cursor = conn.cursor()
    if values is not None:     # The function decides if the query has some variable in it.
        if select_type_query is True:    # The function decides if the type of the query is SELECT or not.
            cursor.execute(query, values)
            records = cursor.fetchall()
            conn.close()
            return records
        cursor.execute(query, values)
    if values is None:
        if select_type_query is True:
            cursor.execute(query)
            records = cursor.fetchall()
            conn.close()
            return records
        cursor.execute(query)
    conn.close()
