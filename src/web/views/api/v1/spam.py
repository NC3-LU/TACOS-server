#! /usr/bin/env python
# -*- coding: utf-8 -*-

import re
import hashlib
from flask import jsonify
from sqlalchemy import desc
from flask_restful import (Resource, reqparse, fields, marshal, abort)

from web.models import Spam
from bootstrap import db

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
        for field, field_type in spam_fields.items():
            self.reqparse.add_argument(field, type=str, default=None)
        super(SpamListAPI, self).__init__()

    def get(self):
        """Return the list of spam reports.
        """
        args = self.reqparse.parse_args()
        q = Spam.query.order_by(desc(Spam.date))
        for attr, value in args.items():
            if value:
                q = q.filter(getattr(Spam, attr).ilike("%%%s%%" % value))

        return {
            'nb_results': q.count(),
            'objects': [make_public_spam(spam) for spam in q.all()]
        }

    def post(self):
        """Endpoint for the creation of new spam report.
        """
        args = self.reqparse.parse_args()
        number_hash = args['number_hash']
        if not number_hash:
            # number_hash is mandatory
            abort(400)
        try:
            # check if number_hash is a SHA 512 string
            re.match(r'^\w{128}$', number_hash).group(0)
        except:
            abort(400)
        number = args['number'] if args['number'] else ''
        if number:
            # if the 'number' was submitted in clear, we check if its hashed
            # value is equal to the hashed value submitted by the client
            h = hashlib.sha512()
            h.update(number.encode('utf-8'))
            if not number == h.hexdigest():
                abort(400)
        category = args['category'] if args['category'] else 'Other'
        source = args['source'] if args['source'] else 'TACOS'

        new_spam = Spam(number = args['number'],
                    number_hash=number_hash,
                    category=category,
                    source=source)

        db.session.add(new_spam)
        db.session.commit()


class SpamAPI(Resource):
    def get(self, id):
        """Returns more details about a spam report.
        """
        spam = Spam.query.filter(Spam.id==id).first()
        if not spam:
            return abort(404, message='Spam {} does not exist.'.format(id))
        return jsonify({'spam': make_public_spam(spam)})
