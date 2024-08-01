import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv


def send_email(subject, message):
    try:
        load_dotenv()
        sender_email = os.getenv('SENDER_EMAIL')
        receiver_email = os.getenv('RECEIVER_EMAIL')

        # Create a MIMEText object to represent the email body
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Create SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        # Start TLS for security
        s.starttls()
        # Authentication
        s.login(sender_email, os.getenv('SENDER_PASSWORD'))
        # Sending the mail
        s.sendmail(sender_email, receiver_email, msg.as_string())
        # Terminating the session
        s.quit()
        return True
    except Exception as e:
        print("Email not sent")
        print(e)
        return False


def send_scan_emails(responses):
    for data in responses:
        result, body = data
        if result:
            send_email("SCAN SUCCESSFUL", body)
        else:
            send_email("SCAN FAILED", body)
