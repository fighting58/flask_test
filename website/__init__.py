from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from datetime import timedelta

db = SQLAlchemy()
DB_NAME = "database.db"
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
UPLOAD_FOLDER = "C:/Users/USER/PycharmProjects/Flask-Web-App-Tutorial/Website/static/upload-images"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Genius_is_1_inspiration_and_99_perspiration'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
     
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    
    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
