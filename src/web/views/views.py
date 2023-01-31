import os
import sys
import logging
from flask import (render_template, url_for, redirect, current_app, flash,
                  send_from_directory, request)

from bootstrap import application

logger = logging.getLogger(__name__)


@current_app.errorhandler(401)
def authentication_required(error):
    flash(gettext('Authentication required.'), 'info')
    return redirect(url_for('login'))


@current_app.errorhandler(403)
def authentication_failed(error):
    flash(gettext('Forbidden.'), 'danger')
    return redirect(url_for('login'))


@current_app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


@current_app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html'), 500


@current_app.errorhandler(503)
def internal_server_error(error):
    return render_template('errors/503.html'), 503


@current_app.errorhandler(AssertionError)
def handle_sqlalchemy_assertion_error(error):
    return error.args[0], 400


@current_app.route('/', methods=['GET'])
def index():
    """index page."""
    return render_template('index.html')


@current_app.route('/documentation', methods=['GET'])
def documentation():
    """Documentation page."""
    return redirect('https://github.com/NC3-LU/TACOS-server/tree/master/docs', code=308)


@current_app.route('/privacy', methods=['GET'])
def privacy():
    """Terms page."""
    return render_template('privacy.html')


@current_app.route('/human.txt', methods=['GET'])
def human():
    """Human dot txt page."""
    return render_template('human.txt'), 200, {'Content-Type': 'text/plain'}
