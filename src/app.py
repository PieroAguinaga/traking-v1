"""."""
from flask import Flask, flash, render_template, redirect, url_for, request, Response
import ComputerVision
from datetime import datetime

from dao.DAOusuario import DAOusuario
from dao.DAOcamara import DAOcamara
from dao.DAOtraking_regs import DAOtraking_regs
from dao.DAOcalle import DAOcalle
from dao.DAOtraking import DAOtraking

app = Flask(__name__)
app.secret_key = "s3cr3tk3y"

db_usuario = DAOusuario()
db_camara = DAOcamara()
db_traking_regs = DAOtraking_regs()
db_calle= DAOcalle()
db_traking= DAOtraking()

@app.route('/')
def login():
    """."""
    return render_template('login.html')

@app.route('/loginver', methods = ['POST'])
def loginver():
    """."""
    data = db_usuario.read_usuario(request.form['email'])

    if len(data) != 0:
        if request.form['password'] == data['password']:
            return redirect(url_for('index'), usuario_datos=data)
        flash("Contraseña incorrecta")
        return render_template('login.html')
    flash("Usuario incorrecto")
    return render_template('login.html')

@app.route('/inicio')
def inicio():
    """."""
    # leer valores de las camaras
    camara_datos = db_camara.read_camara()
    return render_template('index.html', camara_datos = camara_datos, detected_colors_hex = ComputerVision.detected_colors_hex)

@app.route('/video_feed/<int:camera_id>')
def video_feed(camera_id):
    """."""
    camera_rstp = db_camara.read_camara(camera_id)[0][2]
    if camera_rstp:
        return Response(ComputerVision.DetectionAndDisplay(camera_rstp), mimetype='multipart/x-mixed-replace; boundary=frame')
    return "Camera not found", 404

@app.route('/userconfig')
def userconfig():
    """."""
    return render_template('userconfig.html')

@app.route('/trakingconfig')
def trakingconfig():
    """."""
    return render_template('trakingconfig.html')

@app.route('/watchtraking')
def watchtraking():
    """."""
    return render_template('watchtraking.html')

@app.route('/mytrakings')
def mytrakings():
    """."""
    tracking_data = db_traking.read_traking(None)
    return render_template('mytrakings.html', tracking_data = tracking_data)

@app.route('/start_tracking', methods=['POST'])
def start_tracking():
    color = request.form.get('color')
    vehicle_type = "Vehiculo"
    camera_id = request.form.get('camera_id')
    user_id = "1"
    start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = "Activo"
    tracking_data = {'vehicle_type': vehicle_type,'color': color,'id_camera': camera_id,'fecha_comienzo': start_time ,'id_usuario': user_id, 'estado': status}
    db_traking.insert_traking(tracking_data)
    return redirect(url_for('mytrakings'))

@app.route('/trakingrecord')
def trakingrecord():
    """."""
    return render_template('trakingrecord.html')

@app.route('/prueba')
def pruebas():
    """."""
    return render_template('table.html')


@app.errorhandler(404)
def page_not_found(error):
    """."""
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)
