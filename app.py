from flask import Flask
from flask import redirect, url_for, render_template, request, session

app = Flask(__name__, static_url_path='/static')
app.secret_key = "asdfghjkl"

@app.route("/")
def home():
    return render_template("index.html", content="Testing")

@app.route("/home/")
def homeRedirect():
    return redirect(url_for("home"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["email"]
        session["user_email"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")
# 
@app.route("/user")
def user():
    if "user_email" in session:
        user = session["user_email"]
    else:
        return redirect(url_for("login"))
    return render_template("index.html", activesession=True)

@app.route("/logout")
def logout():
    session.pop("user_email", None)
    return redirect(url_for("login"))
 
if __name__ == "__main__":
    app.run(debug=True)