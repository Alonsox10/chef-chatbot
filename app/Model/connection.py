import psycopg 
from dotenv import load_dotenv
import os
from fastapi import HTTPException


load_dotenv()

def get_connection():
    try:
        conn = psycopg.connect(
            host = os.getenv("DB_HOST"),
            port = os.getenv("DB_PORT"),
            dbname = os.getenv("DB_NAME"),
            user = os.getenv("DB_USER"),
            password = os.getenv("DB_PASSWORD")
        )
        print("Conexion exitosa a la base de datos")
        return conn
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")
    

get_connection()
    

