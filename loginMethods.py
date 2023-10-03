#
#   Developed by Eddie Gu for Veloxity
#   All rights reserved
#   Unauthorized distribution or use is strictly prohibited
#   @kyrofx on GitHub
from dbConnect import *
from flask import *






######################################################################################################################
###  F U N C T I O N S  ##############################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
########################################################################################################## :3 MAFIA ##
######################################################################################################################

def newLogin(username):
    connection = dbc()
    if connection is None:
        print("Failed to connect to database.")
        return None
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    result = cursor.fetchone()
    if result is None:
        # username does not exist
        return None
    else:
        # username exists
        cursor.execute(f"SELECT * FROM users where username = '{username}' and password is NULL")
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True


def createPassword(username, password):
    try:
        connection = dbc()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE users SET password = '{password}' WHERE username = '{username}'")
        connection.commit()
        return True
    except:
        return False


def confirmPassword(username, password):
    try:
        connection = dbc()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users WHERE username = '{username}' and password = '{password}'")
        connection.commit()
        result = cursor.fetchone()
        if result is None:
            return False
        else:
            return True
    except:
        return False
