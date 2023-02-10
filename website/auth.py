from flask import Blueprint, render_template, request, flash

# Set up blueprint variable for Flask app (actual blueprint is called the same as the variable it's contained in)
auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["get", "post"])
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"


@auth.route("/sign-up", methods=["get", "post"])
def sign_up():
    if request.method == "post":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # If form input is incorrect, use Flask's 'flash' method to store error/ success message
        if len(email) < 4:
            flash("E-mail must be at least 4 characters.", category="error")
        elif len(first_name) < 2:
            flash("Name must be at least 2 characters.", category="error")
        elif password1 != password2:
            flash("Passwords do not match.", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category="error")
        else:
            flash("Account created successfully!", category="success")

    return render_template("signup.html")
