#!/usr/bin/env python
#! -*- coding: utf-8 -*-

import phonenumbers
from phonenumbers import geocoder
from pymisp import PyMISP

from bootstrap import application, db
from web.models import Report

misp_url = application.config.get('MISP_URL', '')
misp_key = application.config.get('MISP_KEY', '')
misp_verifycert = True
relative_path = 'attributes/restSearch'
body = {
    "type": "phone-number"
}

misp = PyMISP(misp_url, misp_key, misp_verifycert)
result = misp.direct_call(relative_path, body)

def retrieve_spam_from_misp():
    for attribute in result['response']['Attribute']:
        try:
            x = phonenumbers.parse(attribute['value'], None)
        except phonenumbers.phonenumberutil.NumberParseException as e:
            continue

        iternational_format = phonenumbers.format_number(x,
                                    phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        geo = geocoder.description_for_number(x, "en")

        print("{} - {} - {}".format(iternational_format, geo,
                                    attribute['category']))

        new_report = Report(number=attribute['value'],
                            type=attribute['category'])
        db.session.add(new_report)
    db.session.commit()
