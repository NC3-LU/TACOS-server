#! /usr/bin/env python
# -*- coding: utf-8 -*-

from flask import jsonify
from sqlalchemy import desc
from flask_restful import (Resource, reqparse, fields, marshal)

from web.models import FeedSet, Feed

feed_fields = {
    'title': fields.String,
    'description': fields.String,
    'language': fields.String,
    'link': fields.String,
}

feed_set_fields = {
    'title': fields.String,
    'description': fields.String,
    'feeds': fields.List(fields.Nested(feed_fields)),
    'ui_position': fields.Integer,
}

def make_public_feed(feed):
    """Convert the internal representation of a feed to
    the external representation that clients expected."""
    return marshal(feed, feed_set_fields)


class FeedSetListAPI(Resource):
    #decorators = [auth.login_required]
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        for field, field_type in feed_set_fields.items():
            self.reqparse.add_argument(field, type=str, default=None)
        super(FeedSetListAPI, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()
        q = FeedSet.query.order_by(desc(FeedSet.date_created))
        for attr, value in args.items():
            if value:
                q = q.filter(getattr(FeedSet, attr).ilike("%%%s%%" % value))

        return {
            'nb_results': q.count(),
            'objects': [make_public_feed(feed) for feed in q.all()]
        }
