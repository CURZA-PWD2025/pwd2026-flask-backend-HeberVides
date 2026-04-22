from flask import Blueprint
from app.routes.auth_routes import auth_bp
from app.routes.rol_routes import roles
from app.routes.user_routes import users
from app.routes.categorias_routes import categorias_bp
from app.routes.proveedores_routes import proveedores_bp
from app.routes.productos_routes import productos_bp
from app.routes.movimientos_routes import movimientos_bp

# Nombre (api_v1) de la ruta que anida las rutas de los otros modelos
api_v1 = Blueprint('api_v1', __name__, url_prefix='/api_v1')

api_v1.register_blueprint(users)
api_v1.register_blueprint(roles)
api_v1.register_blueprint(auth_bp)
api_v1.register_blueprint(categorias_bp)
api_v1.register_blueprint(proveedores_bp)
api_v1.register_blueprint(productos_bp)
api_v1.register_blueprint(movimientos_bp)

# Acá agrupo las rutas, en "api_v1" que se va a usar en el __init__.py de la app para registrar las mismas.