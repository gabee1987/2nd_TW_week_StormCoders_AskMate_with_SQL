from common import *
import psycopg2

select_type_query = True
query = """SELECT id, submission_time, vote_number, question_id, message, image FROM answer\
                WHERE question_id = %s;"""
values = '0'
view_answers = database_manager(query, select_type_query, values)
print(view_answers)
