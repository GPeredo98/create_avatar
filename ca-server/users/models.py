  
from utilities import db, add_schema
from datetime import datetime


@add_schema()
class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    status = db.Column(db.BOOLEAN, default=1)
    created_date = db.Column(db.DateTime, default=datetime.now())
    modified_date = db.Column(db.DateTime, default=datetime.now())
    image = db.Column(db.Text, default=None)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def to_json(self):
        return dict(nombres=self.first_name, apellidos=self.last_name)

class Avatar(db.Model):
    __tablename__ = 'avatars'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(400), nullable=True)
    cabello = db.Column(db.String(400), nullable=True)
    vello_facial = db.Column(db.String(400), nullable=True)
    tono_piel = db.Column(db.String(400), nullable=True)
    atuendo = db.Column(db.String(400), nullable=True)
    rostro = db.Column(db.String(400), nullable=True)
    lentes = db.Column(db.String(400), nullable=True)
    sombrero = db.Column(db.String(400), nullable=True)

    def __init__(self, nombre, cabello, vello_facial, tono_piel, atuendo, rostro, lentes, sombrero):
        self.nombre = nombre
        self.cabello = cabello
        self.vello_facial = vello_facial
        self.tono_piel = tono_piel
        self.vello_facial = vello_facial
        self.atuendo = atuendo
        self.rostro = rostro
        self.lentes = lentes
        self.sombrero = sombrero

    def __str__(self):
        return self.id + ' ' + self.nombre

    def to_json(self):
        return dict(nombre=self.nombre, cabello=self.cabello)

    class Trait(db.Model):
        __tablename__ = 'traits'

        id = db.Column(db.Integer, primary_key=True)
        tipo = db.Column(db.Integer, nullable=False) # 1 cabello; 2 vello_facial; 3 tono_piel; 4 atuendo; 5 rostro; 6 lentes; 7 sombrero
        imagen = db.Column(db.String(500), nullable=False)
    
    def __str__(self):
        return self.id

    def to_json(self):
        return dict(id=self.id, tipo=self.tipo, imagen=self.imagen)
        

        

        

