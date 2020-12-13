from basecong import db
#####################################
####################################
###################################

# Let's create our first model!
# We inherit from db.Model class



class B_Admin(db.Model):


    __tablename__ = 'B_Admin'

    A_id = db.Column(db.Text,primary_key=True)

    A_pass=db.Column(db.Text)

    def __init__(self,A_id,A_pass):
        self.A_id=A_id
        self.A_pass=A_pass


    def __repr__(self):
        #
        return f"admin{self.A_id} fetched and password = {self.A_pass}"


######################################################################################################################################
########################################################################################################################################



class B_Employee(db.Model):

    # If you don't provide this, the default table name will be the class name
    __tablename__ = 'B_Employee'

    # Now create the columns
    # Lots of possible types. We'll introduce through out the course
    # Full docs: http://docs.sqlalchemy.org/en/latest/core/types.html

    #########################################
    ## CREATE THE COLUMNS FOR THE TABLE ####
    #######################################

    # Primary Key column, unique id for each puppy
    E_id = db.Column(db.Text,primary_key=True)
    E_name = db.Column(db.Text)
    E_age = db.Column(db.Integer)
    E_email=db.Column(db.Text,unique=True)
    E_address=db.Column(db.Text)
    E_number = db.Column(db.Integer)
    E_pass=db.Column(db.Text)

    # This sets what an instance in this table will have
    # Note the id will be auto-created for us later, so we don't add it here!
    def __init__(self,E_id,name,age,email,address,number,E_pass):

        self.E_id = E_id
        self.E_name = name
        self.E_age = age
        self.E_email=email
        self.E_address=address
        self.E_number=number
        self.E_pass=E_pass


    def __repr__(self):

        # This is the  representation of B_Employee  in the model

        m=[self.E_id,self.E_name,self.E_age,self.E_email,self.E_address,self.E_number,self.E_pass]
        return f"employee fetched"





######################################################################################################################################
########################################################################################################################################






class B_Customer(db.Model):

    __tablename__ = 'B_Customer'
    C_id = db.Column(db.Text,primary_key=True)
    C_name = db.Column(db.Text)
    C_age = db.Column(db.Integer)
    C_email=db.Column(db.Text,unique=True)
    C_address=db.Column(db.Text)
    C_number = db.Column(db.Integer)
    C_pass=db.Column(db.Text)
    C_balance=db.Column(db.Float)
    C_Cards = db.relationship('B_Customer_Card_Details',backref='B_Customer',lazy='dynamic')
    C_Transacs = db.relationship('B_Customer_transactions',backref='B_Customer',lazy='dynamic')


    def __init__(self,C_id,name,age,email,address,number,C_pass,balance):

        self.C_id = C_id
        self.C_name = name
        self.C_age = age
        self.C_email=email
        self.C_address=address
        self.C_number=number
        self.C_pass=C_pass
        self.C_balance=balance


    def __repr__(self):
        a=[self.C_id,self.C_name,self.C_age,self.C_email,self.C_address,self.C_number,self.C_pass,self.C_balance]
        return f"customer fetched"





######################################################################################################################################
########################################################################################################################################




class B_Customer_transactions(db.Model):
    __tablename__ = 'B_Customer_transactions'
    id = db.Column(db.Integer,primary_key=True)
    C_id = db.Column(db.Text,db.ForeignKey('B_Customer.C_id'))
    T_id = db.Column(db.Integer)
    Card_Number=db.Column(db.Integer,db.ForeignKey('B_Customer_Card_Details.Card_No'))
    T_amount=db.Column(db.Float)
    T_Type=db.Column(db.Text)
    R_id=db.Column(db.Text)

    def __init__(self,C_id,T_id,Card_Number,T_amount,T_Type,R_id):

        self.C_id = C_id
        self.T_id = T_id
        self.Card_Number=Card_Number
        self.T_amount=T_amount
        self.T_Type=T_Type
        self.R_id=R_id


    def __repr__(self):
        return [self.id,self.C_id,self.self.T_id,self.Card_Number,self.T_amount,self.T_Type,self.R_id]



######################################################################################################################################
########################################################################################################################################




class B_Customer_Card_Details(db.Model):

    __tablename__ = 'B_Customer_Card_Details'
    id = db.Column(db.Integer,primary_key=True)
    C_id = db.Column(db.Text,db.ForeignKey('B_Customer.C_id'))
    Card_Type = db.Column(db.Text)
    Card_No = db.Column(db.Integer,unique=True)
    Card_Activate=db.Column(db.Boolean)
    # add Expiry date to card details
    #add access type to card details
    Transacs = db.relationship('B_Customer_transactions',backref='B_Customer_Card_Details',lazy='dynamic')



    def __init__(self,C_id,Card_Type,Card_No,Card_Activate):

        self.C_id = C_id
        self.Card_Type = Card_Type
        self.Card_No=Card_No
        self.Card_Activate=Card_Activate


    def __repr__(self):
        return [self.id,self.self.self.self.C_id,self.self.self.Card_Type,self.self.Card_No,self.Card_Activate]


#creating Table instances
db.create_all()
