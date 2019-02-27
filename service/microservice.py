"""Main application module"""
import os
import json
import jsend
import sentry_sdk
import falcon
from .resources.welcome import Welcome
from .resources.permit_list import PermitList

def start_service():
    """Start this service
    set SENTRY_DSN environmental variable to enable logging with Sentry
    """
    # Initialize Sentry
    sentry_dsn = os.environ.get('SENTRY_DSN')
    if(os.environ.get('environment').lower() == 'production'
       and os.environ.get('SENTRY_DSN_PRODUCTION')):
        sentry_dsn = os.environ.get('SENTRY_DSN_PRODUCTION')
    sentry_sdk.init(
        sentry_dsn,
        environment=os.environ.get('environment')
    )
    # Initialize PermitList
    permit_list_obj = PermitList()
    permit_list_obj.init_screendoor(
        os.environ['SD_KEY'], '0', os.environ['SD_HOST'], os.environ['SD_PROJECT']
    )

    # Initialize Falcon
    api = falcon.API()
    api.add_route('/welcome', Welcome())
    api.add_route('/list/{permit_type}', permit_list_obj)
    api.add_sink(default_error, '')
    return api

def default_error(_req, resp):
    """Handle default error"""
    resp.status = falcon.HTTP_404
    msg_error = jsend.error('404 - Not Found')

    sentry_sdk.capture_message(msg_error)
    resp.body = json.dumps(msg_error)
