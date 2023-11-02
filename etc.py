# Developed by Eddie Gu for Veloxity, 2023
# Unauthorized distribution or use is strictly prohibited
# All Rights Reserved
# @kyrofx on GitHub and Discord

from dbConnect import dbc, database

def apisubmitdata(expense, revenue, id):
    # API for submitting data. This needs to be updated in accordance with the new database structure and plans.
    print ("etc api called")
    try:
        expense = float(expense)
        revenue = float(revenue)
    except ValueError:
        print("Invalid input: expense and revenue must be convertible to float.")
        return False
    try:
        connection = database()
        print("connected")
        cursor = connection.cursor()
        print("cursor created")
        cursor.execute(f"INSERT INTO {id} (timestamp, expense, revenue) VALUES (NOW(), {expense}, {revenue})")
        connection.commit()
        print("submit success")
        return True
    except:
        print("Error updating data for " + id)
        return False

def findtable(id):
# Finds if a table exists for the user.
    try:
        connection = database()
        cursor = connection.cursor()
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
# Make a table for a user.
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

def fetchdata(id):
# Fetch data from the user's table.
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

