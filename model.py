"""Models and database functions for Ratings project."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the SQLite database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Model(db.Model):

    __tablename__ = "Models"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    brand_name = db.Column(db.String(50), nullable=True)
    name = db.Column(db.String(50), nullable=False)


    def __repr__(self):
        # """Provides helpful representation when printed."""

        return "<models: id={} year={} brand_name={} name={}>".format(self.id, self.year, self.brand_name, self.name)



class Brand(db.Model):

    __tablename__ = "Brands"
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(50), db.ForeignKey('Models.brand_name'), nullable=False)
    founded = db.Column(db.Integer, nullable=True)
    headquarters = db.Column(db.String(50), nullable=True)
    discontinued = db.Column(db.Integer, nullable=True)

    # employees = db.relationship('Employee')
    # OR
    # dept = db.relationship( 'Department', backref='employees')

    model = db.relationship('Model', backref=db.backref('Brands'))

    def __repr__(self):
        # """Provides helpful representation when printed."""

        return "<brands: id={} name={} founded={} headquarters={} discontinued={}>".format(self.id, self.name, self.founded, self.headquarters, self.discontinued)

# End Part 1
##############################################################################
# Helper functions


def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auto.db'
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
