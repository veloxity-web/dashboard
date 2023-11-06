#   Developed by Eddie Gu for Veloxity, 2023
#   Unauthorized distribution or use is strictly prohibited
#   All Rights Reserved
#   @kyrofx on GitHub and Discord
#
#   File History: 2023-9-26 Initial Commit (Eddie Gu)
#   File History: 2023-11-6 Last Commit (Eddie Gu)
#

from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()


# User model
class User(db.Model):
    __bind_key__ = 'users'  # This will link the model to the users SQLite database
    email = db.Column(db.String(100), unique=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    HSPass = db.Column(db.String(100), nullable=True)
    employee = db.Column(db.Boolean, nullable=False, default=False)
    administrator = db.Column(db.Boolean, nullable=False, default=False)
    AccLock = db.Column(db.Boolean, nullable=False, default=False)


# UserData model
class UserData(db.Model):
    __bind_key__ = 'data'  # This will link the model to the data SQLite database
    id = db.Column(db.Integer, nullable = False, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    income = db.Column(db.Float, nullable=False)
    expense = db.Column(db.Float, nullable=False)
    profit = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Float, nullable=False)


# Initialize app with Flask-SQLAlchemy
def init_app(app):
    db.init_app(app)
    with app.app_context():
        # This will create all tables for the binds specified in the SQLALCHEMY_BINDS config variable
        db.create_all()
