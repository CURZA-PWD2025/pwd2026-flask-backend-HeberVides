from app.models.proveedor import Proveedor
from flask import request, jsonify
from app.models import db


class ProveedorController:

    # Ver todos los proveedores, solo admin
    @staticmethod
    def listar_proveedores():
        proveedores = Proveedor.query.all()
        return jsonify([{"id": proveedores.id, "nombre": proveedores.nombre, "telefono": proveedores.telefono} for proveedores in proveedores])


    # Ver un proveedor por su ID, solo admin
    @staticmethod
    def ver_proveedor(id):
        proveedor = Proveedor.query.get_or_404(id)
        return jsonify({"id": proveedor.id, "nombre": proveedor.nombre, "telefono": proveedor.telefono})


    # Crear un proveedor, solo para admin
    @staticmethod
    def crear_proveedor():
        data = request.get_json()
        nuevo = Proveedor(nombre=data["nombre"], telefono=data.get("telefono"))
        db.session.add(nuevo)
        db.session.commit()
        return jsonify({"id": nuevo.id, "nombre": nuevo.nombre}), 201


    # Editar un proveedor por ID, solo admin
    @staticmethod
    def editar_proveedor(id):
        proveedor = Proveedor.query.get_or_404(id)
        data = request.get_json()
        proveedor.nombre = data.get("nombre", proveedor.nombre)
        proveedor.telefono = data.get("telefono", proveedor.telefono)
        db.session.commit()
        return jsonify({"id": proveedor.id, "nombre": proveedor.nombre, "telefono": proveedor.telefono})

    # Borrar un proveedor por su ID, solo admin

    @staticmethod
    def eliminar_proveedor(id):
        proveedor = Proveedor.query.get_or_404(id)
        db.session.delete(proveedor)
        db.session.commit()
        return jsonify({"message": "Proveedor eliminado"})
