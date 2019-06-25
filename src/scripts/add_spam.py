#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import uuid
from datetime import datetime

from bootstrap import application, db
from web.models import Spam


def add_spam_manual(number, category):

    new_spam = Spam(uuid=uuid.uuid4(),
                    number=number,
                    category=category,
                    source='CLI',
                    date=datetime.now())
    db.session.add(new_spam)
    db.session.commit()
