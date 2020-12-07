
from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details

from basecong import app
from forms import createcustomer
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


##############################################
#############Login #########################3
#############################################
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

        try:
            Admin1 = B_Admin.query.filter_by(A_id=form.user.data).first()
            print("A")
            if(Admin1.A_pass==form.passl.data):
                return redirect(url_for("admin",id=m))
            else:
                return "username and pasword doesn't match"

        except Exception as e:
            try:
                Emp1 = B_Employee.query.filter_by(E_id=form.user.data).first()
                if(Emp1.E_pass==form.passl.data):
                    return redirect(url_for("employee",id=m))

                else:
                    return "username and pasword doesn't match"

            except Exception as e:

                try:
                    cmp1 = B_Customer.query.filter_by(C_id=form.user.data).first()
                    if(cmp1.C_pass==form.passl.data):
                        return redirect(url_for("customer",id=m))

                    else:

                        return "username and pasword doesn't match"

                except Exception as e:


                    return(e)


    return render_template('index.html', form=form)


##############################################
#############Admin ##########################
#############################################

@app.route('/admin/<id>', methods=['GET', 'POST'])
def admin(id):

    return render_template('admin.html',id=id)

@app.route('/admin/<id>/CreateCustomer', methods=['GET', 'POST'])
def CreateCustomer(id):
    form=createcustomer()
    if form.validate_on_submit():
        print("entered validate")
        Emplast = B_Customer.query.all()[-1]
        Empid="C"+str(int(Emplast.C_id[1:])+1)
        print(Empid,form.name.data,form.age.data,form.email.data,form.address.data,form.phone.data,"password",form.balance.data)
        cus1=B_Customer(C_id=Empid, name=form.name.data, age=form.age.data, email=form.email.data, address=form.address.data, number=form.phone.data, C_pass="password", balance=form.balance.data)
        db.session.add(cus1)
        db.session.commit()
        return redirect(url_for("admin",id=id))



    return render_template('CreateNewCustomer.html',id=id,form=form)























##############################################
#############Employee ##########################
#############################################



@app.route('/employee/<id>', methods=['GET', 'POST'])
def employee(id):

    return render_template('employee.html',id=id)

















##############################################
#############Customer ##########################
#############################################


@app.route('/customer/<id>', methods=['GET', 'POST'])
def customer(id):

    return render_template('customer.html',id=id)


if __name__ == '__main__':
    app.run(debug=True)
