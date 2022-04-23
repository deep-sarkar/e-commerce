from .apis import UserRegisterAPI, UserLoginAPI
from .views import UserVerifyTokenAPI

api_routes = [
    ('/api/user/register', UserRegisterAPI),
    ('/api/user/login', UserLoginAPI),

]

view_routes = [
    ('/api/verify/token', UserVerifyTokenAPI.as_view('token-verification')),
]