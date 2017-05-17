'''
AskMate Q&A website
by StormCoders
'''
from flask import Flask, request, redirect, render_template, flash
from common import *
import psycopg2

app = Flask(__name__)
app.secret_key = 'Stormcoders AskMate website is awesome'


@app.route('/', methods=['GET'])
def index():
    '''
        Displays the question as a table.
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
    conn = db_connection()
    view_question_attributes = db_execute(query, conn)
    return render_template('home.html', table_headers=table_headers, view_questions=view_question_attributes)


@app.route('/question/new', methods=['GET'])
def new_question():
    '''
        Displays the question form page.
    '''
    return render_template('question_form.html')


@app.route('/new_question', methods=['POST'])
def add_new_question():
    '''
        Adds a question to the database given by user.
        Appends question elements as rows to the appropiate file.
    '''
    pass


@app.route('/question/<q_id>', methods=['GET', 'POST'])
def display_question(q_id):
    '''
        Displays the question from the database, selected by q_id.
    '''
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
                WHERE id={0};""".format(q_id))
    conn = db_connection
    db_execute(query, conn)
    records = db_execute()
    return render_template('question.html', q_id=q_id, records=records, table_headers=table_headers)


@app.route('/question/<q_id>/delete', methods=['POST'])
def delete_question(q_id=None):
    '''
        Deletes the appropiate question.
        Removes a row from the file.
    '''
    pass


@app.route('/question/<q_id>/vote-up', methods=['POST'])
def vote_up_question(q_id=None):
    '''
        Takes a vote up in the appropiate question.
        Adds 1 to the number in file.
    '''
    pass


@app.route('/question/<q_id>/vote-down', methods=['POST'])
def vote_down_question(q_id=None):
    '''
        Takes a vote down in the appropiate question.
        Substracs 1 from the number in file.
    '''
    pass


@app.route('/question/<q_id>/new-answer', methods=['POST'])
def display_answer(q_id=None):
    '''
        Displays the answer form page.
    '''
    pass


@app.route('/question/new-answer', methods=['POST'])
def add_new_answer():
    """
    Add the new answer to database.
    """
    pass


@app.errorhandler(404)
def page_not_found(error):
    return 'Oops, page not found!', 404


if __name__ == '__main__':
    app.run(debug=True)
