from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class HelpRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    location = db.Column(db.String(100))
    contact = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
