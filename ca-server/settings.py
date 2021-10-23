import os

# JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_SECRET_KEY = 'super_secret'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost:3306/create_avatar_db'
CORS_HEADERS = 'Content-Type'
# CORS_HEADERS = 'application/json'