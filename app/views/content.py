from flask import Blueprint, render_template ,url_for
from app import app

content = Blueprint('content', __name__,template_folder='templates' ,static_folder='static')

@content.route('/contact')
def emails():
    title = 'Content'
    return render_template('content.html', title=title)