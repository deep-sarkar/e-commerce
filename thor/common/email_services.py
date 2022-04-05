import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from jinja2 import FileSystemLoader, Environment

SMTP_SERVER = os.environ.get('SMTP_SERVER')
SMTP_PORT = os.environ.get('SMTP_PORT')
SMTP_EMAIL = os.environ.get('SMTP_EMAIL')
SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')


def render_template(template, **kwargs):
    try:
        path = '../templates/'
        template_loader = FileSystemLoader(searchpath=path)
        template_env = Environment(loader=template_loader)
        templ = template_env.get_template(template)
        return templ.render(**kwargs)
    except Exception as e:
        print(e)


def send_email(email, **kwargs):
    try:
        # Create your SMTP session
        smtp = smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT))

        # Use TLS to add security
        smtp.starttls()

        # User Authentication
        smtp.login(SMTP_EMAIL, SMTP_PASSWORD)

        # Defining The Message
        email_data = kwargs.get('email_data')
        template = email_data.get('template')

        msg = MIMEMultipart('alternative')
        msg['From'] = SMTP_EMAIL
        msg['Subject'] = email_data['subject']
        msg['To'] = email

        if template:
            data = email_data.get('data', {})
            temp = render_template(template, **data)
            temp_data = MIMEText(temp, 'html')
            msg.attach(temp_data)
        else:
            message = email_data.get('message')
            text = MIMEText(message, 'plain')
            msg.attach(text)

        # Sending the Email
        smtp.sendmail(SMTP_EMAIL, email, msg.as_string())

        # Terminating the session
        smtp.quit()
        print("Email sent successfully!")

    except Exception as ex:
        print("Something went wrong....", ex)
