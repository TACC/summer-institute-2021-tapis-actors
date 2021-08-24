"""Send Email from Actor with User Message"""
from agavepy.actors import get_context
import smtplib

# function to email the message
def email_message(m, user_email, user_password):
    """Send Email from Actor With User Message"""

    context = get_context()

    if m == " ":
        print("Empty Message!")
    else:
        sent_from = user_email
        to = ['shwetagopaul92@gmail.com']
        subject = 'Actor Email'
        message = m

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(user_email, user_password)
            smtp_server.sendmail(sent_from, to, message)
            smtp_server.close()
            print("Email sent successfully!")
        except Exception as ex:
            print("Exception occured",ex)


def main():
    """Main entry to grab message context from user input"""
    context = get_context()
    message = context['raw_message']
    user_email = context['USER_EMAIL']
    user_password = context['USER_PASSWORD']
    email_message(message, user_email, user_password)

if __name__ == '__main__':
    main()
