

# Now that the table has been created by running
# BasicModelApp and SetUpDatabase we can play around with CRUD commands
# This is just an overview, usually we won't run a single script like this
# Our goal here is to just familiarize ourselves with CRUD commands

from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details

###########################
###### CREATE ############
#########################
db.create_all()

admin1=B_Admin("A1","password")
db.session.add(admin1)

emp=B_Employee("E1","sumanth",22,"hello@gmail.com","5-786",987897688868,"password")

cus1=B_Customer("C1","JC",22,"jc@gmail.com","USA",9876543221,"password",20200)

db.session.add(emp)



db.session.add(cus1)



db.session.commit()


admin=B_Admin.query.all()
print(admin)

employee=B_Employee.query.all()
print(employee)
customer=B_Customer.query.all()
print(customer)
