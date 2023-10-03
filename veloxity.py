#
#   Developed by Eddie Gu for Veloxity
#   All rights reserved
#   Unauthorized distribution or use is strictly prohibited
#   @kyrofx on GitHub

from etc import *
from loginMethods import *
from dbConnect import *
from flask import *

veloxity = Flask(__name__)
veloxity.secret_key = "VqMXxcFU00cP9oi7hKEoUjyvmNGUWjQO7dcr6QRE0hzwCTMy1p"


@veloxity.route("/", methods=["GET"])
def index():
    if "ID" in session:
        return redirect(url_for("home"))
    else:
        return render_template("index.html")


@veloxity.route("/login", methods=["GET", "POST"])
def login():
    if "loggedIn" in session:
        print("User is already logged in. Redirecting to HOME")
        return redirect(url_for("home"))
    elif request.method == "POST":
        print("User is using POST Request. Logging in.")
        # login stuff
        username = request.form["username"]
        session['ID'] = username
        if newLogin(username):
            print("User does not have an existing password.")
            return redirect(url_for("create_password"))
        elif newLogin(username) is None:
            print("User does not exist. Redirecting to index.")
            return redirect(url_for("index"))
        elif newLogin(username) is False:
            print("User has a password. Redirecting to login.")
            return redirect(url_for("password"))
    else:
        print("Rendering ID input template.")
        return render_template("login.html")
@veloxity.route("/passwordcreate", methods=["GET", "POST"])
def create_password():
    if request.method == "POST":
        password = request.form["password"]
        if createPassword(session['ID'], password):
            session['loggedIn'] = True
            return redirect(url_for("home"))

    else:
        return render_template("create_password.html")


@veloxity.route("/password", methods=["GET", "POST"])
def password():
    if request.method == "POST":
        password = request.form["password"]
        if confirmPassword(session['ID'], password):
            session['loggedIn'] = True
            print("password is correct")
            return redirect(url_for("home"))
        else:
            print("password is incorrect")
            return redirect(url_for("password"))
    else:
        return render_template("password.html")






@veloxity.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@veloxity.route("/home")
def home():
    if "loggedIn" in session:
        return render_template("home.html", username=session['ID'])
    else:
        return redirect(url_for("login"))


@veloxity.route("/data")
def data():
    if "loggedIn" in session:
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
    else:
        return redirect(url_for("login"))


######################################################################################################################
###  A P I  R O U T E S  #############################################################################################
######################################################################################################################
######################################################################################################################
######################################################################################################################
########################################################################################################## :3 MAFIA ##
######################################################################################################################


veloxity.route("/api/submitdata", methods=["POST"])


def submitdata():
    if "ID" in session & session['loggedIn'] is True:
        expense = request.form["expense"]
        revenue = request.form["revenue"]
        identification = session['ID']
        if apisubmitdata(expense, revenue, identification):
            return "Success", 200
        else:
            return "Error", 500
    else:
        return "Unauthorized", 401


if __name__ == "__main__":
    veloxity.run(host="0.0.0.0", port=5000, debug=True)
