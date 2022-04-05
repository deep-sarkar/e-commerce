import json

from flask_restful import Resource
from flask import request, render_template
from flask.views import View
from mongoengine import Q

from mongoengine.errors import ValidationError

from .models import User, Address
from .utils import send_account_activation_mail


class UserRegisterAPI(Resource):

    def post(self):
        req_data = json.loads(request.data)
        first_name = req_data.get('first_name')
        last_name = req_data.get('last_name')
        mobile = req_data.get('mobile')
        email = req_data.get('email')
        gender = req_data.get('gender')
        password = req_data.get('password')
        conf_password = req_data.get('conf_password')

        if not all([first_name, last_name, mobile, email, password, conf_password]):
            return {'error': 'All fields are mandatory', 'code': 300}

        if password != conf_password:
            return {'error': 'password not matching', 'code': 301}

        user = User.objects(Q(email=email) | Q(mobile=mobile)).first()

        if user:
            return {'error': 'email/mobile no already in use', 'code': 302}

        try:
            user = User(first_name=first_name,
                        last_name=last_name,
                        mobile=mobile,
                        email=email,
                        gender=gender,
                        password=password)
            user.save()

            send_account_activation_mail(user)
        except ValidationError as e:
            return {'error': e.to_dict(), 'code': 300}
        except Exception as e:
            return {'error': str(e), 'code': 300}
        return {'message': 'success', 'code': 200}

