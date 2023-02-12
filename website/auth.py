from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, login_required, current_user

# Set up blueprint variable for Flask app (actual blueprint is called the same as the variable it's contained in)
auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # Check if user exists:
        if user := User.query.filter_by(email=email).first():
            # If user exists, check if password is correct:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                # Log in user and cache it (until Flask server gets closed):
                login_user(user, remember=True)
                return redirect(url_for("views.home"))

            else:
                flash("Incorrect password.", category="error")
        else:
            flash("User does not exist.", category="error")

    return render_template("login.html")


@auth.route("/logout")
# Decorator that prevents logout function being called if no user is logged in
@login_required
def logout():
    # Logs out current logged-in user:
    logout_user()
    return redirect(url_for("auth.login"))


@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        # Check if e-mail is already in use:
        if user := User.query.filter_by(email=email).first():
            flash("E-mail is already in use.", category="error")

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
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method="sha256"))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created successfully!", category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html")
