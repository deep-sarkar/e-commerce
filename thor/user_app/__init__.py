from .apis import UserRegisterAPI
from .views import UserVerifyTokenAPI

api_routes = [
    ('/api/user/register', UserRegisterAPI),
]

view_routes = [
    ('/api/verify/token', UserVerifyTokenAPI.as_view('token-verification')),
]