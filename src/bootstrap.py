#! /usr/bin/env python
# -*- coding: utf-8 -

# required imports and code exection for basic functionning

import os
import logging
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from werkzeug.routing import BaseConverter, ValidationError
from flask_babel import Babel


def set_logging(log_path=None, log_level=logging.INFO, modules=(),
                log_format='%(asctime)s %(levelname)s %(message)s'):
    if not modules:
        modules = ('workers.fetch_cve', 'bootstrap', 'runserver', 'web',)
    if log_path:
        if not os.path.exists(os.path.dirname(log_path)):
            os.makedirs(os.path.dirname(log_path))
        if not os.path.exists(log_path):
            open(log_path, 'w').close()
        handler = logging.FileHandler(log_path)
    else:
        handler = logging.StreamHandler()
    formater = logging.Formatter(log_format)
    handler.setFormatter(formater)
    for logger_name in modules:
        logger = logging.getLogger(logger_name)
        logger.addHandler(handler)
        for handler in logger.handlers:
            handler.setLevel(log_level)
        logger.setLevel(log_level)

# Create Flask application
application = Flask('web', instance_relative_config=True)
if os.environ.get('DATABASE_URL'):
    application.config.from_pyfile('heroku.cfg', silent=False)
else:
    try:
        application.config.from_pyfile('production.cfg', silent=False)
    except:
        application.config.from_pyfile('development.cfg', silent=False)
db = SQLAlchemy(application)

babel = Babel(application)

# set_logging(application.config['LOG_PATH'])


def populate_g():
    from flask import g
    g.db = db
    g.app = application
