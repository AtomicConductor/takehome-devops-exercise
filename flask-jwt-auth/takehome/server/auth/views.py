# takehome/server/auth/views.py


from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from takehome.helper import decode_auth_token

auth_blueprint = Blueprint('auth', __name__)
localhostIP = '127.0.0.1'

class HealthAPI(MethodView):
    """
    Health API
    """
    def get(self):
        ip_addr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
        if ip_addr != localhostIP:
            return make_response(), 401
        responseObject = {
            'status': 'OK',
        }
        return make_response(jsonify(responseObject)), 204

class UserAPI(MethodView):
    """
    User Resource
    """
    def get(self):
        # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            auth_token = ''
        if auth_token:
            resp = decode_auth_token(auth_token)
            if not isinstance(resp, str):
                responseObject = {
                    'status': 'success',
                    'data': {
                        'user_id': resp['user_id'],
                        'user_full_name': resp['user_full_name'],
                        'user_email': resp['user_email'],
                    }
                }
                return make_response(jsonify(responseObject)), 200
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(responseObject)), 401


user_view = UserAPI.as_view('user_api')
health_view = HealthAPI.as_view('health_api')

auth_blueprint.add_url_rule(
    '/v1/user',
    view_func=user_view,
    methods=['GET']
)

auth_blueprint.add_url_rule(
    '/healthz',
    view_func=health_view,
    methods=['GET']
)
