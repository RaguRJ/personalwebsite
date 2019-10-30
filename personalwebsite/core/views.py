# core/views.py

#Importing modules
from flask import render_template,request,Blueprint

#Creating an instance of the blueprint class
core = Blueprint('core',__name__)

# Creating route for the index/home page
@core.route('/')
def index(): # Function name to be specified in {{url_for('core.index')}}
    return render_template('intro.html')

# Creating route for the about website page
@core.route('/about')
def about(): 
    return render_template('about.html')