from .apis import UserRegisterAPI, UserLoginAPI, ForgetPasswordAPI
from .views import UserVerifyTokenAPI

api_routes = [
    ('/api/user/register', UserRegisterAPI),
    ('/api/user/login', UserLoginAPI),
    ('/api/forgot/password', ForgetPasswordAPI),

]

view_routes = [
    ('/api/verify/token', UserVerifyTokenAPI.as_view('token-verification')),
]