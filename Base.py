from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                     RadioField,SelectField,TextField,
                     TextAreaField,SubmitField)
from wtforms.validators import DataRequired
from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details


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

        try:
            Admin1 = B_Admin.query.filter_by(A_id==form.user.data).first()
            print("A")
            if(Admin1.A_pass==form.passl.data):
                return redirect(url_for("admin"))
            else:
                print("username and pasword doesn't match")

        except Exception as e:
            try:
                Emp1 = B_Employee.query.filter_by(E_id==form.user.data).first()
                if(Emp1.E_pass==form.passl.data):
                    return redirect(url_for("employee"))

                else:
                    print("username and pasword doesn't match")

            except Exception as e:

                try:
                    cmp1 = B_Customer.query.filter_by(C_id==form.user.data).first()
                    if(cmp.C_pass==form.passl.data):
                        return redirect(url_for("customer"))

                    else:
                        print("username and pasword doesn't match")

                except Exception as e:

                    print(e)



    return render_template('index.html', form=form)

@app.route('/admin')
def admin():

    return render_template('admin.html')

@app.route('/employee')
def employee():

    return render_template('employee.html')

@app.route('/customer')
def customer():

    return render_template('customer.html')


if __name__ == '__main__':
    app.run(debug=True)
