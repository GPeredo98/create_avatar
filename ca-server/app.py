  
from flask import Flask
from flask_cors import CORS
from utilities import db, ma, jwt
from avatars.views import avatars
from users.views import users


def create_app(config_file='settings.py'):
    application = Flask(__name__)
    application.config.from_pyfile(config_file)
    CORS(application)
    ma.init_app(application)
    jwt.init_app(application)
    db.init_app(application)
    with application.app_context():
        db.create_all()
    application.register_blueprint(users, url_prefix='/users')
    application.register_blueprint(avatars, url_prefix='/avatars')
    return application


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=4000)