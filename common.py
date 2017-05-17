'''
    Frequently used functions for the AskMate project.
    by StormCoders
'''

import psycopg2
from local_config import *


def db_connection():
    conn = psycopg2.connect(
                            database=DATABASE,
                            user=USER,
                            password=PASSWORD,
                            host=HOST,
                            port=PORT
                            )






