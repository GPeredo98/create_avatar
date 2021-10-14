  
from utilities import db, add_schema
from datetime import datetime


@add_schema()
class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    status = db.Column(db.BOOLEAN, default=1)
    created_date = db.Column(db.DateTime, default=datetime.now())
    modified_date = db.Column(db.DateTime, default=datetime.now())
    image = db.Column(db.Text)

    def __init__(self, first_name, last_name, phone, email, password, status, image):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.password = password
        self.estado = status
        self.imagen = image

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def to_json(self):
        return dict(nombres=self.first_name, apellidos=self.last_name)