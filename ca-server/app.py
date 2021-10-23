  
from flask import Flask
from flask_cors import CORS
from utilities import db, ma, jwt
# from productos.views import productos
from users.views import users


def create_app(config_file='settings.py'):
    application = Flask(__name__)
    application.config.from_pyfile(config_file)
    application.register_blueprint(users, url_prefix='/users')


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=4000)