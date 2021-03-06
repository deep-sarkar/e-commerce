import os

from common.email_services import send_email
from common.token_utils import create_token


DOMAIN = os.environ.get('DOMAIN')


def send_account_activation_mail(user):
    first_name = user.first_name
    email = user.email

    payload = {
        'id': user.id,
        'first_name': first_name,
        'email': email
    }

    token = create_token(payload)
    activation_url = f'{DOMAIN}/api/verify/token?token={token}'
    subject = 'Account activation mail'

    email_data = {
        'subject': subject,
        'template': 'users/base.html',
        'data': {
            'first_name': first_name,
            'activation_url': activation_url,
            'email_body': 'Welcome to <b>Asgard</b>. Be a part of asgard family and enjoy unlimited shopping. '
                          'Activate your account by clicking the Enter Asgard button.'
        }
    }
    send_email(email, **{'email_data': email_data})


def send_forgot_password_mail(user):
    first_name = user.first_name
    email = user.email

    payload = {
        'id': user.id,
        'first_name': first_name,
        'email': email
    }

    token = create_token(payload)
    reset_password_url = f'{DOMAIN}/api/user/reset/password?token={token}'
    subject = 'Forgot password mail'
    email_data = {
        'subject': subject,
        'template': 'users/base.html',
        'data': {
            'first_name': first_name,
            'activation_url': reset_password_url,
            'email_body': 'Welcome to <b>Asgard</b>. To reset password please click Enter Asgard button.'
        }
    }

    send_email(email, **{'email_data': email_data})
