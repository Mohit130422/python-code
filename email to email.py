#email to email
import smtplib
send_mail=input("Enter your Gmail:")
receivers_mail=input("Enter receivers Gmail:")
message="""From:From Person %s 
To:To Person %s
Subject:Sending SMTP e-mail
This is a test e-mail message.
"""%(send_mail,receivers_mail)
try:
    password = input("Enter the Password:")
    print(password)
    smtp0bj = smtplib.SMTP('gmail.com',587)
    smtp0bj.login(send_mail,password)
    smtp0bj.sendmail(send_mail,receivers_mail,message)
    print("Successfully sent email..")
except Exception as e:
    print("Error:unable to send email",e)
#run