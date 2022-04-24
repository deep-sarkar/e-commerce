import re
from mongoengine.errors import ValidationError


def validate_mobile_number(mobile):
    regex = r'^[6-9]{1}\d{9}$'
    match = re.match(regex, mobile)
    if not match:
        raise ValidationError('Invalid mobile number {}'.format(mobile))


def validate_password(password):
    regex = r'^[A-Za-z0-9]{8,}$'
    match = re.match(regex, password)
    if not match:
        raise ValidationError('password should be alpha numerical and min 8 digit len')