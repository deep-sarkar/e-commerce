from flask import request, render_template
from flask.views import View

from common.token_utils import decode_token
from user_app.models import User


class UserVerifyTokenAPI(View):

    def dispatch_request(self):
        data = {'first_name': '', 'error': 'token not found in url', 'status_code': 300}
        _template = 'users/account_activate.html'
        token = request.args.get('token')
        if not token:
            render_template(_template, data=data)

        payload = decode_token(token)
        user_id = payload.get('id')
        user = User.objects.get(id=int(user_id))
        if not user:
            data['error'] = 'user not found'
            return render_template(_template, data=data)

        user.is_active = True
        user.save()
        data['first_name'] = user.first_name
        data['status_code'] = 200
        return render_template(_template, data=data)
