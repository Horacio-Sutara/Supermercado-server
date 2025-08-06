from app.db import get_connection, release_connection, RealDictCursor
# app/utils/update.py

def actualizar_datos(entidad, columnas, valores, condicion):
    conn= get_connection()
    try:
        with conn.cursor() as cursor:
            query= f"UPDATE {entidad} SET {', '.join([f'{col} = %s' for col in columnas])} WHERE {condicion};"
            cursor.execute(query, valores)
            conn.commit()

    except Exception as e:
        print(f"Error al actualizar datos: {e}")
    finally:
        release_connection(conn)

if __name__ == "__main__":
    # Ejemplo de uso
    entidad = "usuario"
    columnas = ["id"]
    valores = ("4")
    condicion = "id = 7"
    actualizar_datos(entidad, columnas, valores, condicion)
    print("Datos actualizados correctamente.")