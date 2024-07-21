from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# import os
# from dotenv import load_dotenv

# load_dotenv()

#CREATE WEBAPP
app = Flask(__name__)

#API INFO


#CREATE DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///starter.db"
db = SQLAlchemy()
db.init_app(app)

#CREATE DB TABLE
class Starter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title  = db.Column(db.String, unique=True, nullable=False)
with app.app_context():
    db.create_all()

#WEB HOME PAGE
@app.route('/')
def welcome():
    return render_template("index.html")

#RUN THE WEBAPP
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)