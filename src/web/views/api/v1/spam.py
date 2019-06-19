#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse, fields, marshal

spams = [
    {
        'id': 1,
        'type': 'phone',
        'number': '+352',
        'timestamp': '11111'
    }
]

spam_fields = {
    'type': fields.String,
    'number': fields.String,
    'timestamp': fields.Boolean
}

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
        return {
            'nb_results': len(spams),
            'objects': [marshal(spam, spam_fields) for spam in spams]
        }
