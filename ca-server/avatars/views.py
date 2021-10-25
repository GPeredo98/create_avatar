from flask import Blueprint, jsonify, request, send_file
from utilities import db
from avatars.models import Avatar, Trait

avatars = Blueprint('avatars', __name__)


@avatars.route('/traits')
def obtener_caracteristicas():
    try:
        lista_usuarios = Trait.query.all()
        return jsonify(
            {'data': Trait.Schema(many=True).dump(lista_usuarios), 'success': True, 'message': 'Usuarios obtenidos'})
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})

@avatars.route('/traits_by_types')
def obtener_caracteristicas_por_tipo():
    try:
        pieles = Trait.query.filter(Trait.tipo == 1).all()
        rostros = Trait.query.filter(Trait.tipo == 2).all()
        atuendos = Trait.query.filter(Trait.tipo == 3).all()
        cabellos = Trait.query.filter(Trait.tipo == 4).all()
        lentes = Trait.query.filter(Trait.tipo == 5).all()

        traits = {
            "pieles": Trait.Schema(many=True).dump(pieles),
            "rostros": Trait.Schema(many=True).dump(rostros),
            "atuendos": Trait.Schema(many=True).dump(atuendos),
            "cabellos": Trait.Schema(many=True).dump(cabellos),
            "lentes": Trait.Schema(many=True).dump(lentes),
        }
        
        return jsonify(
            {'data': traits, 'success': True, 'message': 'Características obtenidas'})
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})

@avatars.route('/<image>')
def get_image(image):
    return send_file('static/images/'+image+'.png', mimetype='image/gif')

@avatars.route('/create_avatar', methods=['POST'])
def create_avatar():
    try:
        new_avatar = Avatar(
            request.json['nombre'],
            request.json['cabello'] if 'cabello' in request.json else None,
            request.json['vello_facial'] if 'vello_facial' in request.json else None,
            request.json['piel'] if 'piel' in request.json else None,
            request.json['atuendo'] if 'atuendo' in request.json else None,
            request.json['rostro'] if 'rostro' in request.json else None,
            request.json['lente'] if 'lente' in request.json else None,
            request.json['sombrero'] if 'sombrero' in request.json else None,
            request.json['fk_user']
            )

        db.session.add(new_avatar)
        db.session.commit()
        return jsonify(
            {
                'data': {'avatar': Avatar.Schema().dump(new_avatar)},
                'success': True,
                'message': 'Avatar saved'
            })
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})

@avatars.route('/edit_avatar', methods=['POST'])
def edit_avatar():
    try:
        avatar = Avatar.query.filter(Avatar.id == request.json['id']).first()
        if avatar:
            avatar.nombre = request.json['nombre'] if 'nombre' in request.json else avatar.nombre
            avatar.cabello = request.json['cabello'] if 'cabello' in request.json else avatar.cabello
            avatar.vello_facial = request.json['vello_facial'] if 'vello_facial' in request.json else avatar.vello_facial
            avatar.piel = request.json['piel'] if 'piel' in request.json else avatar.piel
            avatar.atuendo = request.json['atuendo'] if 'atuendo' in request.json else avatar.atuendo
            avatar.rostro = request.json['rostro'] if 'rostro' in request.json else avatar.rostro
            avatar.lente = request.json['lente'] if 'lente' in request.json else avatar.lente
            avatar.sombrero = request.json['sombrero'] if 'sombrero' in request.json else avatar.sombrero

        db.session.commit()
        return jsonify(
            {
                'data': {'avatar': Avatar.Schema().dump(avatar)},
                'success': True,
                'message': 'Avatar updated'
            })
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})


@avatars.route('/delete_avatar/<avatar_id>', methods=['DELETE'])
def delete_avatar(avatar_id):
    try:
        Avatar.query.filter(Avatar.id == avatar_id).delete()
        db.session.commit()
        return jsonify({
            'data': '',
            'success': True,
            'message': 'Avatar borrado'
        })
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})


@avatars.route('/all_avatars')
def all_avatars():
    try:
        list = Avatar.query.all()
        return jsonify({
            'data': Avatar.Schema(many=True).dump(list),
            'success': True,
            'message': 'Usuario registrado'
        })
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})


@avatars.route('/my_avatars/<user_id>')
def my_avatars(user_id):
    try:
        list = Avatar.query.filter(Avatar.fk_user == user_id).all()
        return jsonify({
            'data': Avatar.Schema(many=True).dump(list),
            'success': True,
            'message': 'Usuario registrado'
        })
    except Exception as e:
        return jsonify({'data': str(e), 'success': False, 'message': 'Ocurrió un error en el servidor'})
