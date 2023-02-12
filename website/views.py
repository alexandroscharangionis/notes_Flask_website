from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db


# Set up blueprint variable for Flask app (actual blueprint is called the same as the variable it's contained in)
views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
# Decorator that prevents accessing homepage unless logged in
@login_required
def home():
    if request.method == "POST":
        note = request.form.get("note")
        if len(note) < 1:
            flash("Note is too short.", category="error")
        else:
            new_note = Note(text=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added.", category="success")

            # 'user' arg references the current user via the current_user method inside the html template, so we can display some html elements only if user is signed-in
    return render_template("home.html", user=current_user)
