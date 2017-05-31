'''
AskMate Q&A website
by StormCoders
'''
from flask import Flask, request, redirect, render_template, flash
from db_manager import *
import psycopg2
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'Stormcoders AskMate website is awesome'


@app.route('/')
@app.route('/index')
def index():
    '''
        Displays the questions as a table.
    '''
    table_headers = [
                    '#ID',
                    'Submission time',
                    'View number',
                    'Vote number',
                    'Title',
                    'Message',
                    'Image',
                    'View',
                    'Delete',
                    'Vote Up',
                    'Vote Down'
                    ]
    query = ("""SELECT * FROM question;""")
    view_questions = query_execute(query, return_data='all_data')
    return render_template('index.html', table_headers=table_headers, view_questions=view_questions)


@app.route('/question/new')
def new_question():
    '''
        Displays the question form page.
    '''
    return render_template('question_form.html')


@app.route('/new_question', methods=['POST'])
def add_new_question():
    '''
        Adds new question to the database.
    '''
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    question_title = request.form['q_title']
    question_message = request.form['q_message']
    query = """INSERT INTO question (submission_time, view_number, vote_number, title, message, image, user_id) \
                VALUES(%s, %s, %s, %s, %s, %s, %s);"""
    data_to_modify = (dt, 0, 0, question_title, question_message, 0, 1)
    query_execute(query, data_to_modify, 'no_data')
    return redirect("/")


@app.route('/question/<q_id>', methods=['GET', 'POST'])
def display_question(q_id=None):
    '''
        Displays the question from the database, selected by q_id.
    '''
    q_table_headers = [
                    'Submission Time',
                    'View number',
                    'Vote number',
                    'Title',
                    'Message',
                    'Image'
                    ]
    a_table_headers = [
                    'ID',
                    'Submission Time',
                    'Vote number',
                    'Question Id',
                    'Message',
                    'Image',
                    'Delete'
                    ]
    data_to_modify = [q_id]
    query = """UPDATE question SET view_number = view_number + 1\
                WHERE id = %s;"""
    query_execute(query, data_to_modify, return_data == 'no_data')
    query = """SELECT submission_time, view_number, vote_number, title, message, image FROM question\
                WHERE id = %s;"""
    view_question = query_execute(query, data_to_modify, 'all_data')
    query = """SELECT id, submission_time, vote_number, question_id, message, image FROM answer\
                WHERE question_id = %s;"""
    view_answers = query_execute(query, data_to_modify, 'all_data')
    return render_template(
                        'question.html',
                        q_id=q_id,
                        view_question=view_question,
                        q_table_headers=q_table_headers,
                        a_table_headers=a_table_headers,
                        view_answers=view_answers
                        )


@app.route('/question/<q_id>/delete')
def delete_question(q_id=None):
    '''
        Deletes the appropriate question.
        Removes a row from the table.
    '''
    query = """DELETE FROM answer WHERE question_id = %s;"""
    data_to_modify = [q_id]
    query_execute(query, data_to_modify, 'no_data')

    query = """DELETE FROM question WHERE id = %s;"""
    data_to_modify = [q_id]
    query_execute(query, data_to_modify, 'no_data')
    return redirect('/')


@app.route('/answer/<q_id>/<a_id>/delete')
def delete_answer(q_id=None, a_id=None):    # This function isn't working right now!!!
    '''
        Deletes the appropriate answer.
        Removes a row from the table.
    '''
    query = """DELETE FROM answer WHERE id = %s;"""
    data_to_modify = [a_id]
    query_execute(query, data_to_modify, 'no_data')
    return redirect('/question/' + q_id)


@app.route('/question/<q_id>/vote-up')
def vote_up_question(q_id=None):
    '''
        Takes a vote up in the appropiate question.
        Adds 1 to the number in file.
    '''
    query = """UPDATE question SET vote_number = vote_number + 1 WHERE id = %s;"""
    data_to_modify = [q_id]
    query_execute(query, data_to_modify, 'no_data')
    return redirect("/")


@app.route('/question/<q_id>/vote-down')
def vote_down_question(q_id=None):
    '''
        Takes a vote down in the appropiate question.
        Substracs 1 from the number in file.
    '''
    query = """UPDATE question SET vote_number = vote_number - 1 WHERE id = %s;"""
    data_to_modify = [q_id]
    query_execute(query, data_to_modify, 'no_data')
    return redirect("/")


@app.route('/question/<q_id>/new-answer')
def display_answer(q_id=None):
    '''
        Displays the answer form page.
    '''
    query = """SELECT title, message FROM question WHERE id = %s;"""
    data_to_modify = [q_id]
    view_questions = query_execute(query, data_to_modify, 'all_data')
    return render_template('answer_form.html', q_id=q_id, view_questions=view_questions)


@app.route('/question/new-answer/<q_id>', methods=['POST'])
def add_new_answer(q_id=None):
    """
    Add the new answer to database.
    """
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    answer_message = request.form["answer_message"]
    query = """INSERT INTO answer (submission_time, vote_number, question_id, message, image)
                VALUES(%s, %s, %s, %s, %s);"""
    data_to_modify = (dt, 0, q_id, answer_message, 0)
    query_execute(query, data_to_modify, 'no_data')
    return redirect("/question/" + q_id)


@app.errorhandler(404)
def page_not_found(error):
    return 'Missing', 404


if __name__ == '__main__':
    app.run(debug=True)
