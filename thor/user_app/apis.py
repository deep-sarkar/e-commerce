import json

from flask_restful import Resource
from flask import request, render_template
from flask.views import View
from mongoengine import Q

from mongoengine.errors import ValidationError

from common.token_utils import create_token, token_required
from .models import User
from .utils import send_account_activation_mail, send_forgot_password_mail


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


class UserLoginAPI(Resource):
    def get(self):
        email = request.args.get('email')
        password = request.args.get('password')

        if not email or not password:
            return {'error': 'both email and password required', 'code': 300}

        user = User.objects.get(email=email)
        if not user:
            return {'error': 'User with mail does not exists.', 'code': 300}

        if user.password != password:
            return {'error': 'Password Did not matched.', 'code': 300}
        if not user.is_active:
            return {'error': 'Please activate your account first.', 'code': 300}
        first_name = user.first_name
        email = user.email

        payload = {
            'id': user.id,
            'first_name': first_name,
            'email': email
        }

        token = create_token(payload)

        return {'message': 'success', 'token': token, 'code': 200}


class ForgetPasswordAPI(Resource):
    def get(self):
        email = request.args.get('email')

        if not email :
            return {'error': 'Please enter email address.', 'code': 300}

        user = User.objects.get(email=email)
        if not user:
            return {'error': 'User with mail does not exists.', 'code': 300}

        if not user.is_active:
            return {'error': 'Please activate your account first.', 'code': 300}

        send_forgot_password_mail(user)
        return {'message': 'success', 'code': 200}


class ResetPassword(Resource):
    @token_required
    def get(self, *args, **kwargs):
        user_id = kwargs['id']
        user = User.objects.get(id=user_id)
        if not user:
            return {'error': 'user does not exists', 'code': 404}
        password = request.args.get('password')
        cnf_password = request.args.get('cnf_password')
        if not all([password, cnf_password]):
            return {'error': 'password and confirm password missing', 'code': 300}

        if password != cnf_password:
            return {'error': 'password did not matched', 'code': 300}

        try:
            user.password = password
            user.save()
        except ValidationError as e:
            return e.to_dict()
        return {'message': 'success', 'code': 200}
