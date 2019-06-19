
from datetime import datetime

from bootstrap import db

class Report(db.Model):
    """Represent a spam report.
    """
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Text(), nullable=False)
    type = db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime(), default=datetime.utcnow())
