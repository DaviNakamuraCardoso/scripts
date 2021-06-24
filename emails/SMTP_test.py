import smtplib
smtp_object = smtplib.SMTP('smtp.mail.com', 587) # Security measures prevent Python from being able to log in Gmail,
# Outlook and Yahoo # The second argument is the port, a integer, most ever 587
smtp_object.ehlo() # When successful, the smtp_object.ehlo() returns the integer 250
smtp_object.starttls() # If using the 587 port argument, you have to call the .starttls() method to enable encryption
smtp_object.login('example@mail.com', 'password') # Once with the encryption enabled, you can log in with username and
# password
smtp_object.sendmail('example@mail.com', 'recipient@mail.com', 'Subject: Hello, World!\n HELLO!')  # The sendmail method
# requires three arguments:
# Your email
# Your recipient's email as a string or a list
# The email body

smtp_object.quit()  # The quit() method disconnects you from the server. The 221 return value means you have
# successfully disconnected





