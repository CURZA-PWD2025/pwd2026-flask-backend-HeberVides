from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify


def rol_access(*roles_permitidos):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # verifica que tenga el token en el request, el get_jwt toma los datos del mismo 
            # busca que tenga el claim "rol" 
            verify_jwt_in_request()
            claims = get_jwt()
            if claims.get("rol") not in roles_permitidos:
                return jsonify(
                    msg=f"Acceso denegado: se requiere rol {' o '.join(roles_permitidos)}"
                ), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator