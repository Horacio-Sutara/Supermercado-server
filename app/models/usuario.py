from app.db import get_connection, release_connection, RealDictCursor

# app/models/usuario.py
def obtener_usuarios():
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM usuario;")
            productos = cursor.fetchall()
            return productos
    except Exception as e:
        print("Error al obtener productos:", e)
        return []
    finally:
        release_connection(conn)
if __name__ == "__main__":
    usuarios = obtener_usuarios()
    for usuario in usuarios:
        for clave,valor in usuario.items():
            print(f"{clave}: {valor}")