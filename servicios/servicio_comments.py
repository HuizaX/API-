import requests

# URL base de la API para comentarios
URL_COMMENTS = "https://jsonplaceholder.typicode.com/comments"

def obtener_todos_los_comentarios():
    """
    Obtiene todos los comentarios desde la API JSONPlaceholder.
    """
    try:
        response = requests.get(URL_COMMENTS)
        response.raise_for_status()  # Lanza una excepción si ocurre un error HTTP
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener comentarios: {e}")
        return []

def buscar_comentario_por_campo(campo, valor):
    """
    Busca comentarios por un campo y valor específicos.
    - campo: El nombre del campo en el JSON (ejemplo: 'name', 'email', 'body').
    - valor: El valor a buscar.
    """
    try:
        comentarios = obtener_todos_los_comentarios()
        resultados = [comentario for comentario in comentarios if comentario.get(campo) == valor]
        return resultados
    except Exception as e:
        print(f"Error al buscar comentarios: {e}")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    # Obtener y mostrar todos los comentarios
    print("Obteniendo todos los comentarios...")
    comentarios = obtener_todos_los_comentarios()
    for comentario in comentarios[:10]:  # Mostrar solo los primeros 10 comentarios
        print(f"ID: {comentario['id']}, Nombre: {comentario['name']}, Email: {comentario['email']}")

    # Buscar un comentario por email
    print("\nBuscando comentario con email 'Eliseo@gardner.biz'...")
    comentario_encontrado = buscar_comentario_por_campo("email", "Eliseo@gardner.biz")
    if comentario_encontrado:
        for comentario in comentario_encontrado:
            print(f"ID: {comentario['id']}, Nombre: {comentario['name']}, Email: {comentario['email']}, Cuerpo: {comentario['body']}")
    else:
        print("No se encontró ningún comentario con ese criterio.")
