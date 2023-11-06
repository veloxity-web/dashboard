#   Developed by Eddie Gu for Veloxity, 2023
#   Unauthorized distribution or use is strictly prohibited
#   All Rights Reserved
#   @kyrofx on GitHub and Discord
#
#   File History: 2023-9-26 Initial Commit (Eddie Gu)
#   File History: 2023-11-6 Last Commit (Eddie Gu)
#

import bcrypt
from dbConnect import db, User, UserData

def newLogin(email):
    # Checks if a user's password exists in the database.
    user = User.query.filter_by(email=email).first()
    if user is None:
        # username does not exist
        return None
    elif user.HSPass is None:
        # Password is not set for the user
        return True
    else:
        # username exists and password is set
        return False

def createPassword(email, password):
    # Submit a password to database
    print(f"Creating password for {email}")
    hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    user = User.query.filter_by(email=email).first()
    if user:
        user.HSPass = hashed_pw
        db.session.commit()
        print(f"Password created for {email}")
        return True
    else:
        print(f"User {email} not found.")
        return False

def confirmPassword(email, password):
    # Confirm a user's password.
    user = User.query.filter_by(email=email).first()
    if user:
        # Assuming the `password` field is the hashed password stored in the database
        if bcrypt.checkpw(password.encode('utf-8'), user.HSPass.encode('utf-8')):
            return True
        else:
            return False
    else:
        print(f"User {email} not found.")
        return False
