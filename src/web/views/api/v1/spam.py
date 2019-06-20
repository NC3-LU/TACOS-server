#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from flask_restful import (Resource, reqparse, fields, marshal, abort)

from web.models import Spam

spam_fields = {
    'number': fields.String,
    'category': fields.String,
    'source': fields.String,
    'created': fields.DateTime
}

def make_public_spam(spam):
    """Convert the internal representation of a spam to
    the external representation that clients expected."""
    return marshal(spam, spam_fields)


class SpamListAPI(Resource):
    #decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('type', type=str, required=True,
                                   help='No spam type provided',
                                   location='json')
        self.reqparse.add_argument('number', type=str, default="",
                                   location='json')
        super(SpamListAPI, self).__init__()

    def get(self):
        spams = Spam.query
        return {
            'nb_results': spams.count(),
            'objects': [marshal(spam, spam_fields)
                            for spam in spams.all()]
        }


class SpamAPI(Resource):
    def get(self, id):
        spam = Spam.query.filter(Spam.id==id).first()
        if not spam:
            return abort(404, message='Spam {} does not exist.'.format(id))
        return jsonify({'spam': make_public_spam(spam)})
