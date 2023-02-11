from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(10000))
    # Get time of note creation automatically via func.now() + corresponding timezone via DateTime:
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Link note to the user's (who created it) id:
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Class field for referencing all notes the user created
    notes = db.relationship("Note")
