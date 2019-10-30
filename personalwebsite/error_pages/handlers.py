# personalwebsite>error_pages>handlers.py

from flask import Blueprint, render_template

error_pages = Blueprint('error_pages',__name__)

@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html'), 404 #Returning a tuple with the render template function and an integer 404

# Add more error functions as needed