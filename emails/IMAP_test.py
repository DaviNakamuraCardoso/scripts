# import imaplib - Python provides a IMAP module, but the third-party imapclient is easier to use
import imapclient
imap_object = imapclient.IMAPClient('imap.gmail.com', ssl=True) # Again, security measures prevent python from be able
# to log in to Gmail, Outlook and Yahoo servers
# Most servers require a encryption, so pass the ssl=True argument

imap_object.login('example@mail.com', 'password') # Once connected, pass the account and password arguments to login
imap_object.select_folder('INBOX', readonly=True) # First you must select a folder you want to search in.
# To see all the folders, call the list_folders() method, that will return you a list of tuples. There are three values
# in each of the tuples: A tuple of the folder's flag, a tuple of the delimiter used and finally a tuple with the
# folder's full name
UIDs = imap_object.search(['SINCE 05-Jul-2020']) # ...then search for emails with the IMAP keys, like:
# ALL - returns all the messages in the folder, but you can size a limit
# SINCE, BEFORE, ON - messages received since, before and on a date
# SUBJECT, BODY, TEXT - returns messages where certain string is found on subject, body or either
# FROM, TO, CC, BCC - searches certain from, to, cc or bcc messages
# And lots of other arguments!
# If you want to size limits, call: imaplib._MAXLINE = 10000

print(UIDs)
raw_messages = imap_object.fetch([40041], ['BODY[]', 'FLAGS']) # If you want to mark your emails as read, pass the
# readonly = False to select_folder() method

import pyzmail
message = pyzmail.PyzMessage.factory(raw_messages[40041][b'BODY']) # First we create a pyzmail object, where the
# b is for bytes value
# Now message contains a PyzMessage object, which has several methods that make easy to get the information you need,
# such as:
message.get_subject() # The subject
message.get_address('from') # The sender
message.get_addresses('to') # The recipient
message.get_addresses('cc') # The cc(s)
message.get_addresses('bcc') # The bcc(s)

# Emails can have plain text, HTML or both. Plaintext contains only text, while HTML contains colors, images and others
# features and styles that make the message look like a little site. For both, there's the method get_payload(), that
# returns it in the format of a bytes data. But to get a string with it's value, you have to pass the method .decode()
# with the argument text_/html_ part.charset
print(message.text_part != None)  #
message.text_part.get_payload().decode(message.text_part.charset)
print(message.html_part != None)
print(message.html_part.get_patload().decode(message.html_part.charset))
# Deleting emails
# If you want to send it to trash, pass the imap object the method delete_messages and the UIDs. Else, pass the
# expunge() method to permanently delete messages
imap_object.logout() # Finally, logout



