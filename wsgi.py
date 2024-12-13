import sys
import os

# add your project directory to the sys.path
project_home = os.path.expanduser('~/my_website')
if project_home not in sys.path:
    sys.path.append(project_home)

# import flask app but need to call it "application" for WSGI to work
from app import app as application  # noqa
