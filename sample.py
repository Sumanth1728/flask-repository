
from flask import Flask, render_template, session, redirect, url_for, session,flash,request
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details

from basecong import app
from forms import createcustomer,searchform,EditEmployee,createemloyee
# Now create a WTForm Class
# Lots of fields available:
# http://wtforms.readthedocs.io/en/stable/fields.html
emid=0
class LoginForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''
    user = StringField('UserName',validators=[DataRequired()])
    passl  = StringField("Password",validators=[DataRequired()])
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
    print(form.errors)
    if form.is_submitted():
        print("submitted")
        print(form.errors)
    if form.validate():
        print("valid")
        print(form.errors)
    if form.validate_on_submit():
        print("entered validate")
        cuslast = B_Customer.query.all()[-1]
        cusid="C"+str(int(cuslast.C_id[1:])+1)
        print(cusid,form.name.data,form.age.data,form.email.data,form.address.data,form.phone.data,"password",form.balance.data)
        cus1=B_Customer(C_id=cusid, name=form.name.data, age=form.age.data, email=form.email.data, address=form.address.data, number=form.phone.data, C_pass="password", balance=form.balance.data)
        db.session.add(cus1)
        db.session.commit()
        cardno=B_Customer_Card_Details.query.all()[-1]
        cardid=cardno.Card_No+1
        card1=B_Customer_Card_Details(C_id=cusid, Card_Type="MasterCard", Card_No=cardid, Card_Activate=True)
        db.session.add(card1)
        db.session.commit()
        return render_template('CreateAlert.html',id=id,messages=["hello"])
    else:
        err=form.errors
        for i in err:
            flash(i+"-"+str(err[i]))

    return render_template('CreateNewCustomer.html',id=id,form=form)


@app.route('/admin/<id>/CreateEmployee', methods=['GET', 'POST'])
def CreateEmployee(id):
    form=createemloyee()
    if form.validate_on_submit():
        print("entered validate")
        emplast = B_Employee.query.all()[-1]
        empid="E"+str(int(emplast.E_id[1:])+1)
        print(empid)
        Emp1=B_Employee(E_id=empid, name=form.name.data, age=form.age.data, email=form.email.data, address=form.address.data, number=form.phone.data, E_pass="password")
        db.session.add(Emp1)
        db.session.commit()
        return redirect(url_for("admin",id=id))
    else:
        print(form.errors)
    return render_template('CreateNewEmployee.html',id=id,form=form)



@app.route('/admin/<id>/EditCustomer',methods=['GET', 'POST'])
def EditCustomer(id):


    # Create instance of the form.
    form1 = searchform()

    # If the form is valid on submission (we'll talk about validation next)
    if form1.validate_on_submit():
        # Grab the data from the breed on the form.
        try:
            cust=B_Customer.query.filter_by(C_id=form1.user.data).first()
            return redirect(url_for("EditCustomerDetails",id=id,cid=cust.C_id))
        except Exception as e:
            try:
                cust=B_Customer.query.filter_by(C_email=form1.user.data).first()
                return redirect(url_for("EditCustomerDetails",id=id,cid=cust.C_id))
            except Exception as e:
                print(e)

    return render_template('EditCustomer.html',id=id,form1=form1)


@app.route('/admin/<id>/EditCustomerDeatils/<cid>',methods=['GET', 'POST'])
def EditCustomerDetails(id,cid):

    form=EditEmployee()
    custm=B_Customer.query.filter_by(C_id=cid).first()

    if form.validate_on_submit():
        print("hello",form.name.data,form.age.data,form.address.data,form.address.data,form.phone.data)
        custm=B_Customer.query.filter_by(C_id=cid).first()
        custm.C_name=form.name.data
        custm.C_age=form.age.data
        custm.C_address=form.address.data
        custm.C_number=form.phone.data
        db.session.add(custm)
        db.session.commit()
        return redirect(url_for("admin",id=id))
    else:
        print(form.errors)


    return render_template('EditCustomerDetails.html',id=id, form=form,custm=custm)






@app.route('/admin/<id>/SearchCustomer',methods=['GET', 'POST'])
def SearchCustomer(id):

    cust= False
    cards1=False
    # Create instance of the form.
    form = searchform()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.
        m = form.user.data
        try:
            cust=B_Customer.query.filter_by(C_id=form.user.data).first()

            cards1=B_Customer_Card_Details.query.filter_by(C_id=cust.C_id).all()
        except Exception as e:
            try:
                cust=B_Customer.query.filter_by(C_email=form.user.data).first()
                cards1=B_Customer_Card_Details.query.filter_by(C_id=cust.C_id).all()
            except Exception as e:
                a=0
    return render_template('SearchCustomor.html',id=id, form=form, cust=cust,cards1=cards1)




















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
