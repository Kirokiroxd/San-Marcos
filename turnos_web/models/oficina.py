from database import conectar

def obtener_oficinas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM oficinas")
    oficinas = cursor.fetchall()
    conn.close()
    return oficinas
