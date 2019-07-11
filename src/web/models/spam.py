
from datetime import datetime
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

from bootstrap import db


class Spam(db.Model):
    """Represent a spam report.
    """
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False,
                    default=uuid4)
    number = db.Column(db.Text(), nullable=True)
    number_hash = db.Column(db.Text(), nullable=True)
    category = db.Column(db.Text(), nullable=False)
    source =  db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow())

    def __str__(self):
        return """UUID: {}
Number: {}
Date: {}""".format(self.uuid, self.number, self.date)
