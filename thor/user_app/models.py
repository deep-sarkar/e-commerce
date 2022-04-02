import datetime

from mongoengine.fields import StringField, SequenceField, EmailField, ListField, \
    ReferenceField, IntField, BooleanField, DateTimeField
from mongoengine import Document, PULL
from .validation import validate_mobile_number, validate_pin_number, validate_password


class Address(Document):
    id = SequenceField(primary_key=True)
    house_no = IntField()
    area = StringField(required=True, max_length=50)
    city = StringField(requied=True, max_length=30)
    dist = StringField(required=True, max_length=30)
    state = StringField(required=True, max_length=30)
    pin = StringField(validation=validate_pin_number)
    landmark = StringField()
    additional_data = StringField()
    dt_created = DateTimeField(default=datetime.datetime.now)
    dt_updated = DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return f'{self.city}'


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
    address = ListField(ReferenceField(Address, reverse_delete_rule=PULL))
    dt_created = DateTimeField(default=datetime.datetime.now)
    dt_updated = DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return f'{self.id} : {self.email}'
