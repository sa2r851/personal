from flask import Flask, render_template
from dotenv import load_dotenv
import config
import os
from flask_pymongo import PyMongo

app = Flask(__name__)
APP_ROOT = os.path.join(os.path.dirname(__file__), "..")
dotenv_path = os.path.join(APP_ROOT, ".env")
load_dotenv(dotenv_path)
app.config.from_object('config.settings.' + os.environ.get('FLASK_ENV'))



from app.views.about import about as a
from app.views.blog import blog as b
from app.views.content import content as c
from app.views.projects import projects as p
from app.views.index import home as h


app.register_blueprint(h)
app.register_blueprint(a)
app.register_blueprint(p)
app.register_blueprint(b)
app.register_blueprint(c)


app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
mongo = PyMongo(app)
@app.route("/admin")
def home_page():
    online_users = mongo.db.users.find({"online": True})
    return render_template("safg",
        online_users=online_users)