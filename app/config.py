import os
from dotenv import load_dotenv

load_dotenv()  # carga variables desde .env automáticamente

DB_NAME = os.getenv("DB_NAME", "Supermercado")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
