from app.Model.connection import get_connection

#Funcion para crear un usuario nuevo
def crear_usuario(nombre):
    conn = get_connection()
    with conn.cursor() as cur:

        query = """
        INSERT INTO users (nombre, fecha_registro)
        VALUES (%s, NOW())
        RETURNING id;
        """

        cur.execute(query, (nombre,))
        id_usuario = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return id_usuario

#Funcion para obtener un usuario por su id
def obtener_usuario_por_nombre(nombre):
    conn = get_connection()
    with conn.cursor()as cur:
        query = """
        SELECT *
        FROM users
        WHERE nombre = %s;
        """
        
        cur.execute(query, (nombre,))
        resultado = cur.fetchone()
        conn.close()
        return resultado