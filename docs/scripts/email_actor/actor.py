"""Send Email from Actor with User Message"""
from agavepy.actors import get_context
import smtplib

# function to email the message
def email_message(m):
    """Send Email from Actor With User Message"""
    context = get_context()
    if m == " ":
        print("Empty Message!")
    else:
        user_email = context["USER_EMAIL"]
        password = context["USER_PASSWORD"]
        sent_from = user_email
        to = ['shwetagopaul92@gmail.com']
        subject = 'Actor Email'
        message = m

        try:
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            smtp_server.ehlo()
            smtp_server.login(user_email, password)
            smtp_server.sendmail(sent_from, to, message)
            smtp_server.close()
            print("Email sent successfully!")
        except Exception as ex:
            print("Exception occured",ex)


def main():
    """Main entry to grab message context from user input"""
    context = get_context()
    message = context['raw_message']
    print(context['USER_EMAIL'])
    email_message(message)

if __name__ == '__main__':
    main()
