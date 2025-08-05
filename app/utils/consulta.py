from app.db import get_connection, release_connection, RealDictCursor
# app/utils/consulta.py
def consulta_general(entidad):
    conn= get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(f"SELECT * FROM {entidad};")
            resultados = cursor.fetchall()
            return resultados
    except Exception as e:
        print(f"Error al obtener datos de {entidad}:", e)
        return []
    finally:
        release_connection(conn)

def consulta_por_condicion(entidad, condicion, valor):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            query = f"SELECT * FROM {entidad} WHERE {condicion} = %s;"
            cursor.execute(query, (valor,))
            resultados = cursor.fetchall()
            return resultados
    except Exception as e:
        print(f"Error al obtener datos de {entidad} por {condicion}:", e)
        return []
    finally:
        release_connection(conn)

if __name__ == "__main__":
    #resultados = consulta_general("producto")
    resultados = consulta_por_condicion("sesion_caja", "id", 1)
    print(resultados)