#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import hashlib
import phonenumbers
from datetime import datetime
from pymisp import PyMISP
#from phonenumbers import geocoder

from bootstrap import application, db
from web.models import Spam

misp_url = application.config.get('MISP_URL', '')
misp_key = application.config.get('MISP_KEY', '')
misp_verifycert = True
relative_path = 'attributes/restSearch'
body = {
    #"org": "CIRCL",
    "returnFormat": "json",
    "type": "phone-number"
}

def retrieve_spam_from_misp():
    misp = PyMISP(misp_url, misp_key, misp_verifycert)
    result = misp.direct_call(relative_path, body)

    h = hashlib.sha512()

    for attribute in result['response']['Attribute']:
        if Spam.query.filter(Spam.uuid==attribute['uuid']).count():
            continue

        try:
            x = phonenumbers.parse(attribute['value'], None)
        except phonenumbers.phonenumberutil.NumberParseException as e:
            continue

        #iternational_format = phonenumbers.format_number(x,
                                    #phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        #geo = geocoder.description_for_number(x, "en")
        #print("{} - {} - {}".format(iternational_format, geo,
                                    #attribute['category']))

        h.update(attribute['value'].encode('utf-8'))

        new_spam = Spam(uuid=attribute['uuid'],
                        number_hash=h.hexdigest(),
                        category=attribute['category'],
                        source=misp_url,
                        date=datetime.fromtimestamp(int(attribute['timestamp'])))
        db.session.add(new_spam)
    db.session.commit()
