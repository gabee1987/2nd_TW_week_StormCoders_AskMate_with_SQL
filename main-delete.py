@app.route('/question/<q_id>/delete', methods=['POST'])
def delete_question(q_id=None):
    '''
        Deletes the appropriate question.
        Removes a row from the table.
    '''
    db_execute("DELETE FROM question WHERE id = q_id;")
    return redirect('/')


@app.route('/answer/<a_id>/delete', methods=['POST'])
def delete_answer(a_id=None):
    '''
        Deletes the appropriate answer.
        Removes a row from the table.
    '''
    db_execute("DELETE FROM answer WHERE id = a_id;")
    return redirect('/')
