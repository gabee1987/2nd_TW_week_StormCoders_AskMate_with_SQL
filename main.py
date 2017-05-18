'''
AskMate Q&A website
by StormCoders
'''
from flask import Flask, request, redirect, render_template, flash
from common import *
import psycopg2

app = Flask(__name__)
app.secret_key = 'Stormcoders AskMate website is awesome'


@app.route('/')
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
    select_type_query = True
    query = ("""SELECT * FROM question;""")
    view_questions = database_manager(query, select_type_query)
    return render_template('home.html', table_headers=table_headers, view_questions=view_questions)


@app.route('/question/new')
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
def display_question(q_id=None):
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
    query = ("""SELECT submission_time, view_number, vote_number, title, message, image FROM question\
                WHERE id={0};""".format(q_id))
    select_type_query = True
    view_question = database_manager(query, select_type_query)
    query = ("""SELECT submission_time, vote_number, question_id, message, image FROM answer\
                WHERE question_id={0};""".format(q_id))
    view_answers = database_manager(query, select_type_query)
    return render_template(
                        'question.html',
                        q_id=q_id,
                        view_question=view_question,
                        table_headers=table_headers,
                        view_answers=view_answers
                        )


@app.route('/question/<q_id>/delete', methods=['POST'])
def delete_question(q_id=None):
    '''
        Deletes the appropriate question.
        Removes a row from the table.
    '''
    select_type_query = False
    query = ("""DELETE FROM question WHERE id={0};""".format(q_id))
    database_manager(query, select_type_query)
    return redirect('/')


@app.route('/answer/<a_id>/delete', methods=['POST'])
def delete_answer(a_id=None):
    '''
        Deletes the appropriate answer.
        Removes a row from the table.
    '''
    select_type_query = False
    query = ("""DELETE FROM answer WHERE question_id={0};""".format(a_id))
    database_manager(query, select_type_query)
    return redirect('/')


@app.route('/question/<q_id>/vote-up')
def vote_up_question(q_id=None):
    '''
        Takes a vote up in the appropiate question.
        Adds 1 to the number in file.
    '''
    query = ("""UPDATE question SET vote_number = vote_number + 1 WHERE id = {0};""".format(q_id))
    select_type_query = False
    database_manager(query, select_type_query)
    return redirect("/")


@app.route('/question/<q_id>/vote-down')
def vote_down_question(q_id=None):
    '''
        Takes a vote down in the appropiate question.
        Substracs 1 from the number in file.
    '''
    query = ("""UPDATE question SET vote_number = vote_number - 1 WHERE id = {0};""".format(q_id))
    select_type_query = False
    database_manager(query, select_type_query)
    return redirect("/")


@app.route('/question/<q_id>/new-answer')
def display_answer(q_id=None):
    '''
        Displays the answer form page.
    '''
    query = ("""SELECT title, message FROM question WHERE id={0};""".format(q_id))
    select_type_query = True
    view_questions = database_manager(query, select_type_query)
    return render_template('answer_form.html', question_id=q_id, view_questions=view_questions)


@app.route('/question/new-answer/<q_id>', methods=['POST'])
def add_new_answer(q_id=None):
    """
    Add the new answer to database.
    """
    dt = datetime.now()
    answer_message = request.form["answer_message"]
    query = ("""INSERT INTO answer(submisson_time, vote_number, question_id, message, image)
                 VALUES({0}, {1}, {2}, {3}, {4}, {5}) WHERE id={6};""".format(dt, 0, q_id, answer_message, 0, q_id))
    select_type_query = False
    database_manager(query, select_type_query)
    return redirect("/question/<q_id>")


@app.errorhandler(404)
def page_not_found(error):
    return 'Oops, page not found!', 404


if __name__ == '__main__':
    app.run(debug=True)
