@app.route('/question/<q_id>/delete', methods=['POST'])
def delete_question(q_id=None):
    '''
        Deletes the appropriate question.
        Removes a row from the table.
    '''
    conn = db_connection()
    db_execute("""DELETE FROM question WHERE id={0};""".format(q_id), conn)
    return redirect('/')


@app.route('/answer/<a_id>/delete', methods=['POST'])
def delete_answer(a_id=None):
    '''
        Deletes the appropriate answer.
        Removes a row from the table.
    '''
    conn = db_connection()
    db_execute("""DELETE FROM answer WHERE id={0};""".format(a_id), conn)
    return redirect('/')
