from datetime import datetime

from bootstrap import db


class Feed(db.Model):
    """Represents a feed.
    """
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), default="")
    description = db.Column(db.String(), default="")
    language = db.Column(db.String(), default="")
    link = db.Column(db.String(), nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.utcnow())

    # foreign keys
    set_id = db.Column(db.Integer(), db.ForeignKey('feed_set.id'))

    def output(self, key, obj):
        return {'title': self.title}


class FeedSet(db.Model):
    """Represents a set of feeds.
    """
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), default="")
    description = db.Column(db.String(), default="")
    date_created = db.Column(db.DateTime(), default=datetime.utcnow())
    ui_position = db.Column(db.Integer(), default=0)

    # relationships
    feeds = db.relationship(Feed, backref='set', cascade='all, delete-orphan',
                            foreign_keys=[Feed.set_id])
