
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID

from bootstrap import db

class Spam(db.Model):
    """Represent a spam report.
    """
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(UUID(as_uuid=True), unique=True, nullable=False)
    number = db.Column(db.Text(), nullable=False)
    category = db.Column(db.Text(), nullable=False)
    source =  db.Column(db.Text(), nullable=False)
    created = db.Column(db.DateTime(), default=datetime.utcnow())
