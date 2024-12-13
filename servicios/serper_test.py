import requests

def buscar_en_serper(consulta):
    """
    Realiza una búsqueda en la API de Serper y devuelve los resultados.

    :param consulta: Término de búsqueda.
    :return: Diccionario con los resultados de la búsqueda o un mensaje de error.
    """
    url = "https://google.serper.dev/search"
    
    # Encabezados requeridos para la autenticación
    headers = {
        "X-API-KEY": "d1294a4fd82efbfe67f9fef527ffe95a11b84fa0",
        "Content-Type": "application/json"
    }

    # Datos de la solicitud
    payload = {
        "q": consulta
    }

    try:
        # Realiza la solicitud POST
        respuesta = requests.post(url, json=payload, headers=headers)
        
        # Verifica si la respuesta fue exitosa
        if respuesta.status_code == 200:
            return respuesta.json()
        else:
            return {"error": f"Error en la solicitud: {respuesta.status_code}", "detalles": respuesta.text}
    except requests.RequestException as e:
        return {"error": "Error al conectar con la API", "detalles": str(e)}

# Ejemplo de uso
if __name__ == "__main__":
    consulta = "Python programming"
    
    resultados = buscar_en_serper(consulta)
    print(resultados)
