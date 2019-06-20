from flask import Blueprint
from flask_restful import Api

from bootstrap import application

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

from web.views.api.v1.spam import SpamListAPI, SpamAPI

api.add_resource(SpamListAPI, '/api/v1/spams', endpoint='spams')
api.add_resource(SpamAPI, '/api/v1/spams/<int:id>', endpoint = 'spam')
