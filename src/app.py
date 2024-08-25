
#Librerías y comandos
from flask import Flask, flash, render_template, redirect, url_for, request, session
import requests
import json


from dao.DAOusuario import DAOusuario
from dao.DAOcamara import DAOcamara
from dao.DAOtraking_regs import DAOtraking_regs
from dao.DAOcalle import DAOcalle
from dao.DAOtraking import DAOtraking


#Variables

url_computer_vision_app=" https://123.123.4.1"

app = Flask(__name__)

#Bases de datos 
db_usuario = DAOusuario()
db_camara = DAOcamara()
db_traking_regs = DAOtraking_regs()
db_calle= DAOcalle()
db_traking= DAOtraking()

#API que comunica aplicación de computer vision

#response = requests.get(url_computer_vision_app)
#if response.status_code==200:
 #           lista = response.json()
  #          vehiculos_cv=lista.get('vehiculos_cv',[])

          




@app.route('/')
def login():

    return render_template('login.html')

@app.route('/loginver', methods = ['POST'])
def loginver():
    data = db_usuario.read_usuario(request.form['email'])

    if len(data) != 0:
        
        if request.form['password'] == data['password']:
            return redirect(url_for('index'),usuario_datos=data)
        
        else:
            flash("Contraseña incorrecta")
            return render_template('login.html')
        
    else:
        flash("Usuario incorrecto")
    
    return render_template('login.html')




@app.route('/inicio')
def index():
    #camara_datos = db_camara.read_camara()
    camara_datos=[]

    return render_template('index.html', camara_datos = camara_datos)



@app.route('/userconfig')
def userconfig():
    return render_template('userconfig.html')

@app.route('/trakingconfig')
def trakingconfig():
    return render_template('trakingconfig.html')

@app.route('/watchtraking')
def watchtraking():
    return render_template('watchtraking.html')

@app.route('/mytrakings')
def mytrakings():
    return render_template('mytrakings.html')

@app.route('/trakingrecord')
def trakingrecord():
    return render_template('trakingrecord.html')

@app.route('/prueba')
def pruebas():
    return render_template('table.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0",debug=True)    
