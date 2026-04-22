from app.models.categoria import Categoria
from app.models import db
from flask import request, jsonify


class CategoriaController:

    # Se listan las categorías, se necesita estar autenticado.
    @staticmethod
    def listar_categorias():
        categorias = Categoria.query.all()
        return jsonify([{"id": categorias.id, "nombre": categorias.nombre, "descripcion": categorias.descripcion} for categorias in categorias])


    # Ver una categoría por el ID, se necesita estar autenticado tmb.
    @staticmethod
    def ver_categoria(id):
        categoria = Categoria.query.get_or_404(id)
        return jsonify({"id": categoria.id, "nombre": categoria.nombre, "descripcion": categoria.descripcion})


    # Crear categoría, si o si hay que ser admin.
    @staticmethod
    def crear_categoria():
        data = request.get_json()
        nueva = Categoria(nombre=data["nombre"], descripcion=data.get("descripcion"))
        db.session.add(nueva)
        db.session.commit()
        return jsonify({"id": nueva.id, "nombre": nueva.nombre}), 201


    # Editar categoría por su ID, imperativo ser admin.
    @staticmethod
    def editar_categoria(id):
        categoria = Categoria.query.get_or_404(id)
        data = request.get_json()
        categoria.nombre = data.get("nombre", categoria.nombre)
        categoria.descripcion = data.get("descripcion", categoria.descripcion)
        db.session.commit()
        return jsonify({"id": categoria.id, "nombre": categoria.nombre})


    # Borrar categoría por el ID, only admin.
    @staticmethod
    def eliminar_categoria(id):
        categoria = Categoria.query.get_or_404(id)
        db.session.delete(categoria)
        db.session.commit()
        return jsonify({"message": "Categoría Borrada"})
