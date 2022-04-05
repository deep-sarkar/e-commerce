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
        'template': 'users/registration.html',
        'data': {
            'first_name': first_name,
            'activation_url': activation_url
        }
    }

    send_email(email, **{'email_data': email_data})
