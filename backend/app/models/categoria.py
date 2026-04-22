from app.models.base_model import BaseModel
from app.models import db

class Categoria(BaseModel):
    __tablename__ = "categorias"

    nombre = db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    productos = db.relationship("Producto", back_populates="categoria")

    def __repr__(self):
        return f'Categoria {self.nombre}'

    def to_dict(self, incluye_productos=False):
        data = super().to_dict()
        data.update({
            "nombre": self.nombre,
            "descripcion": self.descripcion
        })
        if incluye_productos:
            data["productos"] = [p.to_dict(incluye_categoria=False) for p in self.productos]
        return data






