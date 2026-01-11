import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    print(cur.fetchone())
    cur.close()
    conn.close()
    print("Conexión exitosa")
except Exception as e:
    print("Error:", e)