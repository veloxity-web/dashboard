#
#   Developed by Eddie Gu for Veloxity
#   All rights reserved
#   Unauthorized distribution or use is strictly prohibited
#   @kyrofx on GitHub

from dbConnect import *


# needs fix for new datastructure


def apisubmitdata(expense, revenue, id):
    intData = int(data)
    try:
        connection = dbc()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE data SET data = {intData} WHERE username = {id}")
        connection.commit()
        return True
    except:
        print("Error updating data for " + id)
        return False


def findtable(id):
    try:
        connection = database()
        cursor = connection.cursor()

        # Check if the table exists
        cursor.execute("SELECT count(*) FROM information_schema.tables WHERE table_name = %s", (id,))
        if cursor.fetchone()[0] == 1:
            cursor.execute(f"SELECT * FROM {id}")
            result = cursor.fetchone()
            return result is not None
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        if connection:
            connection.close()


def createtable(id):
    try:
        connection = database()
        cursor = connection.cursor()
        #create table with timestamp, expense, revenue
        cursor.execute(f"CREATE TABLE {id} (timestamp DATETIME, expense decimal(10,2), revenue decimal(10,2))")
        cursor.execute(f"INSERT INTO {id} (timestamp, expense, revenue) VALUES (NOW(), 0, 0)")
        return True
    except:
        print("Error creating table for " + id)
        return False

def submitdata(expense, revenue, id):
    try:
        connection = database()
        cursor = connection.cursor()
        #insert data into table
        cursor.execute(f"INSERT INTO {id} (timestamp, expense, revenue) VALUES (NOW(), {expense}, {revenue})")
        return True
    except:
        print("Error submitting data for " + id)
        return False


def fetchdata(id):
    try:
        connection = database()
        cursor = connection.cursor()
        cursor.execute("SELECT count(*) FROM information_schema.tables WHERE table_name = %s", (id,))
        if cursor.fetchone()[0] == 1:
            cursor.execute(f"SELECT * FROM {id}")
            data = cursor.fetchall()
            return data
        else:
            print(f"No table found for {id}")
            return []
    except Exception as e:
        print(f"Error fetching data for {id}: {e}")
        return []

