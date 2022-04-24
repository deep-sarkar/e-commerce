import datetime
import json

from mongoengine import ValidationError, DoesNotExist

from .models import Address
from flask_restful import Resource
from flask import request
from common.token_utils import token_required


class AddressAPI(Resource):
    @token_required
    def get(self, *args, **kwargs):
        user_id = kwargs['id']
        addresses = Address.objects.filter(user_id=user_id)
        address_json = []
        for address in addresses:
            address_json.append(address.to_dict())

        return {'message': 'success', 'code': 200, 'data': address_json}

    @token_required
    def post(self, *args, **kwargs):
        user_id = kwargs['id']
        data = json.loads(request.data)
        house_no = data.get('house_no')
        area = data.get('area')
        city = data.get('city')
        dist = data.get('dist')
        state = data.get('state')
        pin = data.get('pin')
        landmark = data.get('landmark')
        additional_data = data.get('additional_data')
        if not all([house_no, area, city, dist, state, pin]):
            return {'error': 'please fill mandatory fields', 'code': 300}

        address = Address(user_id=user_id,
                          house_no=house_no,
                          area=area,
                          city=city,
                          dist=dist,
                          state=state,
                          pin=pin,
                          landmark=landmark,
                          additional_data=additional_data
                          )

        try:
            address.save()
        except ValidationError as e:
            return e.to_dict()

        return {'message': 'success', 'code': 201}

    @token_required
    def put(self, *args, **kwargs):
        _id = request.args.get('id')
        if not _id:
            return {'error': 'Address id required', 'code': 301}

        try:
            address = Address.objects.get(id=_id)
            data = json.loads(request.data)
            for k,v in data.items():
                address.__setattr__(k, v)

            address.dt_updated = datetime.datetime.now
            address.save()
        except ValidationError as e:
            return e.to_dict()
        except DoesNotExist as e:
            return {'error': str(e), 'code': 300}

        return {'message': 'success', 'code': 201}

    @token_required
    def delete(self, *args, **kwargs):
        _id = request.args.get('id')
        if not _id:
            return {'error': 'Address id required', 'code': 301}

        try:
            address = Address.objects.get(id=_id)
            address.delete()
        except DoesNotExist as e:
            return {'error': str(e), 'code': 300}

        return {'message': 'success', 'code': 200}