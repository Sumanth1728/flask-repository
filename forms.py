from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField,RadioField,SelectField,TextField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length
class createcustomer(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    phone=StringField('Phone Number',validators=[DataRequired()])
    balance=StringField('Current Desposited Amount')
    age=StringField('Age',validators=[DataRequired()])
    address=TextAreaField('Address',validators=[DataRequired()])
    submit=SubmitField("create")

class createemloyee(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    phone=StringField('Phone Number',validators=[DataRequired()])
    age=StringField('Age',validators=[DataRequired()])
    address=TextAreaField('Address',validators=[DataRequired()])
    submit=SubmitField("create")

class searchform(FlaskForm):
    user=StringField('Enter Name or Email addrees ',validators=[DataRequired()])
    submit=SubmitField("Search")

class EditEmployee(FlaskForm):
    name=StringField('Name')
    phone=StringField('Phone Number')
    balance=StringField('Current Desposited Amount')
    age=StringField('Age')
    address=TextAreaField('Address')
    submit=SubmitField("Edit")
