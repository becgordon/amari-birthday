"""Models for Amari's Birthday Site."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# GUEST CLASS ----------------------------------------------------------------


class Guest(db.Model):
    """A guest."""
    
    __tablename__ = 'guests'

    guest_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    num_rsvp = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        """Show info about guest."""

        return f'<Guest guest_id={self.guest_id} name={self.fname} {self.lname}>'


# ----------------------------------------------------------------------------


def connect_to_db(app, db_uri="postgresql:///guests"):
    """Connect to database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)

    print("Connected to db.")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)