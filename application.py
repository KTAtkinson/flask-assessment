from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"


@app.route("/application-form")
def application_form_page():
    """Renders application page."""
    return render_template('application-form.html')


@app.route('/application', methods=['post'])
def application_submit_page():
    """Renders thank you page after user has filled out application."""
    # strip to get rid of an extra leading space of the user doesn't provide
    # their first name and trailing spaces if the user doesn't provide a
    # las name.
    users_name = '{} {}'.format(request.form.get('first-name', ''),
                                request.form.get('last-name', '')).strip()
    position = request.form.get('job-title')
    required_salary = request.form.get('required-salery')

    return render_template('application-response.html',
                           applicant_name=users_name,
                           applicant_position=position,
                           salary_requirement=required_salary)


if __name__ == "__main__":
    app.run(debug=True)
