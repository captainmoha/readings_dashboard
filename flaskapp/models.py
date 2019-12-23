from datetime import datetime as dt
from flaskapp import db

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.DateTime, nullable=False, default=dt.utcnow)