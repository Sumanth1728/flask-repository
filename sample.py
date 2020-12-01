
from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details
from loginfunc import login


app = Flask(__name__)
# Configure a secret SECRET_KEY
# We will later learn much better ways to do this!!
app.config['SECRET_KEY'] = 'mysecretkey'

# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
class LoginForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    user = StringField('UserName',validators=[DataRequired()])
    passl  = StringField("Password")
    submit = SubmitField('Submit')



@app.route('/', methods=['GET', 'POST'])
def index():

    # Create instance of the form.
    form = LoginForm()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():

        # Grab the data from the breed on the form.

        m=form.user.data
        n=form.passl.data
        print(m,n)
        Admin1 = B_Admin.query.filter_by(A_id==id).first()
        """
        if (l[0]=="Admin")
            return redirect(url_for("admin",id=m))

        elif(l[0]=="Employee"):
            return redirect(url_for("employee",id=m))

        elif(l[0]=="Customer"):
            return redirect(url_for("customer",id=m))

        else:
            return l[0]
     """
    return render_template('index.html', form=form)

@app.route('/admin/<id>', methods=['GET', 'POST'])
def admin(id):

    return render_template('admin.html',id=id)

@app.route('/employee/<id>', methods=['GET', 'POST'])
def employee(id):

    return render_template('employee.html',id=id)

@app.route('/customer/<id>', methods=['GET', 'POST'])
def customer(id):

    return render_template('customer.html',id=id)


if __name__ == '__main__':
    app.run(debug=True)
























"""
from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details
user=str(input("enter the username"))
pass1=str(input("enter the password"))
try:
    Admin1 = B_Admin.query.filter_by(A_id=user).first()
    if(Admin1.A_pass==pass1):

        print("admin logged in")
    else:
        print(" admin username and pasword doesn't match")

except Exception as e:
    try:
        Emp1 = B_Employee.query.filter_by(E_id=user).first()
        if(Emp1.E_pass==pass1):
            print("employee logged in")

        else:
            print("employee username and pasword doesn't match")

    except Exception as e:

        try:
            cmp1 = B_Customer.query.filter_by(C_id=user).first()
            if(cmp1.C_pass==pass1):

                print("customer logged in")

            else:
                print("customer username and pasword doesn't match")

        except Exception as e:

            print("username doesn't exist")
"""
