from app.Model.connection import get_connection

#Funcion para obtener recetas por ingredientes (funcion principal)
def obtener_recetas_por_ingredientes(nombre_ingrediente):
    conn = get_connection()
    with conn.cursor() as cur:

        query = """
            SELECT r.id_receta, r.nombre
            FROM recetas r
            JOIN receta_ingrediente ri ON r.id_receta = ri.id_receta
            JOIN ingredientes i ON ri.id_ingrediente = i.id_ingrediente
            WHERE i.nombre ILIKE %s;
            """
        cur.execute(query, (f"%{nombre_ingrediente}%",))
        resultados = cur.fetchall()

        cur.close()
        conn.close()

        return resultados



    


