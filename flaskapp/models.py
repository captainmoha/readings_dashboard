from datetime import datetime as dt
from flaskapp import db

class Log(db.Model):
    '''
        Logger table class
        id, id of log
        time_stamp, time it was created
    '''

    id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.DateTime, nullable=False, default=dt.utcnow)