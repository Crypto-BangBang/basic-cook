import sys
import os

func_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(func_dir, 'packages'))
sys.path.insert(0, func_dir)

import serverless_wsgi
from app import app as flask_app

def handler(event, context):
    return serverless_wsgi.handle_request(flask_app, event, context)
