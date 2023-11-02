# Developed by Eddie Gu for Veloxity, 2023
# Unauthorized distribution or use is strictly prohibited
# All Rights Reserved
# @kyrofx on GitHub and Discord

import pymysql

def dbc():
# Database connection for user login
    try:
        connection = pymysql.connect(
            host="localhost",
            port=55001,
            user="root",
            password="84271",
            database="test",
            autocommit=True
        )
        return connection
    except pymysql.MySQLError as error:
        print(f"Error connecting to database (test): {error}")
        return None

def database():
# Database connection for user data / storage
    try:
        connection = pymysql.connect(
            host="localhost",
            port=55001,
            user="root",
            password="84271",
            database="data",
            autocommit=True
        )
        return connection
    except pymysql.MySQLError as error:
        print(f"Error connecting to database (data): {error}")
        return None