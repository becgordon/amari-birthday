"""Server for Amari's  Birthday Site."""

from flask import Flask, render_template, request, flash, session, redirect
import os
from model import connect_to_db, db, Guest

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"


# ROUTES ---------------------------------------------------------------------


@app.route('/')
def welcome_page():
    """View welcome page."""
    
    return render_template('homepage.html')


@app.route('/rsvp', methods=['POST'])
def rsvp():
    """RSVP to party."""
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    num_rsvp = request.form.get('num-guests')

    guest = Guest(fname=first_name, lname=last_name, num_rsvp=num_rsvp)

    db.session.add(guest)
    db.session.commit()

    session['RSVP'] = True

    return render_template('homepage.html')

# ----------------------------------------------------------------------------


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)