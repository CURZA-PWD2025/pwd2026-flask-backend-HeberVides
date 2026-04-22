from app.models.producto import Producto
from app.models.movimiento_stock import MovimientoStock
from app.models import db
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity


class MovimientoController:

    # Listar todos los movimientos, para admins
    @staticmethod
    def listar_movimientos():
        movimientos = MovimientoStock.query.all()
        return jsonify([
            {"id": movimientos.id, "tipo": movimientos.tipo, "cantidad": movimientos.cantidad, "motivo": movimientos.motivo, 
            "producto": movimientos.producto.nombre if movimientos.producto else None,
            "usuario": movimientos.user.nombre if movimientos.user else None
            } for movimientos in movimientos
        ])


    # Listar movimientos del usuario autenticado
    @staticmethod
    def listar_mis_movimientos():
        user_id = get_jwt_identity()
        movimientos = MovimientoStock.query.filter_by(user_id=user_id).all()
        return jsonify([{"id": m.id, "tipo": m.tipo, "cantidad": m.cantidad, "motivo": m.motivo, "producto": m.producto.nombre if m.producto else None} for m in movimientos])


    # Registrar los movimiento solo para el operador
    @staticmethod
    def registrar_movimiento():
        data = request.get_json()
        producto = Producto.query.get_or_404(data["producto_id"])
        cantidad = int(data["cantidad"])
        tipo = data["tipo"]  
        
        # La entrada/salida

        # Se valida el stock
        if tipo == "salida" and producto.stock_actual < cantidad:
            return jsonify({"error": "El Stock es insuficiente para registrar la salida"}), 400

        # Se Actualiza el stock
        if tipo == "entrada":
            producto.stock_actual += cantidad
        elif tipo == "salida":
            producto.stock_actual -= cantidad

        # Se Registra el movimiento
        user_id = get_jwt_identity()
        movimiento = MovimientoStock(
            tipo=tipo,
            cantidad=cantidad,
            producto_id=producto.id,
            user_id=user_id,
            motivo=data.get("motivo")
        )
        db.session.add(movimiento)
        db.session.commit()

        return jsonify({
            "id": movimiento.id,
            "tipo": movimiento.tipo,
            "cantidad": movimiento.cantidad,
            "producto": producto.nombre,
            "stock_actual": producto.stock_actual
        }), 201
