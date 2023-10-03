#
#   Developed by Eddie Gu for Veloxity
#   All rights reserved
#   Unauthorized distribution or use is strictly prohibited
#   @kyrofx on GitHub




import pymysql

def dbc():
    try:
        connection = pymysql.connect(
            host="localhost",
            port=32769,
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
    try:
        connection = pymysql.connect(
            host="localhost",
            port=32769,
            user="root",
            password="84271",
            database="data",
            autocommit=True
        )
        return connection
    except pymysql.MySQLError as error:
        print(f"Error connecting to database (data): {error}")
        return None