import smtplib

gmail_user = 'parkingcontestfocs@gmail.com'  
gmail_password = 'thisisastrongpassword'

to = ['mcompton2002@gmail.com']
sent_from = gmail_user

email_text = '''
From: parkingcontestfocs@gmail.com
To: mcompton2002@gmail.com
Subject: OOF

L
'''

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
except:  
    print 'Something went wrong...'
