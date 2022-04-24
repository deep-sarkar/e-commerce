from .apis import UserRegisterAPI, UserLoginAPI, ForgetPasswordAPI, ResetPassword
from .views import UserVerifyTokenAPI

api_routes = [
    ('/api/user/register', UserRegisterAPI),
    ('/api/user/login', UserLoginAPI),
    ('/api/user/forgot/password', ForgetPasswordAPI),
    ('/api/user/reset/password', ResetPassword)

]

view_routes = [
    ('/api/verify/token', UserVerifyTokenAPI.as_view('token-verification')),
]