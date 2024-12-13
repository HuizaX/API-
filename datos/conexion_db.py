import mysql.connector
from mysql.connector import errorcode
from auxiliares.constantes import host, user, password, database

def generar_conexion():
    config={
        'root': user,
        '': password,
        'localhost': host,
        'api': database
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion and conexion.is_connected():
            return conexion
        else:
            print("No fue posible conectarse a la base de datos.")
    
    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Acceso denegado, usuario o contraseña incorrectos.")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Su base de datos NO existe")
        else:
            print(error)
    else:
        conexion.close()
        
def leer_datos(consulta):      
    conexion = generar_conexion()
    cursor = conexion.cursor()
    if cursor != None:
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        cursor.close()    
        return resultado
    else:
        print("Su búsqueda no arrojó resultados...")
    conexion.close()
        
def insertar_datos(consulta):      
    conexion = generar_conexion()
    cursor = conexion.cursor()
    if cursor != None:
        cursor.execute(consulta)
        conexion.commit()
        id = cursor.lastrowid
        cursor.close()        
        return print(f"Id registro insertado = {id}")
    else:
        print("Su búsqueda no arrojó resultados...")
    conexion.close()
