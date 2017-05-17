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
