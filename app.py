from fileinput import filename
from flask import *
from flask_mysqldb import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

app = Flask(__name__)

@app.route("/login")
def home():
    return render_template("login.html")


if __name__=="__main__":
    app.run(debug=True)