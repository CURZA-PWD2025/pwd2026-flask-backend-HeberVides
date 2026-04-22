from app.models.base_model import BaseModel
from app.models import db

# Modifique el modelo rol para que no tenga problemas con bucles

class Rol(BaseModel):
    __tablename__="roles"

    nombre = db.Column(db.String, unique=True, nullable=False)
    users = db.relationship('User', back_populates='rol')
    
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        
    def to_dict(self, incluye_user = True):
        data = super().to_dict()
        data.update(
        {
            'nombre': self.nombre
        })
        if incluye_user:
            data['user'] = [user.to_dict(incluye_rol = False) for user in self.users]
        return data