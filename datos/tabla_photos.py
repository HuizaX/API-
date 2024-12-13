# tabla_photos.py
from conexion_db import conectar

def insertar_photos(photos):
    """Inserta una lista de fotos en la tabla photos."""
    conn = conectar()
    cursor = conn.cursor()
    for photo in photos:
        cursor.execute('''
            INSERT OR IGNORE INTO photos (id, album_id, title, url, thumbnail_url)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            photo['id'],
            photo['albumId'],
            photo['title'],
            photo['url'],
            photo['thumbnailUrl']
        ))
    conn.commit()
    conn.close()