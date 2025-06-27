from database import conectar

def insertar_turno(fecha, hora, estado, id_cliente, id_servicio):
    conn = conectar()
    cursor = conn.cursor()
    sql = """
        INSERT INTO turnos (fecha, hora, estado, id_cliente, id_servicio)
        VALUES (%s, %s, %s, %s, %s)
    """
    valores = (fecha, hora, estado, id_cliente, id_servicio)
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()
def obtener_servicios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_servicio, nombre FROM servicios")
    servicios = cursor.fetchall()
    conn.close()
    return servicios

def obtener_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id_cliente, nombre FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes
