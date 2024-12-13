# tabla_users.py
from conexion_db import conectar

def insertar_users(users):
    """Inserta una lista de usuarios en la tabla users."""
    conn = conectar()
    cursor = conn.cursor()
    for user in users:
        cursor.execute('''
            INSERT OR IGNORE INTO users (id, name, username, email, address, phone, website, company)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user['id'],
            user['name'],
            user['username'],
            user['email'],
            str(user['address']),
            user['phone'],
            user['website'],
            str(user['company'])
        ))
    conn.commit()
    conn.close()