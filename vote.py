

@app.route('/question/<q_id>/vote-up')
def vote_up_question(q_id=None):
    query = ("""UPDATE question SET vote_number + 1 WHERE id = {0};""".format(q_id))
    select_type_query = False
    database_manager(query, select_type_query)
    return redirect("/")


@app.route('/question/<q_id>/vote-down')
def vote_down_question(q_id=None):
    query = ("""UPDATE question SET vote_number - 1 WHERE id = {0};""".format(q_id))
    select_type_query = False
    database_manager(query, select_type_query)
    return redirect("/")
