from common.email_services import send_email


def send_account_activation_mail(user, token):
    first_name = user.first_name
    email = user.email
    activation_url = f'http://127.0.0.1:5000/api/verify/token?token={token}'
    subject = 'Account activation mail'
    email_data = {
        'subject': subject,
        'template': 'base.html',
        'data': {
            'first_name': first_name,
            'activation_url': activation_url
        }
    }

    send_email(email, **{'email_data': email_data})
