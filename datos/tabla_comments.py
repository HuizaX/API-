# tabla_comments.py
from conexion_db import conectar

def insertar_comments(comments):
    """Inserta una lista de comentarios en la tabla comments."""
    conn = conectar()
    cursor = conn.cursor()
    for comment in comments:
        cursor.execute('''
            INSERT OR IGNORE INTO comments (id, post_id, name, email, body)
            VALUES (?, ?, ?, ?, ?)
        ''', (
            comment['id'],
            comment['postId'],
            comment['name'],
            comment['email'],
            comment['body']
        ))
    conn.commit()
    conn.close()