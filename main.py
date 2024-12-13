from datos.conexion_db import crear_tablas
from datos.api_clientes import obtener_datos
from datos.tabla_users import insertar_users
from datos.tabla_photos import insertar_photos
from datos.tabla_comments import insertar_comments

def main():
    # Crear las tablas en la base de datos
    crear_tablas()

    # Obtener y guardar usuarios
    users = obtener_datos("users")
    insertar_users(users)

    # Obtener y guardar fotos
    photos = obtener_datos("photos")
    insertar_photos(photos)

    # Obtener y guardar comentarios
    comments = obtener_datos("comments")
    insertar_comments(comments)

    print("Datos cargados exitosamente en la base de datos.")

if __name__ == "__main__":
    main()

