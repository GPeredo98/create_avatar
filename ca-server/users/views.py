from flask import Blueprint, jsonify, request, make_response
import flask
from flask_cors.decorator import cross_origin
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from utilities import db
from users.models import User
import bcrypt

users = Blueprint('users', __name__)

@users.route('/list')
def obtener_usuarios():
    try:
        lista_usuarios = User.query.all()
        return jsonify(
            {'data': User.Schema(many=True).dump(lista_usuarios), 'success': True, 'message': 'Usuarios obtenidos'})
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})

@users.route('/<id_user>')
@jwt_required
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
@cross_origin()
def registrar_usuario():
    response = flask.jsonify({'some': 'data'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response