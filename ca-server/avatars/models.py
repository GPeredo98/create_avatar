  
from users.models import User
from utilities import db, add_schema
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql import func


@add_schema()
class Avatar(db.Model):
    __tablename__ = 'avatars'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(400), nullable=True)
    cabello = db.Column(db.String(400), nullable=True)
    vello_facial = db.Column(db.String(400), nullable=True)
    piel = db.Column(db.String(400), nullable=True)
    atuendo = db.Column(db.String(400), nullable=True)
    rostro = db.Column(db.String(400), nullable=True)
    lente = db.Column(db.String(400), nullable=True)
    sombrero = db.Column(db.String(400), nullable=True)
    fk_user = db.Column(db.Integer, ForeignKey('users.id'))
    #created_at = db.Column(db.DateTime, default=func.now())

    def __init__(self, nombre, cabello, vello_facial, piel, atuendo, rostro, lente, sombrero, fk_user):
        self.nombre = nombre
        self.cabello = cabello
        self.vello_facial = vello_facial
        self.piel = piel
        self.vello_facial = vello_facial
        self.atuendo = atuendo
        self.rostro = rostro
        self.lente = lente
        self.sombrero = sombrero
        self.fk_user = fk_user

    def __str__(self):
        return self.id + ' ' + self.nombre

    def to_json(self):
        return dict(nombre=self.nombre, cabello=self.cabello)

    def get_owner(self):
        user = User.query.get(self.fk_user)
        return user

@add_schema()
class Trait(db.Model):
    __tablename__ = 'traits'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.Integer, nullable=False) # 1 cabello; 2 vello_facial; 3 tono_piel; 4 atuendo; 5 rostro; 6 lentes; 7 sombrero
    imagen = db.Column(db.String(500), nullable=False)
    
    def __str__(self):
        return self.id

    def to_json(self):
        return dict(id=self.id, tipo=self.tipo, imagen=self.imagen)
        