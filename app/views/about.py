from flask import Blueprint, render_template , url_for
from app import app

about = Blueprint('about', __name__,template_folder='templates' ,static_folder='static')

@about.route('/about')
def skills():
    title = 'About'
    return render_template('about.html', title=title)