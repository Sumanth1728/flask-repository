from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,Length
from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details

class createcustomer(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired()])
    phone=StringField('Phone Number',validators=[DataRequired()])
    balance=StringField('Current Desposited Amount',validators=[DataRequired()])
    age=StringField('Age',validators=[DataRequired()])
    address=StringField('Address',validators=[DataRequired()])
    submit=SubmitField("create user")

class createemloyee(FlaskForm):
    E_name=StringField('emp_name',validators=[DataRequired(),Length(min=4,max=15)])
    E_id=StringField('ID',validators=[DataRequired(),Length(min=4,max=15)])
    E_email=StringField('emp_Email',validators=[DataRequired(),Email()])
    E_number=StringField('emp_phone',validators=[DataRequired()])
    E_state=StringField('emp_state',validators=[DataRequired(),Length(min=3,max=15)])
    E_pincode=StringField('emp_pincode',validators=[DataRequired()])
    E_address=StringField('emp_address',validators=[DataRequired(),Length(min=10,max=40)])
    submit=SubmitField("create employee")
