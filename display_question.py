from common import *


def display_question(q_id):
    table_headers = [
                    'Submission Time',
                    'View number',
                    'Vote number',
                    'Title',
                    'Message',
                    'Image'
                    ]
    db_connection()
    query = ("""SELECT submission_time, view_number, vote_number, title, message, image FROM question\
                WHERE id='q_id';""")
    db_execute(query, conn)
    records = db_execute()
    return render_template('question.html', q_id=q_id, records=records, table_headers=table_headers)

