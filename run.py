import os
from eve import Eve

SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')
app = Eve(settings=SETTINGS_PATH)
