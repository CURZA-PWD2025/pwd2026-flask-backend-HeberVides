from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.auth_controller import AuthController

# Ruta para registrar en el __init__.py
auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


# Registra al usuario.
@auth_bp.route("/register", methods=["POST"])
def register():
    return AuthController.register()

# Login del usuario
@auth_bp.route("/login", methods=["POST"])
def login():
    return AuthController.login()

# Solo agregue el metodo para mostrar el perfil
# Muestra el perfil del usuario autenticado
@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    return AuthController.me()
