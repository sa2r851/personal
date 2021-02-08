from flask import Blueprint, render_template , url_for
from app import app


blog = Blueprint('blog', __name__,template_folder='templates' ,static_folder='static')

@blog.route('/blog')
def article():
    title = 'Blog'
    return render_template('blog.html', title=title)

@blog.route('/blog/myblog')
def posts():
    title = 'My blog'
    return render_template('blog-post.html', title=title)