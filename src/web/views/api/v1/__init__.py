from flask import Blueprint
from flask_restful import Api

from bootstrap import application

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

from web.views.api.v1.spam import SpamListAPI, SpamAPI
from web.views.api.v1.feed_set import FeedSetListAPI

api.add_resource(SpamListAPI, '/api/v1/spams', endpoint='spams')
api.add_resource(SpamAPI, '/api/v1/spams/<int:id>', endpoint = 'spam')

api.add_resource(FeedSetListAPI, '/api/v1/feeds_sets', endpoint='feeds_sets')
