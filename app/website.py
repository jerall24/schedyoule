# from app.main import example

import os
from functools import wraps

from flask import Flask, request, session, g, redirect, url_for, \
                  abort, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

# Reading an excel file using Python
import xlrd

# Give the location of the file
loc = ("app/position_descriptions.xlsx")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

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

import app.models as models


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
    if session.get("logged_in"):
        return redirect(url_for('home'))

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
    return redirect(url_for("home"))


@heroku_app.route("/search", methods=["GET"])
def search():
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    query = request.args.get("query")
    entries = db.session.query(models.Role)
    if query:
        return render_template("search.html", entries=entries, query=query)
    return render_template("search.html", entries=entries)


@heroku_app.route("/cards", methods=["GET"])
def cards():
    if not session.get("logged_in"):
        return redirect(url_for('login'))
    entries = db.session.query(models.Role)
    return render_template("cards.html", entries=entries)


@heroku_app.route("/add", methods=["POST"])
def add_entry():
    """Adds new post to the database."""
    if not session.get("logged_in"):
        abort(401)

    # POSSIBLE ISSUES
    # 1. numeric values (assignment_id, career_level_from, career_level_to, candidates)
    # 2. date formats yyyy-mm-dd (created_date, requested_start_date, end_date)
    # 3. boolean formats (sold (Yes/No), gcp_preference (Y/N), client_contract_based (Yes/No))

    new_entry = models.Role(int(request.form["assignment_id"]), request.form["demand_type"], \
                request.form["career_track"], request.form["location_radius"], request.form["source_location"], \
                request.form["gu"], request.form["assignment_fulfillment_entity"], request.form["client"], \
                request.form["project"], request.form["project_metro_city"], request.form["project_supervising_entity"], \
                request.form["project_client_supply_demand_specialist"], request.form["sold"] == "Yes", \
                request.form["gcp_preference"] == "Y", request.form["client_contract_based"] == "Yes", \
                request.form["assignment_title"], request.form["description"], request.form["fulfillment_channel"], \
                request.form["created_date"], request.form["source"], request.form["requested_start_date"], \
                request.form["end_date"], request.form["status"], int(request.form["career_level_from"]), \
                int(request.form["career_level_to"]), request.form["talent_segment"], request.form["assigned_role"], \
                request.form["work_location"], \
                request.form["assignment_primary_specialization_level_one"], \
                request.form["assignment_primary_specialization_level_two"], \
                request.form["assignment_primary_specialization_level_three"], \
                request.form["assignment_primary_specialization_level_four"], \
                request.form["assignment_primary_specialization_level_five"], \
                request.form["assignment_primary_specialization_paths"], \
                request.form["skill_and_proficiency"], request.form["primary_contact"], \
                request.form["assignment_audit"], request.form["role_client_supply_demand_specialist"], \
                int(request.form["candidates"]))
    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for("search"))


if __name__ == '__main__':
    heroku_app.run(debug=True)
