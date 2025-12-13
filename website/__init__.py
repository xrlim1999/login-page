from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

""" create database """
db = SQLAlchemy()
db_name = "registered_users"

""" create app """
def create_app():

    ## initialise app
    app = Flask(__name__)
    # set a SECRET KEY
    app.config["SECRET_KEY"] = "choose_your_own_secret_key"
    # choose a database type and name
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{db_name}'

    # initialise database for this app
    db.init_app(app)

    ## set app routes
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    ## import data models
    from .models import User

    # create database
    with app.app_context():
        db.create_all()

    # login manager?????
    login_manager = LoginManager()
    login_manager.login_view = "views.home" # redirect users to "views.home" if they try to interact
                                            # with a page that has @login_requiredx
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # <func> .get : looks for the primary_key by default

    return app

