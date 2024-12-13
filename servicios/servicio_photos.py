import requests

URL_PHOTOS = "https://jsonplaceholder.typicode.com/photos"

def obtener_todas_las_photos():
    """
    Obtiene todas las fotos desde la API JSONPlaceholder.
    """
    try:
        response = requests.get(URL_PHOTOS)
        response.raise_for_status()  # Lanza una excepción si ocurre un error HTTP
        return response.json()
    except requests.RequestException as e:
        print(f"Error al obtener fotos: {e}")
        return []

def buscar_photo_por_campo(campo, valor):
    """
    Busca fotos por un campo y valor específicos.
    - campo: El nombre del campo en el JSON (ejemplo: 'title', 'albumId').
    - valor: El valor a buscar.
    """
    try:
        photos = obtener_todas_las_photos()
        resultados = [photo for photo in photos if photo.get(campo) == valor]
        return resultados
    except Exception as e:
        print(f"Error al buscar fotos: {e}")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    # Obtener y mostrar todas las fotos
    print("Obteniendo todas las fotos...")
    photos = obtener_todas_las_photos()
    for photo in photos[:10]:  # Mostrar solo las primeras 10 fotos para no sobrecargar la salida
        print(f"ID: {photo['id']}, Título: {photo['title']}, URL: {photo['url']}")

    # Buscar una foto por título
    print("\nBuscando foto con título 'accusamus beatae ad facilis cum similique qui sunt'...")
    photo_encontrada = buscar_photo_por_campo("title", "accusamus beatae ad facilis cum similique qui sunt")
    if photo_encontrada:
        for photo in photo_encontrada:
            print(f"ID: {photo['id']}, Título: {photo['title']}, URL: {photo['url']}")
    else:
        print("No se encontró ninguna foto con ese criterio.")