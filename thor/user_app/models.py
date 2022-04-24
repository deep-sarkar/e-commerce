import datetime

from mongoengine.fields import StringField, SequenceField, EmailField, ListField, \
    ReferenceField, BooleanField, DateTimeField
from mongoengine import Document, PULL
from .validation import validate_mobile_number, validate_password


class User(Document):
    id = SequenceField(primary_key=True)
    first_name = StringField(null=False)
    last_name = StringField(null=False)
    mobile = StringField(required=True, validation=validate_mobile_number)
    email = EmailField(required=True)
    password = StringField(required=True, validation=validate_password)
    gender = StringField(default='male', choices=['male', 'female'])
    is_active = BooleanField(default=False)
    admin = BooleanField(default=False)
    dt_created = DateTimeField(default=datetime.datetime.now)
    dt_updated = DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return f'{self.id} : {self.email}'
