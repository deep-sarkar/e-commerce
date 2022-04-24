import re

from mongoengine import ValidationError


def validate_pin_code(pin):
    regex = r'^[0-9]{6}$'
    match = re.match(regex, pin)
    if not match:
        raise ValidationError('Invalid pin-code {}'.format(pin))