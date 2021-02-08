from flask import Blueprint, render_template ,url_for
from app import app

projects = Blueprint('projects', __name__,template_folder='templates' ,static_folder='static')

@projects.route('/projects')
def project():
    title = 'Pojects'
    return render_template('projects.html', title=title)