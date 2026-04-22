from app.models.producto import Producto
from flask import request, jsonify
from app.models import db


class ProductoController:

    # Listar todos los Productos, autenticación necesaria.
    @staticmethod
    def listar_productos():
        productos = Producto.query.all()
        return jsonify([{"id": productos.id, "nombre": productos.nombre, "precio_costo": productos.precio_costo, "precio_venta": productos.precio_venta, 
                        "stock_actual": productos.stock_actual,"stock_minimo": productos.stock_minimo,"categoria": productos.categoria.nombre if productos.categoria else None,
                        "proveedor": productos.proveedor.nombre if productos.proveedor else None} for productos in productos
        ])

    # Ver un producto por su ID, autenticación requerida
    @staticmethod
    def ver_producto(id):
        producto = Producto.query.get_or_404(id)
        return jsonify({"id": producto.id, "nombre": producto.nombre, "precio_costo": producto.precio_costo, "precio_venta": producto.precio_venta, "stock_actual": producto.stock_actual,
            "stock_minimo": producto.stock_minimo, "categoria": producto.categoria.nombre if producto.categoria else None, "proveedor": producto.proveedor.nombre if producto.proveedor else None
        })


    # Crear un producto, solo admin
    @staticmethod
    def crear_producto():
        data = request.get_json()
        nuevo = Producto(
            nombre=data["nombre"],
            precio_costo=data["precio_costo"],
            precio_venta=data["precio_venta"],
            stock_actual=data.get("stock_actual", 0),
            stock_minimo=data.get("stock_minimo", 0),
            categoria_id=data["categoria_id"],
            proveedor_id=data["proveedor_id"]
        )
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"id": nuevo.id, "nombre": nuevo.nombre}), 201


    # Editar un producto por su ID, solo admin
    @staticmethod
    def editar_producto(id):
        producto = Producto.query.get_or_404(id)
        data = request.get_json()
        producto.nombre = data.get("nombre", producto.nombre)
        producto.precio_costo = data.get("precio_costo", producto.precio_costo)
        producto.precio_venta = data.get("precio_venta", producto.precio_venta)
        producto.stock_actual = data.get("stock_actual", producto.stock_actual)
        producto.stock_minimo = data.get("stock_minimo", producto.stock_minimo)
        producto.categoria_id = data.get("categoria_id", producto.categoria_id)
        producto.proveedor_id = data.get("proveedor_id", producto.proveedor_id)
        db.session.commit()
        return jsonify({"id": producto.id, "nombre": producto.nombre})


    # Borrar un producto por su ID, solo admin
    @staticmethod
    def eliminar_producto(id):
        producto = Producto.query.get_or_404(id)
        db.session.delete(producto)
        db.session.commit()
        return jsonify({"message": "Producto eliminado"})
