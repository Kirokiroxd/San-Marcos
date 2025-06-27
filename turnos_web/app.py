from flask import Flask, render_template, request, redirect, url_for
from models.turno import insertar_turno, obtener_servicios, obtener_clientes
from models.cliente import insertar_cliente
from models.oficina import obtener_oficinas

app = Flask(__name__)

@app.route('/')
def inicio():
    oficinas = obtener_oficinas()
    return render_template('index.html', oficinas=oficinas)

@app.route('/registrar_turno', methods=['GET', 'POST'])
def registrar_turno():
    if request.method == 'POST':
        fecha = request.form['fecha']
        hora = request.form['hora']
        id_cliente = request.form['id_cliente']
        id_servicio = request.form['id_servicio']
        insertar_turno(fecha, hora, 'Pendiente', id_cliente, id_servicio)
        return redirect(url_for('inicio'))
    
    servicios = obtener_servicios()
    clientes = obtener_clientes()
    return render_template('registro_turno.html', servicios=servicios, clientes=clientes)

@app.route('/registrar_cliente', methods=['GET', 'POST'])
def registrar_cliente():
    if request.method == 'POST':
        nombre = request.form['nombre']
        cedula = request.form['cedula']
        telefono = request.form['telefono']
        correo = request.form['correo']
        insertar_cliente(nombre, cedula, telefono, correo)
        return redirect(url_for('inicio'))
    
    return render_template('registro_cliente.html')

if __name__ == '__main__':
    app.run(debug=True)
