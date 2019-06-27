#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import hashlib
import uuid
from datetime import datetime

from bootstrap import application, db
from web.models import Spam


def add_spam_manual(number, category):
    """Add a new number as a spam in the database.
    """
    h = hashlib.sha512()
    h.update(number.encode('utf-8'))
    new_uuid = uuid.uuid4()
    if not Spam.query.filter(Spam.uuid==new_uuid).count():
        new_spam = Spam(uuid=new_uuid,
                        number_hash=h.hexdigest(),
                        category=category,
                        source='CLI',
                        date=datetime.now())
        db.session.add(new_spam)
        db.session.commit()
