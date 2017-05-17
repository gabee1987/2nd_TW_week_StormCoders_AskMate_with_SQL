'''
    Frequently used functions for the AskMate project.
    by StormCoders
'''


from constants import (QUESTIONS_FILE, ANSWERS_FILE)
import psycopg2


def db_connection():
    conn = psycopg2.connect(
                            database='testdb',
                            user='postgres',
                            password='pass123',
                            host='127.0.0.1',
                            port='5432'
                            )






