from app.models.base_model import BaseModel
from app.models import db

class Proveedor(BaseModel):
    __tablename__ = "proveedores"

    nombre = db.Column(db.String(150), nullable=False)
    contacto = db.Column(db.String(100))
    telefono = db.Column(db.String(30))
    email = db.Column(db.String(120))

    productos = db.relationship("Producto", back_populates="proveedor")
    
    def __repr__(self):
        return f'Proveedor {self.nombre}'

    def to_dict(self, incluye_productos=False):
        data = super().to_dict()
        data.update({
            "nombre": self.nombre,
            "contacto": self.contacto,
            "telefono": self.telefono,
            "email": self.email
        })
        if incluye_productos:
            data["productos"] = [p.to_dict(incluye_proveedor=False) for p in self.productos]
        return data

