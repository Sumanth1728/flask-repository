from tables import db, B_Admin ,B_Employee ,B_Customer,B_Customer_transactions,B_Customer_Card_Details




def login(id):
    id=str(id)
    try:
        Admin1 = B_Admin.query.filter_by(A_id=id).first()
        return ["Admin",Admin1.A_pass]

    except Exception as e:
        try:
            Emp1 = B_Employee.query.filter_by(E_id=id).first()
            return ["Employee",Emp1.E_pass]

        except Exception as e:

            try:
                cmp1 = B_Customer.query.filter_by(C_id=id).first()
                return ["Customer",cmp1.C_pass]
            except Exception as e:
                return e



n=login("A1")
print(n)
if (n[0]=="Admin"):
    print("matched")









"""
Admin1=B_Admin.query.filter_by(A_id=user).first()
adm=B_Admin.query.filter_by(A_id="A1").first_or_404()
print(adm)
print(Admin1.A_pass)

Admin1=B_Admin.query.filter_by(A_id=user).first()
adm=B_Admin.query.filter_by(A_id="A1").first_or_404()
print(adm)
print(Admin1.A_pass)
"""
