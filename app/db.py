from psycopg2 import pool
from psycopg2.extras import RealDictCursor
import config

# app/db.py
# Configuración del pool de conexiones
try:
    connection_pool = pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        dbname=config.DB_NAME,
        user=config.DB_USER,
        password=config.DB_PASSWORD,
        host=config.DB_HOST,
        port=config.DB_PORT
    )
    print("Pool de conexiones creado con éxito.")
except Exception as e:
    print("Error al crear el pool de conexiones:", e)
    exit()

## Funciones para obtener y liberar conexiones del pool
def get_connection():
    return connection_pool.getconn()

def release_connection(conn):
    connection_pool.putconn(conn)
