@app.route('/question/<q_id>/new-answer')
def display_answer(q_id=None):
    '''
        Displays the answer form page.
    '''
    query = ("""SELECT title, message FROM question WHERE id={0};""".format(q_id))
    conn = db_connection()
    view_question_attributes = db_execute(query, conn)
    return render_template('answer_form.html', question_id=q_id, view_question_attributes=view_question_attributes)


@app.route('/question/new-answer/<q_id>', methods=['POST'])
def add_new_answer():
    """
    Add the new answer to database.
    """
    dt = datetime.now()
    answer_message = request.form["answer_message"]
    query = ("""INSERT INTO answer(submisson_time, vote_number, question_id, message, image)
                 VALUES({0}, {1}, {2}, {3}, {4}, {5}) WHERE id={6};""".format(dt, 0, q_id, answer_message, 0, q_id))
    conn = db_connection()
    db_execute(query, conn)
    return redirect("/question/<q_id>")
