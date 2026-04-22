from app.models.base_model import BaseModel
from app.models import db
from werkzeug.security import generate_password_hash, check_password_hash

# Tmb Modifique el modelo user para evitar bucles

class User(BaseModel):
    
    __tablename__= 'users'
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    rol_id = db.Column(db.Integer, db.ForeignKey('roles.id'),)
    password = db.Column(db.String(255), nullable=False)
    rol = db.relationship('Rol', back_populates='users')
    
    def __init__(self, nombre:str, email:str, password:str, rol_id:int) -> None:
      self.nombre = nombre
      self.email = email
      self.rol_id = rol_id
      self.generate_password(password)
    
    def __repr__(self):
       return f"usuario {self.nombre}, email {self.email} , fecha de creacion {self.created_at} " 
     
    def to_dict(self, incluye_rol = True):
      data = super().to_dict()
      data.update(
      {
        'nombre':self.nombre,
        'email':self.email,
      })
      if incluye_rol:
         data['rol'] = self.rol.to_dict(incluye_user = True)
      return data
      
    def validate_password(self, password:str) -> bool:
      return check_password_hash(self.password, password)
    
    def generate_password(self, password:str):
      self.password = generate_password_hash(password)