from app.controllers.producto_controller import ProductoController
from app.decorators.rol_access import rol_access
from app.models import db
from flask import Blueprint
from flask_jwt_extended import jwt_required

# Ruta para registrar en el __init__.py
productos_bp = Blueprint("productos", __name__, url_prefix="/productos")

# Listar todos los Productos, autenticación necesaria.
@productos_bp.route("/", methods=["GET"])
@jwt_required()
@rol_access("admin", "operador")
def listar_productos():
    return ProductoController.listar_productos()


# Ver un producto por su ID, autenticación requerida
@productos_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
@rol_access("admin", "operador")
def ver_producto(id):
    return ProductoController.ver_producto(id)


# Crear un producto, solo admin
@productos_bp.route("/", methods=["POST"])
@jwt_required()
@rol_access("admin")
def crear_producto():
    return ProductoController.crear_producto()


# Editar un producto por su ID, solo admin
@productos_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@rol_access("admin")
def editar_producto(id):
    return ProductoController.editar_producto(id)


# Borrar un producto por su ID, solo admin
@productos_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@rol_access("admin")
def eliminar_producto(id):
    return ProductoController.eliminar_producto(id)