from app.models.base_model import BaseModel
from app.models import db

class Producto(BaseModel):
    __tablename__ = "productos"

    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text)
    precio_costo = db.Column(db.Numeric(10,2), nullable=False)
    precio_venta = db.Column(db.Numeric(10,2), nullable=False)
    stock_actual = db.Column(db.Integer, default=0)
    stock_minimo = db.Column(db.Integer, default=0)

    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey("proveedores.id"))

    categoria = db.relationship("Categoria", back_populates="productos")
    proveedor = db.relationship("Proveedor", back_populates="productos")
    movimientos = db.relationship("MovimientoStock", back_populates="producto")

    def to_dict(self, incluye_categoria=True, incluye_proveedor=True):
        data = super().to_dict()
        data.update({
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio_costo": str(self.precio_costo),
            "precio_venta": str(self.precio_venta),
            "stock_actual": self.stock_actual,
            "stock_minimo": self.stock_minimo
        })
        if incluye_categoria:
            data["categoria"] = self.categoria.to_dict(incluye_productos=False)
        if incluye_proveedor and self.proveedor:
            data["proveedor"] = self.proveedor.to_dict(incluye_productos=False)
        return data


def __repr__(self):
    return f'Producto {self.nombre}, stock {self.stock}'

