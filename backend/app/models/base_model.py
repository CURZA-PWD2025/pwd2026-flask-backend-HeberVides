from app.models import db

# Modelo Base del que van a heredar los demas

class BaseModel(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    activo = db.Column(db.String(1), default = 'S')
    created_at = db.Column(db.DateTime, server_default = db.func.now())
    updated_at = db.Column(db.DateTime, onupdate = db.func.now())
    
    def to_dict(self) -> dict:
        return{
            'id' : self.id,
            'activo' : self.activo,
            'created_at' : self.created_at,
            'updated_at' : self.updated_at
        }