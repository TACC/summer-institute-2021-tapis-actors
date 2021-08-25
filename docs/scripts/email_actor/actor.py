"""Send Email from Actor with User Message"""
from agavepy.actors import get_context
import smtplib
import os

# function to email the message
def email_message(m):
    """Send Email from Actor With User Message"""

    # grab the environment variables set
    useremail_from = os.environ.get('useremail_from')
    useremail_to = os.environ.get('useremail_to')
    userpassword = os.environ.get('userpassword')

    if m == " ":
        print("Empty Message!")
    else:
        sent_from = useremail_from
        to = [useremail_to]
        subject = 'Actor Email'
        message = m

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(useremail_from, userpassword)
            smtp_server.sendmail(sent_from, to, message)
            smtp_server.close()
            print("Email sent successfully!")
        except Exception as ex:
            print("Exception occured",ex)


def main():
    """Main entry to grab message context from user input"""
    context = get_context()
    message = context['raw_message']
    email_message(message)

if __name__ == '__main__':
    main()
