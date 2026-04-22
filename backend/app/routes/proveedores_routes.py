from app.controllers.proveedor_controller import ProveedorController
from flask import Blueprint, request, jsonify
from app.models import db
from app.models.proveedor import Proveedor
from flask_jwt_extended import jwt_required
from app.decorators.rol_access import rol_access

# Ruta para registrar en el __init__.py
proveedores_bp = Blueprint("proveedores", __name__, url_prefix="/proveedores")

# Listar todos los proveedores, solo admin
@proveedores_bp.route("/", methods=["GET"])
@jwt_required()
@rol_access("admin")
def listar_proveedores():
    return ProveedorController.listar_proveedores()

# Ver un proveedor por ID, solo para admin
@proveedores_bp.route("/<int:id>", methods=["GET"])
@jwt_required()
@rol_access("admin")
def ver_proveedor(id):
    return ProveedorController.ver_proveedor(id)


# Crear un proveedor, solo admin
@proveedores_bp.route("/", methods=["POST"])
@jwt_required()
@rol_access("admin")
def crear_proveedor():
    return ProveedorController.crear_proveedor()


# Editar un proveedor por ID, solo admin
@proveedores_bp.route("/<int:id>", methods=["PUT"])
@jwt_required()
@rol_access("admin")
def editar_proveedor(id):
    return ProveedorController.editar_proveedor(id)


# Borrar un  proveedor por su ID, solo admin
@proveedores_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
@rol_access("admin")
def eliminar_proveedor(id):
    return ProveedorController.eliminar_proveedor(id)
