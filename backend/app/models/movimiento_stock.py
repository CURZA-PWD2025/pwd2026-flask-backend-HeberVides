from app.models.base_model import BaseModel
from app.models import db

class MovimientoStock(BaseModel):
    __tablename__ = "movimientos_stock"

    tipo = db.Column(db.String(10), nullable=False)  # 'entrada' o 'salida'
    cantidad = db.Column(db.Integer, nullable=False)
    motivo = db.Column(db.String(200))

    producto_id = db.Column(db.Integer, db.ForeignKey("productos.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    producto = db.relationship("Producto", back_populates="movimientos")
    user = db.relationship("User")

    def __init__(self, tipo: str, cantidad: int, producto_id: int, user_id: int, motivo: str = None):
        if tipo not in ["entrada", "salida"]:
            raise ValueError("El tipo debe ser 'entrada' o 'salida'")
        if cantidad is None or cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a 0")

        self.tipo = tipo
        self.cantidad = cantidad
        self.producto_id = producto_id
        self.user_id = user_id
        self.motivo = motivo

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "tipo": self.tipo,
            "cantidad": self.cantidad,
            "motivo": self.motivo,
            "producto": self.producto.to_dict(incluye_categoria=False, incluye_proveedor=False),
            "user": self.user.to_dict(incluye_rol=False)
        })
        return data
