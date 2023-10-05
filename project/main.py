from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.errorhandler(401)
def custom_401(error):
    return redirect(url_for("auth.login", next=request.url))

# from project import db, create_app, models
# app = create_app()
# app.app_context().push()
# db.create_all()
# flask --app project run --debug