from fileinput import filename
from flask import *

app = Flask(__name__)

@app.route("/login")
def home():
    return render_template("login.html")


if __name__=="__main__":
    app.run(debug=True)