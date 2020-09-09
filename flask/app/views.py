from app import app
from app.forms import LoginForms
from markupsafe import escape

from flask import url_for, render_template, redirect


@app.route('/')
def hello():
    return render_template("basic.html")


@app.route('/test/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/login', methods=['POST', 'GET'])
def forms_time():
    form = LoginForms()
    if form.validate_on_submit():
        return redirect(url_for('show_user_profile', username=form.username))
    return render_template("login.html", form=form)