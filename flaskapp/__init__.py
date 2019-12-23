from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# initialize flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# initialize sqlalchemy
db = SQLAlchemy(app)


from flaskapp import routes

# create Log table if not created
db.create_all()
db.session.commit()
