import sys
import os

# add your project directory to the sys.path
project_home = '/home/Vitaly72/my_website'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from app import app as application  # noqa
