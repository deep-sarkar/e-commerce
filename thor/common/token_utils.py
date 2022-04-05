import jwt
import os

SECRET = str(os.environ.get('SECRET'))


def create_token(payload):
    token = jwt.encode(payload, SECRET, algorithm="HS256")
    return token


def decode_token(token):
    payload = jwt.decode(token, SECRET, algorithms=["HS256"])
    return payload


