#   Developed by Eddie Gu for Veloxity, 2023
#   Unauthorized distribution or use is strictly prohibited
#   All Rights Reserved
#   @kyrofx on GitHub and Discord
#
#   File History: 2023-9-26 Initial Commit (Eddie Gu)
#   File History: 2023-11-6 Last Commit (Eddie Gu)
#

import datetime
from sqlalchemy import Table, Column, Integer, Float, DateTime, MetaData, select, Boolean, create_engine
from dbConnect import db

metadata = MetaData()

def get_user_table(id):
    # Dynamically define a table for the user's data.
    return Table(
        id, metadata,
        Column('id', Integer, primary_key=True),
        Column('timestamp', DateTime, default=datetime.datetime.utcnow),
        Column('income', Float),
        Column('expense', Float),
        Column('profit', Float),
        Column('tax', Float),
        extend_existing=True
    )

def submitdata(email, income, expense, profit, tax):
    print("API called")
    try:
        user_table = get_user_table(email)
        # Ensure the table is created
        metadata.create_all(db.engine, tables=[user_table])
        ins = user_table.insert().values(income=income, expense=expense, profit=profit, tax=tax)
        db.engine.execute(ins)
        print("Submit success")
        return True
    except Exception as e:
        print(f"Error updating data for {email}: {e}")
        return False

def findtable(email):
    try:
        user_table = get_user_table(email)
        sel = select([user_table])
        conn = db.engine.connect()
        result = conn.execute(sel)
        data_exists = result.fetchone() is not None
        conn.close()
        return data_exists
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def createtable(email):
    try:
        user_table = get_user_table(email)
        # This will create the table if it doesn't exist
        metadata.create_all(db.engine, tables=[user_table])
        print(f"Table for {email} created successfully.")
        return True
    except Exception as e:
        print(f"Error creating table for {email}: {e}")
        return False

def fetchdata(email):
    try:
        user_table = get_user_table(email)
        sel = select([user_table])
        conn = db.engine.connect()
        result = conn.execute(sel)
        data = result.fetchall()
        conn.close()
        return data
    except Exception as e:
        print(f"Error fetching data for {email}: {e}")
        return []

from sqlalchemy import MetaData, Table, create_engine

def makeaccount(email, name, employee, administrator):
    print("API called to create account")
    try:
        # Get the engine for the 'users' database
        engine = db.get_engine(bind='users')

        # Reflect the existing 'user' table structure from the 'users' database
        metadata = MetaData()
        user_table = Table('user', metadata, autoload_with=engine)

        # Convert employee and administrator to boolean
        employee_bool = employee.lower() == 'true'
        administrator_bool = administrator.lower() == 'true'

        # Set the AccLock value for new accounts
        acc_lock_value = False

        # Insert the new account data into the table
        with engine.connect() as connection:
            ins = user_table.insert().values(email=email, name=name,
                                             employee=employee_bool, administrator=administrator_bool,
                                             AccLock=acc_lock_value)
            connection.execute(ins)
            connection.commit()

        print(f"Account creation successful for {email}")
        return True
    except Exception as e:
        print(f"Error creating account for {email}: {e}")
        return False