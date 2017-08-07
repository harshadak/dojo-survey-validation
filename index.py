from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "Secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ["POST"])
def result():
    name_val = request.form["name_key"]
    location_val = request.form["location_key"]
    language_val = request.form["language_key"]
    comment_val = request.form["comment_key"]

    # Form validation
    if (len(name_val) < 1):
        flash("The name field cannot be empty!")
    if (len(comment_val) < 1):
        flash("Comment section cannot be empty!")
    if (len(comment_val) > 120):
        flash("Comment section can be no longer than 120 characters.")

    # This if condition helps you see all the flash messages on root route
    if '_flashes' in session:
        return redirect('/')
    else:
        return render_template("result.html", name = name_val, location = location_val, language = language_val, comment = comment_val)

app.run(debug = True)