import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import serverless_wsgi
from app import app as flask_app

def handler(event, context):
    return serverless_wsgi.handle_request(flask_app, event, context)
