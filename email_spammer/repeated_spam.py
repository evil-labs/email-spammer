import getpass
import os
import random
import smtplib
import time

from email.Header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# Frequency of spamming in seconds
SPAM_INTERVAL = 5

# change to your email
MY_EMAIL = 'some_email@some_domain'

# edit for your password in the file
p_reader = open('password.txt', 'rb')
cipher = p_reader.read()

if not cipher:
    cipher = getpass.getpass("Please provide your email password")

# enter recipients here
RECEPIENT_EMAILS = ['recipient_email_1', 'recipient_email_2']

# Email message, enter the message in message.txt file
fp = open('message.txt', 'rb')


count = 1


def spam_repeatedly():
    # some variable text for the subject of email
    variable_text = ['mc', 'bc', 'blah']

    # to use image, save the image in the same director
    # and uncomment the below line
    # img_data = open('index.jpeg', 'rb').read()

    while (True):
        global count

        msg = MIMEMultipart()
        msg.attach(MIMEText(
            fp.read() + "\n Attempt: " + str(count), 'plain', 'utf-8'))

        fp.close()

        msg['Subject'] = Header('Happy birthday {}'.format(
            random.choice(variable_text)), 'utf-8')
        msg['From'] = MY_EMAIL
        msg['To'] = ', '.join(RECEPIENT_EMAILS)

        # Uncomment the following statements for image
        # image = MIMEImage(img_data,
        #                   name=os.path.basename('index.jpeg'))
        # msg.attach(image)

        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(MY_EMAIL, cipher)
        s.sendmail(MY_EMAIL, RECEPIENT_EMAILS, msg.as_string())

        print("Email sent to: " + ', '.join(RECEPIENT_EMAILS))
        count += 1
        s.quit()

        time.sleep(SPAM_INTERVAL)


if __name__ == "__main__":
    spam_repeatedly()
