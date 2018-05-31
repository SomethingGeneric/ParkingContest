# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("parkingcontestfocs@gmail.com", "thisisastrongpassword")
 
# message to be sent
message = "Message_you_need_to_send"
 
# sending the mail
s.sendmail("parkingcontestfocs@gmail.com", "mcompton2002@gmail.com", message)
 
# terminating the session
s.quit()
