from app.controllers.movimiento_stock_controller import MovimientoController
from app.decorators.rol_access import rol_access
from flask import Blueprint
from flask_jwt_extended import jwt_required

# Ruta para registrar en el __init__.py
movimientos_bp = Blueprint("movimientos", __name__, url_prefix="/movimientos")

# Listar todos los movimientos, solo admin
@movimientos_bp.route("/", methods=["GET"])
@jwt_required()
@rol_access("admin")
def listar_movimientos():
    return MovimientoController.listar_movimientos()


# Listar los movimientos del usuario autenticado
@movimientos_bp.route("/mios", methods=["GET"])
@jwt_required()
@rol_access("admin", "operador")
def listar_mis_movimientos():
    return MovimientoController.listar_mis_movimientos()


# Registrar los movimiento solo del operador
@movimientos_bp.route("/", methods=["POST"])
@jwt_required()
@rol_access("operador")
def registrar_movimiento():
    return MovimientoController.registrar_movimiento()