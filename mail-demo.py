import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
emailAddress = os.getenv('EMAILADDRESS')
emailPass = os.getenv('EMAILPASSWORD')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(emailAddress, emailPass)

    subject = 'First automation email!!'
    body = 'HIIIIIIIIIIIII. This was sent from my python script'

    msg = f'Subject: {subject} \n\n{body}'

    smtp.sendmail(emailAddress, 'heather.witherow@gmail.com', msg)