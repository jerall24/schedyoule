# from app.main import example

import os
from functools import wraps

from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy


# get the folder where this file runs
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
SECRET_KEY = 'my_precious'
USERNAME = 'admin'
PASSWORD = 'admin'

# database config
SQLALCHEMY_DATABASE_URI = os.getenv(
    'DATABASE_URL',
    f'sqlite:///{os.path.join(basedir, "flaskr.db")}'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# create app
heroku_app = Flask(__name__)
heroku_app.config.from_object(__name__)
db = SQLAlchemy(heroku_app)

import app.models


@heroku_app.route('/')
def home():
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    return render_template("form.html")

@heroku_app.route('/example/')
def exmpl():
    return render_template("form.html", example=example())

@heroku_app.route('/login', methods=['GET', 'POST'])
def login():
    """User login/authentication/session management."""
    error = None
    if request.method == 'POST':
        if request.form['username'] != heroku_app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != heroku_app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@heroku_app.route("/logout")
def logout():
    """User logout/authentication/session management."""
    session.pop("logged_in", None)
    flash("You were logged out")
    return redirect(url_for("home"))


@heroku_app.route("/search/", methods=["GET"])
def search():
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    query = request.args.get("query")
    entries = db.session.query(models.Role)
    if query:
        return render_template("search.html", entries=entries, query=query)
    return render_template("search.html")

if __name__ == '__main__':
    heroku_app.run(debug=True)
