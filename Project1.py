import smtplib, ssl, getpass, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp.gmail.com'
port = 465
subject = 'Email with attachment test'
body = 'This is a trail mail to test for sending an attachment'
sender_email = 'sender_mail@gmail.com'
receiver_email = 'receiver_mail@gmail.com'
password = getpass.getpass('enter password: ')

message = MIMEMultipart()
message['Subject'] = subject
message['From'] = sender_email
message['To'] = receiver_email

message.attach(MIMEText(body, 'plain'))

filename = 'document.pdf'

with open(filename, 'rb') as attachment:
	part = MIMEBase('application', 'octet-stream')
	part.set_payload(attachment.read())
	
encoders.encode_base64(part)

part.add_header('content-Disposition', f'attachment; filename= {filename}')

message.attach(part)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
	server.login(sender_email, password)
	server.sendmail(sender_email, receiver_email, message.as_string())
