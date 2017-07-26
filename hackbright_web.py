"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    list_grade_by_student = hackbright.get_grades_by_github(github)

    return render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           list_grade_by_student=list_grade_by_student)


    

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    html = render_template("student_search.html")

    return html



@app.route("/student-add")
def get_student_add():
    """Show form for searching for a student."""

    html = render_template("student_add.html")

    return html    

@app.route("/student-add-db", methods=['POST'])
def student_add_db():
    """Add a student."""
    first = request.form.get('first_name')
    last = request.form.get('last_name')
    github = request.form.get('github')

    hackbright.make_new_student(first, last, github)

    html = render_template("student_confirmation.html",
                           first=first,
                           last=last,
                           github=github)
    return html

   

@app.route("/student-confirmation")
def student_confirmation():
    """Confirms addition of student into the database."""

   

    return render_template("student_confirmation.html")

    pass

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
