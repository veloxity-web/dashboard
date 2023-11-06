#   Developed by Eddie Gu for Veloxity, 2023
#   Unauthorized distribution or use is strictly prohibited
#   All Rights Reserved
#   @kyrofx on GitHub and Discord
#
#   File History: 2023-9-26 Initial Commit (Eddie Gu)
#   File History: 2023-11-6 Last Commit (Eddie Gu)
#

from flask import Flask, session, redirect, url_for, render_template, request
from etc import findtable, createtable, fetchdata, submitdata
from loginMethods import newLogin, confirmPassword, createPassword
from dbConnect import db, init_app, User, UserData

veloxity = Flask(__name__)
veloxity.secret_key = "VqMXxcFU00cP9oi7hKEoUjyvmNGUWjQO7dcr6QRE0hzwCTMy1p"
veloxity.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/kyro/Documents/github/webserver/database/data.db'
veloxity.config['SQLALCHEMY_BINDS'] = {
    'users': 'sqlite:////Users/kyro/Documents/github/webserver/database/users.db',
    'data': 'sqlite:////Users/kyro/Documents/github/webserver/database/data.db'
}

veloxity.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print('DB URI:', veloxity.config['SQLALCHEMY_DATABASE_URI'])
print('Bind URIs:', veloxity.config['SQLALCHEMY_BINDS'])

init_app(veloxity)


@veloxity.route("/", methods=["GET"])
def index():
    # Renders the main index page.
    if "ID" in session:
        return redirect(url_for("home"))
    return render_template("index.html")

@veloxity.route("/login", methods=["GET", "POST"])
def login():
    # User Login Page Rendering and Processing
    if "loggedIn" in session:
        print("User is already logged in. Redirecting to HOME")
        return redirect(url_for("home"))
    if request.method == "POST":
        session['ID'] = request.form["username"]
        if not newLogin(session['ID']):
            if confirmPassword(session['ID'], request.form["password"]):
                session["loggedIn"] = True
                return redirect(url_for("home"))
            print("User has entered an incorrect password.")
            return render_template("login.html", error="Incorrect password or ID.")
        print("User does not have an existing password.")
        return redirect(url_for("create_password"))
    print("Rendering ID input template.")
    return render_template("login.html")

@veloxity.route("/createpassword", methods=["GET", "POST"])
def create_password():
    # Password Creation for New Users
    if request.method == "POST":
        password = request.form["password"]
        if createPassword(session['ID'], password):
            session['loggedIn'] = True
            return redirect(url_for("home"))
    else:
        if "loggedIn" in session:
            return redirect(url_for("home"))
        if "ID" not in session:
            return redirect(url_for("login"))
    return render_template("password.html")

@veloxity.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@veloxity.route("/home")
def home():
    # Renders the home page.
    if "loggedIn" in session:
        return render_template("home.html")
    return redirect(url_for("login"))

@veloxity.route("/data", methods=["GET", "POST"])
def data():
    # Handles submission of user data.
    if "loggedIn" in session:
        if request.method == "POST":
            income = request.form["income"]
            expense = request.form["expenses"]
            profit = request.form["profit"]
            tax = request.form["tax"]
            submitdata(session['ID'], income, expense, profit, tax)
            return redirect(url_for("thanks"))
        else:
            user_id = session['ID']
            try:
                table_exists = findtable(user_id)
                if not table_exists:
                    createtable(user_id)
                fetched_data = fetchdata(user_id)
                return render_template("data.html", username=user_id, data=fetched_data)
            except Exception as e:
                print(f"An error occurred: {e}")
                return "Error", 500
    return redirect(url_for("login"))

@veloxity.route("/thanks")
def thanks():
    # Renders the thanks page.
    if "loggedIn" in session:
        return render_template("thanks.html")
    return redirect(url_for("login"))

if __name__ == "__main__":
    veloxity.run(host="0.0.0.0", port=5000, debug=True)