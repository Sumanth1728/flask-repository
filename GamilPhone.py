import smtplib
from email.message import EmailMessage

def Email_Alert(subject,body,to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to
    msg['from']="sumanthpasupuleti1727@gmail.com"

    user="sumanthpasupuleti1727@gmail.com"
    passw="jnlarwfyhojncpip"
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(user,passw)
    server.send_message(msg)
    server.quit()

if __name__=='__main__':
    Email_Alert("Email Checking","this is to check that whether the message is going using email","jayaandsreenu@gmail.com ")
