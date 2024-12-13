
import requests

def obtener_datos(endpoint):
    """Obtiene datos desde un endpoint de la API JSONPlaceholder."""
    url = f"https://jsonplaceholder.typicode.com/{endpoint}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error al obtener datos desde la API: {response.status_code}")
