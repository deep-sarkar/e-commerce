import jwt
import os
import datetime
from flask import request

SECRET = str(os.environ.get('SECRET'))


def create_token(payload):
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(hours=6)
    payload['iat'] = datetime.datetime.utcnow()
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    return token


def decode_token(token):
    payload = jwt.decode(token, SECRET, algorithms=["HS256"])
    return payload


def token_required(func):
    def wrapper(*args, **kwargs):
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        elif 'token' in request.args:
            token = request.args['token']
        else:
            return {'error': 'token missing', 'code': 300}
        try:
            data = decode_token(token)
        except Exception as e:
            return {'error': str(e), 'code': 404}
        return func(*args, **data)
    return wrapper

