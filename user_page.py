@app.route("/user/<user_id>")
def display_user_page(user_id=None):
    select_from_question = ("""SELECT question.title
                                FROM question
                                INNER JOIN users
                                    ON question.user_id = users.id;""")
    select_from_answer = ("""SELECT answer.message
                                FROM answer
                                INNER JOIN users
                                    ON answer.user_id = users.id;""")
    return render_template(
                            'user_page.html',
                            select_from_answer=select_from_answer,
                            select_from_question=select_from_question
                            )