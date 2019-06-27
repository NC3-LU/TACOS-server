#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from sqlalchemy import desc
from flask_restful import (Resource, reqparse, fields, marshal, abort)

from web.models import Spam

spam_fields = {
    'uuid': fields.String,
    'number': fields.String,
    'number_hash': fields.String,
    'category': fields.String,
    'source': fields.String,
    'date': fields.DateTime
}

spam_fields_light = {
    'number_hash': fields.String,
    'category': fields.String,
    'date': fields.DateTime
}

def make_public_spam(spam):
    """Convert the internal representation of a spam to
    the external representation that clients expected."""
    return marshal(spam, spam_fields_light)


class SpamListAPI(Resource):
    #decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for field, field_type in spam_fields_light.items():
            self.reqparse.add_argument(field, type=str, default=None)
        super(SpamListAPI, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()
        q = Spam.query.order_by(desc(Spam.date))
        for attr, value in args.items():
            if value:
                q = q.filter(getattr(Spam, attr).ilike("%%%s%%" % value))

        return {
            'nb_results': q.count(),
            'objects': [make_public_spam(spam) for spam in q.all()]
        }


class SpamAPI(Resource):
    def get(self, id):
        spam = Spam.query.filter(Spam.id==id).first()
        if not spam:
            return abort(404, message='Spam {} does not exist.'.format(id))
        return jsonify({'spam': make_public_spam(spam)})
