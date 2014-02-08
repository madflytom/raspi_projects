#!/usr/bin/python
import httplib
import smtplib
import mimetypes
# Import the email modules we'll need
import email
import email.mime.application
#Import sys to deal with command line arguments
import sys

def get_status_code(host, path="/"):
    """ This function retreives the status code of a website by requesting
        HEAD data from the host. This means that it only requests the headers.
        If the host cannot be reached or something else goes wrong, it returns
        None instead.
    """
    try:
        conn = httplib.HTTPConnection(host)
        conn.request("HEAD", path)
        return conn.getresponse().status
    except StandardError:
        return None


print get_status_code("google.com") # prints 200
if get_status_code("google.com") != 200:
	 
	# Create a text/plain message
	msg = email.mime.Multipart.MIMEMultipart()
	msg['Subject'] = 'somesite.com is down!'
	msg['From'] = 'someemailaddress@somedomain.com'
	msg['To'] = 'receiver@somedomain.com'
	 
	# The main body is just another attachment
	body = email.mime.Text.MIMEText("""It appears your site is not responding.  This message is being sent from your monitoring raspberry pi.""")
	msg.attach(body)
	 
	# send via Gmail 
	# port 25 packets to be port 587 and it is trashing port 587 packets.
	# So, I use the default port 25, but I authenticate.
	# Replace the login and sendmail addresses with your own sender/receiver and login info.
	s = smtplib.SMTP('smtp.gmail.com:587')
	s.starttls()
	s.login('someemailaddress@somedomain.com','somepassword')
	s.sendmail('senderaddresss@somedomain.com',['receiver@somedomain.com'], msg.as_string())
	s.quit()
