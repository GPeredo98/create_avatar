from flask import Blueprint, jsonify, request, make_response
from flask_cors.decorator import cross_origin
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from utilities import db
from users.models import User
import bcrypt

users = Blueprint('users', __name__)

@users.route('/list')
@cross_origin(origin='*')
def obtener_usuarios():
    try:
        lista_usuarios = User.query.all()
        return jsonify(
            {'data': User.Schema(many=True).dump(lista_usuarios), 'success': True, 'message': 'Usuarios obtenidos'})
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})

@users.route('/<id_user>')
#@jwt_required
def obtener_datos_usuario(id_user):
    try:
        token = get_jwt_identity()
        print(token)
        usuario = User.query.get(id_user)
        if usuario is not None:
            return jsonify({'data': User.Schema().dump(usuario), 'success': True, 'message': 'Datos del usuario'})
        else:
            return jsonify({'data': None, 'success': False, 'message': 'Usuario no encontrado'})
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})

@users.route('/registrar', methods=['POST'])
def registrar_usuario():
    try:
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        correo = request.json['correo']
        contrasenha = request.json['contrasenha'] # 'paulo1'
        contrasenha_hasheada = bcrypt.hashpw(contrasenha.encode('utf-8'), bcrypt.gensalt()) # b'$2b$12$XAxZikWeb2jlP1GwIVUh9.RFgb4.NtoUHqrd/iyG6f9TLiVQb17A.'

        nuevo_usuario = User(nombres, apellidos, correo, contrasenha_hasheada)
        token = create_access_token(identity={'id': nuevo_usuario.id, 'correo': nuevo_usuario.email})

        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify(
            {
                'data': {'usuario': User.Schema().dump(nuevo_usuario), 'token': token},
                'success': True,
                'message': 'Usuario registrado'
            })
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})

@users.route('/login', methods=['POST'])
def login_usuario():
    try:
        usuario = User.query.filter(User.email == request.json['correo']).first()
        if usuario is not None and bcrypt.checkpw(request.json['contrasenha'].encode('utf8'), usuario.password.encode('utf8')):
            token = create_access_token(identity={'id': usuario.id, 'correo': usuario.email})
            return jsonify(
                {
                    'data': {'usuario': User.Schema().dump(usuario), 'token': token},
                    'success': True,
                    'message': 'Login exitoso'
                })
        else:
            return jsonify(
                {
                    'data': "",
                    'success': False,
                    'message': 'Usuario y/o contraseña incorrecta'
                })
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})
