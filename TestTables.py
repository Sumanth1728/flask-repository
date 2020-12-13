

# Now that the table has been created by running
# BasicModelApp and SetUpDatabase we can play around with CRUD commands
# This is just an overview, usually we won't run a single script like this
# Our goal here is to just familiarize ourselves with CRUD commands

from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details

cust=B_Customer.query.filter_by(C_id="C1").first()
cust1=cust
cust1.C_name="Jaya Chandra"
db.session.add(cust1)
db.session.commit()
"""

cuslast = B_Customer.query.filter_by(C_id="C6").all()
for i in cuslast:
    print(i.C_name)

cusid='C'+str(int(Emplast.C_id[1:])+1)
cus1=B_Customer(cusid,"Revanth",22,"Revanth@gmail.com","USA",9879543221,"password",20200)
db.session.add(cus1)
db.session.commit()

###########################
###### CREATE ############
#########################
db.create_all()

#admin1=B_Admin(A_id="A1",A_pass="password")
#db.session.add(admin1)

#emp=B_Employee("E1","sumanth",22,"s@gmail.com","vijayawada",9638521478,"password")

cus1=B_Customer("C1","JC",22,"jc@gmail.com","USA",9876543221,"password",20200)

#db.session.add(emp)
db.session.add(cus1)
db.session.commit()

card1=B_Customer_Card_Details(C_id="C1", Card_Type="MasterCard", Card_No=456484560001, Card_Activate=True)
db.session.add(card1)



db.session.commit()



employee=B_Employee.query.all()
print(employee)
customer=B_Customer.query.all()
print(customer)
"""
