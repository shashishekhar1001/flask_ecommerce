from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'dev'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///E:/Flask_Auth_Blueprint/SRC/project/db.sqlite'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #blueprint for admin part of app
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    #blueprint for api part of app
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app

# To Run use:-
# flask --app project run --debug

# To create DB
# >>> from project import db, create_app, models
# >>> app = create_app()
# >>> app.app_context().push()
# >>> db.create_all()
