import ezgmail
import os

os.makedirs('Revelation', exist_ok=True)

#ezgmail.send('davinakamuracardoso@gmail.com', 'Teste', 'TESTANDO') # Once with the .json token, it's easy to send emails
# using the ezgmail
#ezgmail.send('gabinakacardoso@gmail.com', 'IIIIIIIIUUUUUU', 'IUIUIUIUIUIU', ['/home/davi/Downloads/melado.jpg',
                                           #                                  '/home/davi/Downloads/melado_fundo.jpg'])
# As part of the anti-spam and security gmail features, it might not send multiple emails with the same message or
# with .zip or .exe extensions

# It's possible to add cc and bcc keyword arguments to your message
#ezgmail.send('rogerioferrantecardoso@gmail.com', 'TESTE', 'TESTANDO ENVIO DE EMAILS', cc='gabinakacardoso@gmail.com',
 #            bcc='davinakamuracardoso@gmail.com')

# If you want to remember your token's gmail address:
ezgmail.init()
print(ezgmail.EMAIL_ADDRESS)

# Be sure to keep your .json token secret
unread_threads = ezgmail.unread() # List of GmailThread objects
print(ezgmail.summary(unread_threads))
print(len(unread_threads))
print(str(unread_threads))
print(len(unread_threads[0].messages))
print(str(unread_threads[0].messages[0]))
print(unread_threads[0].messages[0].subject)
print(unread_threads[0].messages[0].body)
print(unread_threads[0].messages[0].timestamp)
print(unread_threads[0].messages[0].sender)
print(unread_threads[0].messages[0].recipient)

# Similar to ezgmail.unread() is the ezgmail.recent(), that returns the 25 most recent threads
recent_threads = ezgmail.recent()
print(len(recent_threads))
recent_threads = ezgmail.recent(maxResults=100) # The optional maxResults argument changes this limit
print(len(recent_threads))

# Searching for emails
result_threads = ezgmail.search('TESTANDO ENVIO DE EMAILS')
print(len(result_threads))  # Like unread() and recent() functions, search() returns a array
print(ezgmail.summary(result_threads))
# It's possible to add the search function the current arguments:
# 'label:UNREAD' for unread emails
# 'from: example@gmail.com' the emails from example
# 'subject: hello' for emails with 'hello' in the subject
# 'has: attachment' for emails with file attachments

# Downloading attachments from a email account

threads = ezgmail.search('Revelation')
threads[0].messages[0].attachments
threads[0].messages[0].downloadAllAttachments(downloadFolder='Revelation')

