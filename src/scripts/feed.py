#!/usr/bin/env python
#! -*- coding: utf-8 -*-

from bootstrap import application, db
from web.models import Feed, FeedSet


def add_feed_set(title, description):
    """Add a new feed set.
    """
    new_feed_set = FeedSet(title=title, description=description)
    db.session.add(new_feed_set)
    db.session.commit()


def add_feed(title, description, link, language, set_id):
    """Add a new feed.
    """
    new_feed = Feed(title=title, description=description, link=link,
                        language=language, set_id=int(set_id))
    db.session.add(new_feed)
    db.session.commit()
