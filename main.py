from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox, scrolledtext
from servicios.serper_test import buscar_en_serper
from servicios.servicio_users import *
from servicios.servicio_photos import obtener_todas_las_photos
from servicios.servicio_comments import obtener_todos_los_comentarios

# Funciones de cifrado y descifrado
def generar_clave():
    try:
        with open("clave.key", "rb") as archivo_clave:
            clave = archivo_clave.read()
    except FileNotFoundError:
        clave = Fernet.generate_key()
        with open("clave.key", "wb") as archivo_clave:
            archivo_clave.write(clave)

def cargar_clave():
    with open("clave.key", "rb") as archivo_clave:
        return archivo_clave.read()

def encriptar_contrasena(contrasena):
    clave = cargar_clave()
    fernet = Fernet(clave)
    contrasena_encriptada = fernet.encrypt(contrasena.encode())
    return contrasena_encriptada

def desencriptar_contrasena(contrasena_encriptada):
    clave = cargar_clave()
    fernet = Fernet(clave)
    contrasena_desencriptada = fernet.decrypt(contrasena_encriptada.encode()).decode()
    return contrasena_desencriptada

def guardar_contrasena(nombre, contrasena_encriptada):
    try:
        with open("contrasenas.txt", "a") as archivo:
            archivo.write(f"{nombre}:{contrasena_encriptada.decode()}\n")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo guardar la contraseña: {e}")
        return False
    return True

def cargar_contrasenas():
    contraseñas = {}
    try:
        with open("contrasenas.txt", "r") as archivo:
            for linea in archivo:
                etiqueta, contrasena_encriptada = linea.strip().split(":")
                contraseñas[etiqueta] = contrasena_encriptada
    except FileNotFoundError:
        messagebox.showerror("Error", "El archivo 'contrasenas.txt' no existe.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al leer el archivo: {e}")
    return contraseñas

def procesar_y_guardar_contrasena(entrada_nombre, entrada_contrasena):
    nombre = entrada_nombre.get().strip()
    contrasena = entrada_contrasena.get().strip()

    if not nombre or not contrasena:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    generar_clave()

    contrasena_encriptada = encriptar_contrasena(contrasena)

    if guardar_contrasena(nombre, contrasena_encriptada):
        messagebox.showinfo("Éxito", "Contraseña encriptada y guardada correctamente.")
        entrada_nombre.delete(0, tk.END)
        entrada_contrasena.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "No se pudo guardar la contraseña.")

def validar_contrasena(entrada_nombre, entrada_contrasena):
    etiqueta = entrada_nombre.get().strip()
    contrasena = entrada_contrasena.get().strip()

    if not etiqueta or not contrasena:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    contraseñas = cargar_contrasenas()
    if etiqueta not in contraseñas:
        messagebox.showerror("Error", "Etiqueta no encontrada.")
        return

    contrasena_encriptada = contraseñas[etiqueta]
    try:
        contrasena_desencriptada = desencriptar_contrasena(contrasena_encriptada)
        if contrasena == contrasena_desencriptada:
            messagebox.showinfo("Éxito", "Contraseña válida.")
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al validar la contraseña: {e}")

def realizar_busqueda(entrada_busqueda):
    consulta = entrada_busqueda.get().strip()

    if not consulta:
        messagebox.showerror("Error", "Por favor, ingrese un término de búsqueda.")
        return

    resultados = buscar_en_serper(consulta)

    if "error" in resultados:
        messagebox.showerror("Error", f"Error en la búsqueda: {resultados['detalles']}")
    else:
        mensaje = "Resultados:\n"
        for item in resultados.get("organic", []):
            mensaje += f"- {item.get('title', 'Sin título')}: {item.get('link', 'Sin enlace')}\n"
        messagebox.showinfo("Resultados de la búsqueda", mensaje)

def mostrar_pantalla_principal():
    def abrir_guardar():
        root_guardar.deiconify()
        root_main.withdraw()

    def abrir_validar():
        root_validar.deiconify()
        root_main.withdraw()

    def abrir_busqueda():
        root_busqueda.deiconify()
        root_main.withdraw()

    def abrir_servicios():
        root_servicios.deiconify()
        root_main.withdraw()

    def abrir_users():
        usuarios = obtener_todos_los_usuarios()
        ventana_usuarios = tk.Toplevel()
        ventana_usuarios.title("Usuarios")

        text_area = scrolledtext.ScrolledText(ventana_usuarios, wrap=tk.WORD, width=60, height=20)
        text_area.pack(pady=10, padx=10)

        if usuarios:
            for usuario in usuarios:
                text_area.insert(tk.END, f"ID: {usuario['id']}\nNombre: {usuario['name']}\nEmail: {usuario['email']}\n---\n")
        else:
            text_area.insert(tk.END, "No se pudieron obtener usuarios.")

    def abrir_photos():
        fotos = obtener_todas_las_photos()
        ventana_fotos = tk.Toplevel()
        ventana_fotos.title("Fotos")

        text_area = scrolledtext.ScrolledText(ventana_fotos, wrap=tk.WORD, width=60, height=20)
        text_area.pack(pady=10, padx=10)

        if fotos:
            for foto in fotos[:10]:  # Mostramos solo las primeras 10 fotos para no sobrecargar
                text_area.insert(tk.END, f"ID: {foto['id']}\nTítulo: {foto['title']}\nURL: {foto['url']}\n---\n")
        else:
            text_area.insert(tk.END, "No se pudieron obtener fotos.")

    def abrir_comments():
        comentarios = obtener_todos_los_comentarios()
        ventana_comentarios = tk.Toplevel()
        ventana_comentarios.title("Comentarios")

        text_area = scrolledtext.ScrolledText(ventana_comentarios, wrap=tk.WORD, width=60, height=20)
        text_area.pack(pady=10, padx=10)

        if comentarios:
            for comentario in comentarios[:10]:  # Mostramos solo los primeros 10 comentarios
                text_area.insert(tk.END, f"ID: {comentario['id']}\nNombre: {comentario['name']}\nEmail: {comentario['email']}\nCuerpo: {comentario['body']}\n---\n")
        else:
            text_area.insert(tk.END, "No se pudieron obtener comentarios.")

    def volver():
        root_main.deiconify()
        root_guardar.withdraw()
        root_validar.withdraw()
        root_busqueda.withdraw()
        root_servicios.withdraw()

    root_main = tk.Toplevel()
    root_main.title("Gestión de Contraseñas")

    tk.Label(root_main, text="Seleccione una opción:").pack(pady=10)

    btn_ingresar = tk.Button(root_main, text="Ingresar Contraseña", command=abrir_guardar)
    btn_ingresar.pack(pady=5)

    btn_validar = tk.Button(root_main, text="Validar Contraseña", command=abrir_validar)
    btn_validar.pack(pady=5)

    btn_busqueda = tk.Button(root_main, text="Realizar Búsqueda en Serper", command=abrir_busqueda)
    btn_busqueda.pack(pady=5)

    btn_servicios = tk.Button(root_main, text="Servicios", command=abrir_servicios)
    btn_servicios.pack(pady=5)

    root_guardar = tk.Toplevel()
    root_guardar.title("Ingresar Contraseña")
    root_guardar.withdraw()

    frame_guardar = tk.Frame(root_guardar, padx=10, pady=10)
    frame_guardar.pack()

    tk.Label(frame_guardar, text="Empleado (nombre y apellidos):").grid(row=0, column=0, pady=5, sticky=tk.W)
    entrada_nombre_guardar = tk.Entry(frame_guardar, width=40)
    entrada_nombre_guardar.grid(row=0, column=1, pady=5)

    tk.Label(frame_guardar, text="Ingrese la contraseña:").grid(row=1, column=0, pady=5, sticky=tk.W)
    entrada_contrasena_guardar = tk.Entry(frame_guardar, width=40, show="*")
    entrada_contrasena_guardar.grid(row=1, column=1, pady=5)

    btn_guardar = tk.Button(frame_guardar, text="Guardar Contraseña", command=lambda: procesar_y_guardar_contrasena(entrada_nombre_guardar, entrada_contrasena_guardar))
    btn_guardar.grid(row=2, columnspan=2, pady=10)

    btn_volver_guardar = tk.Button(frame_guardar, text="Volver", command=volver)
    btn_volver_guardar.grid(row=3, columnspan=2, pady=10)

    root_validar = tk.Toplevel()
    root_validar.title("Validar Contraseña")
    root_validar.withdraw()

    frame_validar = tk.Frame(root_validar, padx=10, pady=10)
    frame_validar.pack()

    tk.Label(frame_validar, text="Etiqueta (nombre):").grid(row=0, column=0, pady=5, sticky=tk.W)
    entrada_nombre_validar = tk.Entry(frame_validar, width=40)
    entrada_nombre_validar.grid(row=0, column=1, pady=5)

    tk.Label(frame_validar, text="Ingrese la contraseña:").grid(row=1, column=0, pady=5, sticky=tk.W)
    entrada_contrasena_validar = tk.Entry(frame_validar, width=40, show="*")
    entrada_contrasena_validar.grid(row=1, column=1, pady=5)

    btn_validar = tk.Button(frame_validar, text="Validar Contraseña", command=lambda: validar_contrasena(entrada_nombre_validar, entrada_contrasena_validar))
    btn_validar.grid(row=2, columnspan=2, pady=10)

    btn_volver_validar = tk.Button(frame_validar, text="Volver", command=volver)
    btn_volver_validar.grid(row=3, columnspan=2, pady=10)

    root_busqueda = tk.Toplevel()
    root_busqueda.title("Buscar en Serper")
    root_busqueda.withdraw()

    frame_busqueda = tk.Frame(root_busqueda, padx=10, pady=10)
    frame_busqueda.pack()

    tk.Label(frame_busqueda, text="Ingrese su búsqueda:").grid(row=0, column=0, pady=5, sticky=tk.W)
    entrada_busqueda = tk.Entry(frame_busqueda, width=40)
    entrada_busqueda.grid(row=0, column=1, pady=5)

    btn_buscar = tk.Button(frame_busqueda, text="Buscar", command=lambda: realizar_busqueda(entrada_busqueda))
    btn_buscar.grid(row=1, columnspan=2, pady=10)

    btn_volver_busqueda = tk.Button(frame_busqueda, text="Volver", command=volver)
    btn_volver_busqueda.grid(row=2, columnspan=2, pady=10)

    root_servicios = tk.Toplevel()
    root_servicios.title("Servicios")
    root_servicios.withdraw()

    frame_servicios = tk.Frame(root_servicios, padx=10, pady=10)
    frame_servicios.pack()

    tk.Label(frame_servicios, text="Seleccione una opción de servicios:").pack(pady=10)

    btn_users = tk.Button(frame_servicios, text="Users", command=abrir_users)
    btn_users.pack(pady=5)

    btn_photos = tk.Button(frame_servicios, text="Photos", command=abrir_photos)
    btn_photos.pack(pady=5)

    btn_comments = tk.Button(frame_servicios, text="Comments", command=abrir_comments)
    btn_comments.pack(pady=5)

    btn_volver_servicios = tk.Button(frame_servicios, text="Volver", command=volver)
    btn_volver_servicios.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Gestión de Contraseñas")
    root.withdraw()  # Ocultar la ventana principal inicial
    mostrar_pantalla_principal()
    root.mainloop()