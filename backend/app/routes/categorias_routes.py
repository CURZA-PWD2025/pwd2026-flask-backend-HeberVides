from app.models.categoria import Categoria
from app.controllers.categoria_controller import CategoriaController
from flask import Blueprint
from app.models import db
from flask_jwt_extended import jwt_required
from app.decorators.rol_access import rol_access

# Ruta para registrar en el __init__.py
categorias_bp = Blueprint("categorias", __name__, url_prefix="/categorias")

# Se listan las categorías, se necesita estar autenticado.
@categorias_bp.route("/", methods=["GET"])
@jwt_required()
@rol_access("admin", "operador")
def listar_categorias():
    return CategoriaController.listar_categorias()


# Ver las categorías, hay que estar autenticado.
@categorias_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
@rol_access("admin", "operador")
def ver_categoria(id):
    return CategoriaController.ver_categoria(id)


# Crear categoría, si o si hay que ser admin.
@categorias_bp.route("/", methods=["POST"])
@jwt_required()
@rol_access("admin")
def crear_categoria():
    return CategoriaController.crear_categoria()



# Editar categoría , imperativo ser admin.
@categorias_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@rol_access("admin")
def editar_categoria(id):
    return CategoriaController.editar_categoria(id)


# Borrar categoría, only admin.
@categorias_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@rol_access("admin")
def eliminar_categoria(id):
    return CategoriaController.eliminar_categoria(id)
