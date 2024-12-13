import requests

# URL base de la API
URL_BASE = "https://jsonplaceholder.typicode.com/users"

def obtener_todos_los_usuarios():
    """
    Obtiene todos los usuarios desde la API JSONPlaceholder.
    """
    try:
        response = requests.get(URL_BASE)
        response.raise_for_status()  # Lanza una excepción si ocurre un error HTTP
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener usuarios: {e}")
        return []

def buscar_usuario_por_campo(campo, valor):
    """
    Busca usuarios por un campo y valor específicos.
    - campo: El nombre del campo en el JSON (ejemplo: 'name', 'email').
    - valor: El valor a buscar.
    """
    try:
        usuarios = obtener_todos_los_usuarios()
        resultados = [usuario for usuario in usuarios if usuario.get(campo) == valor]
        return resultados
    except Exception as e:
        print(f"Error al buscar usuarios: {e}")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    # Obtener y mostrar todos los usuarios
    print("Obteniendo todos los usuarios...")
    usuarios = obtener_todos_los_usuarios()
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nombre: {usuario['name']}, Email: {usuario['email']}")

    # Buscar un usuario por nombre
    print("\nBuscando usuario con nombre 'Leanne Graham'...")
    usuario_encontrado = buscar_usuario_por_campo("name", "Leanne Graham")
    if usuario_encontrado:
        for usuario in usuario_encontrado:
            print(f"ID: {usuario['id']}, Nombre: {usuario['name']}, Email: {usuario['email']}")
    else:
        print("No se encontró ningún usuario con ese criterio.")