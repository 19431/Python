from backports import ssl
from imapclient import IMAPClient
context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
imapObj = IMAPClient('imap.mail.yahoo.com', ssl=True, ssl_context=context)
email = input('Enter email address here ')
password= input('Enter password here ')
imapObj.login(email, password)

inbox= imapObj.select_folder('INBOX')

