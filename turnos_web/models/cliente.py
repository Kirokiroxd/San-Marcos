from database import conectar

def insertar_cliente(nombre, cedula, telefono, correo):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO clientes (nombre, cedula, telefono, correo) VALUES (%s, %s, %s, %s)"
    valores = (nombre, cedula, telefono, correo)
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()
