from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length
class createcustomer(FlaskForm):
    username=StringField('username',validators=[DataRequired(),Length(min=4,max=15)])
    Email=StringField('Email',validators=[DataRequired(),Email()])
    phone=StringField('phone',validators=[DataRequired()])
    state=StringField('state',validators=[DataRequired(),Length(min=3,max=15)])
    pincode=StringField('pincode',validators=[DataRequired()])
    address=StringField('address',validators=[DataRequired(),Length(min=10,max=40)])
    submit=SubmitField("create user")

class createemloyee(FlaskForm):
    emp_name=StringField('emp_name',validators=[DataRequired(),Length(min=4,max=15)])
    emp_Email=StringField('emp_Email',validators=[DataRequired(),Email()])
    emp_phone=StringField('emp_phone',validators=[DataRequired()])
    emp_state=StringField('emp_state',validators=[DataRequired(),Length(min=3,max=15)])
    emp_pincode=StringField('emp_pincode',validators=[DataRequired()])
    emp_address=StringField('emp_address',validators=[DataRequired(),Length(min=10,max=40)])
    submit=SubmitField("create employee")
