@app.route('/admin/<id>/EditCustomer',methods=['GET', 'POST'])
def EditCustomer(id):

    cust= False
    cards1=False
    # Create instance of the form.
    form1 = searchform()

    # If the form is valid on submission (we'll talk about validation next)
    if form1.validate_on_submit():
        # Grab the data from the breed on the form.
        try:
            cust=B_Customer.query.filter_by(C_id=form1.user.data).first()
            emid=custm.C_id
        except Exception as e:
            try:
                cust=B_Customer.query.filter_by(C_email=form1.user.data).first()
                emid=custm.C_id
            except Exception as e:
                a=0
    if form.validate_on_submit():
        print("hello",form.name.data,form.age.data,form.address.data,form.address.data,form.phone.data)
        z=emid
        custm=B_Customer.query.filter_by(C_id=z).first()
        custm.C_name=form.name.data
        custm.C_age=form.age.data
        custm.C_address=form.address.data
        custm.C_number=form.phone.data
        db.session.add(custm)
        db.session.commit()
        return redirect(url_for("admin",id=id))
    else:
        print(form.errors)
    return render_template('EditCustomer.html',id=id, form=form,form1=form1, cust=cust,cards1=cards1)
