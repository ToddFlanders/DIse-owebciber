from flask import Flask, render_template
from flask_login import LoginManager


app = Flask(__name__)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/')
def index():
    return render_template('index.html')
