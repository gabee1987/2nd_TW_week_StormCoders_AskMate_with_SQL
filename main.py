'''
AskMate Q&A website
by StormCoders
'''
from flask import Flask, request, redirect, render_template, flash
from common import *

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
    data = open_question_file()
    max_id = 0
    if len(data) > 0:
        max_id = max(int(i[0]) for i in data)
    current_time = str(int(time.time()))
    decoded_time = str(datetime.datetime.fromtimestamp(float(current_time)).strftime('%Y-%m-%d %H:%M:%S'))
    data.append([
                str(max_id+1),
                decoded_time,
                '0',
                '0',
                request.form['question_title'],
                request.form['question_message'],
                ])
    write_question_to_file(data)
    return redirect('/')


@app.route('/question/<q_id>', methods=['GET', 'POST'])
def display_question(q_id=None):
    '''
        Displays the question from the list, selected by q_id.
    '''
    list_of_questions = open_question_file()
    q_id = request.form['view_button']
    current_question = []
    for row in list_of_questions:
        if row[0] == q_id:
            row[2] = str(int(row[2])+1)
            current_question.append(row[0])
            current_question.append(row[4])
            current_question.append(row[5])
            write_question_to_file(list_of_questions)
    answer_list = open_answer_file()
    current_answers = []
    for row in answer_list:
        if row[3] == q_id:
            current_answers.append(row)
    return render_template('question.html', q_id=q_id, current_question=current_question, current_answers=current_answers)


@app.route('/question/<q_id>/delete', methods=['POST'])
def delete_question(q_id=None):
    '''
        Deletes the appropiate question.
        Removes a row from the file.
    '''
    data = open_question_file()
    q_id = request.form['delete_button']
    for row in data:
        if row[0] == q_id:
            data.remove(row)
    write_question_to_file(data)
    return redirect('/')


@app.route('/question/<q_id>/vote-up', methods=['POST'])
def vote_up_question(q_id=None):
    '''
        Takes a vote up in the appropiate question.
        Adds 1 to the number in file.
    '''
    data = open_question_file()
    q_id = request.form['vote_up_button']
    for row in data:
        if row[0] == q_id:
            row[3] = str(int(row[3])+1)
    write_question_to_file(data)
    flash('+1')
    return redirect('/')


@app.route('/question/<q_id>/vote-down', methods=['POST'])
def vote_down_question(q_id=None):
    '''
        Takes a vote down in the appropiate question.
        Substracs 1 from the number in file.
    '''
    data = open_question_file()
    q_id = request.form['vote_down_button']
    for row in data:
        if row[0] == q_id:
            row[3] = str(int(row[3])-1)
    write_question_to_file(data)
    flash('-1')
    return redirect('/')


@app.route('/question/<q_id>/new-answer', methods=['POST'])
def display_answer(q_id=None):
    '''
        Displays the answer form page.
    '''
    question_id = q_id
    return render_template('answer_form.html', question_id=question_id)


@app.route('/question/new-answer', methods=['POST'])
def add_new_answer():
    """
    Add the new answer to database.
    """
    data = open_answer_file()
    max_id = 0
    if len(data) > 0:
        max_id = max(int(i[0]) for i in data)
    current_time = str(int(time.time()))
    decoded_time = str(datetime.datetime.fromtimestamp(float(current_time)).strftime('%Y-%m-%d %H:%M:%S'))
    data.append([
                str(max_id+1),
                decoded_time,
                '0',
                request.form['question_id'],
                request.form['answer_message']
                ])
    write_answer_to_file(data)
    return redirect("/")


@app.errorhandler(404)
def page_not_found(error):
    return 'Oops, page not found!', 404


if __name__ == '__main__':
    app.run(debug=True)
