from flask import Blueprint, render_template ,url_for
from app import app

home = Blueprint('home', __name__ ,template_folder='templates' ,static_folder='static')

@home.route('/')
def home_page():
    title = 'AlgoSocial'
    return render_template('index.html', title=title)
