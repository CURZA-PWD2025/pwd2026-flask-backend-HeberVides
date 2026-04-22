from app.models.user import User
from app.models.rol import Rol
from app.models.categoria import Categoria
from app.models.proveedor import Proveedor
from app.models.producto import Producto
from app.models import db
from app import create_app

app = create_app()

def seed():
    with app.app_context():

        #Crear Roles (actualizado "user" por "operador" pa que ande con los roles y modelos)
        admin_role = Rol(nombre='admin')
        operador_role = Rol(nombre='operador')
        db.session.add_all([admin_role, operador_role])
        db.session.commit()

        #Crear Usuarios (actualizado tmb)

        admin_user = User(nombre='admin01', rol_id=admin_role.id, password='admin123', email='admin01@example.com')
        operador_user = User(nombre='operador01', rol_id=operador_role.id, password='operador123', email='operador01@example.com')
        db.session.add_all([admin_user, operador_user])
        db.session.commit()    

        # Categorías
        alm = Categoria(nombre='Almacén', descripcion='Productos secos')
        lim = Categoria(nombre='Limpieza', descripcion='Artículos de limpieza')
        db.session.add_all([alm, lim])
        db.session.commit()

        # Proveedor
        prov = Proveedor(nombre='Distribuidora Norte', telefono='2994001234')
        db.session.add(prov)
        db.session.commit()

        # Productos
        db.session.add_all([
            Producto(nombre='Harina 000', precio_costo=280, precio_venta=350,
                    stock_actual=50, stock_minimo=10,
                    categoria_id=alm.id, proveedor_id=prov.id),
            Producto(nombre='Lavandina 1L', precio_costo=150, precio_venta=210,
                    stock_actual=30, stock_minimo=5,
                    categoria_id=lim.id, proveedor_id=prov.id),
        ])
        db.session.commit()
        print("Seed completado.")

    
if __name__ == "__main__":
    seed()