import datetime
from mongoengine import Document
from mongoengine.fields import StringField, SequenceField, DateTimeField, IntField
from .validation import validate_pin_code


class Address(Document):
    id = SequenceField(primary_key=True)
    user_id = IntField(required=True)
    house_no = IntField(max_value=9999)
    area = StringField(required=True, max_length=50)
    city = StringField(requied=True, max_length=30)
    dist = StringField(required=True, max_length=30)
    state = StringField(required=True, max_length=30)
    pin = StringField(validation=validate_pin_code)
    landmark = StringField(max_length=100)
    additional_data = StringField(max_length=100)
    dt_created = DateTimeField(default=datetime.datetime.now)
    dt_updated = DateTimeField(default=datetime.datetime.now)

    def __repr__(self):
        return f'{self.id} : {self.city}'

    def to_dict(self):
        address = dict()
        address['id'] = self.id
        address['user_id'] = self.user_id
        address['house_no'] = self.house_no
        address['area'] = self.area
        address['city'] = self.city
        address['dist'] = self.dist
        address['state'] = self.state
        address['pin'] = self.pin
        address['landmark'] = self.landmark
        address['additional_data'] = self.additional_data
        address['dt_created'] = str(self.dt_created)
        address['dt_updated'] = str(self.dt_updated)
        return address
