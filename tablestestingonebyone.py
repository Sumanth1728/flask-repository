import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
######################################
#### SET UP OUR SQLite DATABASE #####
####################################

# This grabs our directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# Connects our Flask App to our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#####################################
####################################
###################################

# Let's create our first model!
# We inherit from db.Model class



class B_Admin(db.Model):

    A_id = db.Column(db.Integer,primary_key=True)
    A_pass=db.Column(db.Text)

    def __init__(self,A_pass):
        self.A_pass=A_pass

    def __repr__(self):
        #
        return f"{self.A_id} password is {self.A_pass}"
