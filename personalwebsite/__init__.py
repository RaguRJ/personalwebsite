# personalwebsite/__init__.py
from flask import Flask

app = Flask(__name__)

# Importing python modules from different folders
from personalwebsite.core.views import core
from personalwebsite.error_pages.handlers import error_pages

# Connecting or linking various routing functions to main app
app.register_blueprint(core)
app.register_blueprint(error_pages)
