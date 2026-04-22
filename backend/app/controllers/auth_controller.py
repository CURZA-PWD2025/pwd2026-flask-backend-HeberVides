from app.models.user import User
from app.models.rol import Rol
from app.models import db
from flask import request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError


class AuthController:

    # MODIFIQUE EL METODO "register" ya que no enviaba el mensaje que deberia, cuando el ususario ya estaba registrado
    # Registra un nuevo usuario ("operador")
    @staticmethod
    def register():
        data = request.get_json()

        rol = Rol.query.filter_by(nombre="operador").first()
        if not rol:
            return jsonify({"error": "El Rol operador no existe"}), 500

        if User.query.filter_by(email=data["email"]).first():
            return jsonify({"error": "El Usuario ya esta registrado"}), 409

        user = User(
            nombre=data["nombre"],
            email=data["email"],
            password=generate_password_hash(data["password"]),
            rol_id=rol.id
        )

        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return jsonify({"error": "Usuario ya se encuentra registrado"}), 409

        return jsonify({"msg": "Se creo el Usuario creado con el rol operador"}), 201
    
        #LOS USUARIOS QUE SE REGISTREN SOLO DEBERIAN PODER SER "operadores" POR SEGURIDAD.


    # Inicia la sesion con las credenciales ("email" y "password") sea de rol ("admin" o "operador")
    @staticmethod
    def login():
        data = request.get_json()
        user = User.query.filter_by(email=data["email"]).first()
        if not user or not user.validate_password(data["password"]):
            return jsonify({"error": "Credenciales inválidas"}), 401

        access_token = create_access_token(
            identity=str (user.id),
            additional_claims={"rol": user.rol.nombre}
        )
        return jsonify(access_token=access_token), 200
    
    # Devuelve el token que se va a usar para validar el uso de CRUD en los modelos de las tablas.

    @staticmethod
    @jwt_required()
    def me():
        user_id = get_jwt_identity()
        user = User.query.get(int(user_id))
        return jsonify(user.to_dict()), 200
