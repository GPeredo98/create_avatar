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

@users.route('/registrar', methods=['POST', 'OPTIONS'])
def registrar_usuario():
    try:
        if request.method == "OPTIONS": # CORS preflight
            return _build_cors_preflight_response()
        nombres = request.json['nombres']
        apellidos = request.json['apellidos']
        telefono = request.json['telefono']
        correo = request.json['correo']
        estado = request.json['estado']
        imagen = request.json['imagen']

        contrasenha = request.json['contrasenha']
        contrasenha_hasheada = bcrypt.hashpw(contrasenha.encode('utf-8'), bcrypt.gensalt())

        nuevo_usuario = User(nombres, apellidos, telefono, correo, contrasenha_hasheada, estado, imagen)
        token = create_access_token(identity={'id': nuevo_usuario.id, 'correo': nuevo_usuario.correo})

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

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response