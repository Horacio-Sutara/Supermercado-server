from app.db import get_connection, release_connection
# app/utils/insert.py

def insertar_datos(entidad,columnas,valores):
    conn= get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                f"INSERT INTO {entidad}({columnas}) VALUES({','.join(['%s'] * len(valores))});",valores)
            conn.commit()
            print(f"Datos insertados correctamente en {entidad}.")
    except Exception as e:
        print(f"Error al insertar datos en {entidad}:", e)
        conn.rollback()
    finally:
        release_connection(conn)

if __name__ == "__main__":
    # Ejemplo de uso
    entidad = "usuario"
    columnas = "nombre, apellido, dni, telefono, rol, activo, contraseña, correo"
    valores = ("Juan", "Pérez", "12345678", "1234567890", "USER", "1", "contraseña123", "juan@example.com")
    insertar_datos(entidad, columnas, valores)
