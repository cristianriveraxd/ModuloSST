import pyodbc
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user 
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from flask_wtf import CSRFProtect
import os 

from conect import Conexion
# models
from models.modelUser import ModelUser
# entities
from models.entities.user import User
#controller
from controller import *

#variables para cargue de archivo
UPLOAD_FOLDER = 'src/forms'
UPLOAD_FOLDER_WORKS = 'src/formsworks'
ALLOWED_EXTENSIONS = {'docx', 'pdf'}

# se instancia flask
app = Flask(__name__)
app.static_folder = 'static'
csrf = CSRFProtect()
db = Conexion()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER_WORKS'] = UPLOAD_FOLDER_WORKS

loginManagerapp = LoginManager(app)
loginManagerapp.login_view = "login"  # Definir la vista de inicio de sesión.

@loginManagerapp.user_loader
def load_user(id):
    return ModelUser.getId(db, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

#Metodo de logica logín
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('validación de datos')
        print(request.form['username'])
        print(request.form['password'])
        user = User(0, request.form['username'], request.form['password'])
        loggedUser = ModelUser.login(db, user)
        if loggedUser:
            if loggedUser.password:
                login_user(loggedUser)
                return redirect(url_for("home"))
            else:
                flash("Contraseña incorrecta")
                print("Contraseña incorrecta")
        else:
            flash("Usuario no encontrado")
            print("Usuario no encontrado")
    return render_template('index.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/home')
@login_required
def home():
    user_id = current_user.id
    try:
        cursor = db.connection.cursor()
        sql = "SELECT username, name, lastname, typeUserID, mail, photo FROM users WHERE idUser = {}".format(user_id)
        cursor.execute(sql)
        row=cursor.fetchone()
        print ("ejecución de id exitosa:", row[0], row[1], row[2], row[3], row[4], row[5], user_id)
    except Exception as e:
        raise Exception(e)
    
    print ("Valor de user_id:", user_id) 
    return render_template('home.html', username=row[0], name=row[1], lastname=row[2], typeUserId=row[3], mail=row[4],photo=row[5], idUser=user_id)

#metodo para listar usuarios
@app.route('/crudUsuarios', methods=['GET','POST'])
@login_required
def crudUsuarios():
    return render_template('layout.html', data = listarUsuarios())

#ruta para crear documentos por parte del administrador
@app.route('/createDocuments', methods = ['GET','POST'])
@login_required
def createDocuments():
    return render_template('uploadsForms.html')

#ruta para crear trabajos por parte del tecnico y supervisor
@app.route('/createWork/<int:idUser>/<int:typeUserId>', methods = ['GET','POST'])
@login_required
def createWork(idUser, typeUserId):
    if request.method == 'GET' and typeUserId == 3:
        data = updateUser(idUser) #updateUser (para listar el usuario)
        lista =listarSupervisores()
        if data:
            return render_template('createWork.html', dataTecnico = data, dataSupervisor = lista, idUser = idUser,
                                   typeUserId = typeUserId)
    elif request.method == 'GET' and typeUserId == 2: #si es supervisor
        data = updateUser(idUser)
        lista = listarTecnicos()
        if data:
            return render_template('createWork.html', dataSuper = data, dataTec = lista, idUser = idUser,
                                   typeUserId = typeUserId)
    else:
        return  redirect(url_for('home', msg = 'No se pudo acceder a la ruta')) 

#metodo para crear trabajo en DB
#metodo en controler para regristar en base de datos <PDTE CAMBIO DE NOMBRE DOCUMENTO>
@app.route('/create-work/<int:idUser>/<int:typeUserId>', methods=['POST'])   
@login_required
def formCreateWork(idUser, typeUserId):
    if request.method == 'POST':
        typework = request.form['typework']
        ubication = request.form['ubication']
        date = request.form['date']
         #metodo de captura de archivo
        if 'file' not in request.files:
            flash('No file part')
            print ('No existe el archivo')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            print('No seleccionado archivo')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Asegurar el nombre del archivo
            file.save(os.path.join(app.config['UPLOAD_FOLDER_WORKS'], filename))
            
            #AGREGAR EN ESTE ESPACIO FUNCION DE CAMBIAR NOMBRE
            nameDoc = filename
            pathDoc = 'formsworks/' + filename
               
        if typeUserId == 3:
            idsupervisor = request.form['supervisor']
            varCert=createWorksTecn(idUser, idsupervisor, 1, typework, ubication, date, nameDoc, pathDoc)
            
            if(varCert):
                flash (f'Cargue con exito de documento {filename}')
                return redirect(url_for('home', msg = f'Documento creado con exito file{filename}', tipo=1))
            
        elif typeUserId == 2:
            idtecnico = request.form['tecnico']
            varCert= createWorksSup(idUser, idtecnico, 1, typework, ubication, date, nameDoc, pathDoc)
            
            if(varCert):
                flash (f'Cargue con exito de documento {filename}')
                return redirect(url_for('home', msg = 'Asignación con exito', tipo=1))
        else: 
            return  redirect(url_for('home', msg = 'No se pudo crear el documento de trabajo'))
    
#ruta para visualizar trabajos       
@app.route('/documentsCreated/<int:idUser>/<int:typeUserId>', methods = ['GET', 'POST'])
@login_required
def documentsCreated(idUser, typeUserId):
    #entrando con tecnico a listardocumentos creados
    if request.method == 'GET' and typeUserId == 3:
        data = listarSupervisores() 
        dataWorks = listarTrabajosCreadosTec(idUser)
        
        if data and dataWorks:
            return render_template('documentsCreatedTec.html', data = data, dataWorks = dataWorks)
        
        else:
            return render_template('documentsCreatedTec.html')
    #entrando con supervisor a listardocumentos asignados 
    elif request.method == 'GET' and typeUserId == 2:
        data = listarTecnicos()
        dataWorks = listarTrabajosCreadosSup(idUser)
        
        if data and dataWorks:
             return render_template('documentsCreatedSup.html', data = data, dataWorks = dataWorks)
        
        else:
            return render_template('documentsCreatedSup.html')

#ruta para generar PQRS sobre el aplicativo
@app.route('/generate_pqrs/<int:idUser>', methods = ['GET'])
@login_required
def generate_pqrs(idUser):
        data = detallesdelusuario(idUser)
        if (data):
            return render_template('generatePQRS.html', infoUsuario = data, idUser = idUser)
        else:
             return render_template('actions/layout.html', msg='Se genero un error en la data', tipo=1)

@app.route('/formCreatePQRS/<int:idUser>', methods = ['GET', 'POST'])
@login_required
def formCreatePQRS(idUser):
    if request.method == 'POST':
        return True
    
#metodo para ver detalles del usuario
#cuando recibe un get, llama a detalles del usuario (metodo controller) y recibe un query
#pasando a llamar a vista para abrir detalles de usuario
@app.route('/ver-detalles-del-usuario/<int:idUser>', methods=['GET', 'POST'])
@login_required
def viewDetalleUser (idUser):
    msg =''
    if request.method == 'GET':
        data = detallesdelusuario(idUser) #Función de detalles de usuario
        
        if data:
            return render_template('actions/view.html', infoUsuario = data, msg='Detalles del usuario', tipo=1)
        else:
            return render_template('actions/layout.html', msg='No existe el Usuario', tipo=1)

#metodo para actualizar usuario
#realiza una consulta al metodo updateUser (metodo controller) recibiendo un query
#llama a la vista update para ir a ventana de actualizar
#update utiliza el metodo siguiente formUpdtadeUser para logica en BD 
@app.route('/form-update-user/<string:idUser>', methods=['GET','POST'])
@login_required
def formViewUpdate(idUser):
    if request.method == 'GET':
        data = updateUser(idUser)
        if data:
            return render_template('actions/update.html',  dataInfo = data)
        else:
            return render_template('layout.html', data = listarUsuarios(), msg='No existe el usuario', tipo= 1)
    else:
        return render_template('layout.html', data = listarUsuarios(), msg = 'Metodo HTTP incorrecto', tipo=1)   
    
#metodo de captura de datos del formulario updates para cargue a BD
#metodo getUpdates realiza logica con BD para actualizar registros
@app.route('/update-user/<string:idUser>', methods=['POST'])
@login_required
def  formUpdateUser(idUser):
    if request.method == 'POST':
        name = request.form['nombre']
        lastname = request.form['apellido']
        typeUserId = request.form['typeUserId']
        email = request.form['email']
        username = request.form['username']
        newphoto = request.form['modificar_foto']
        #Script para recibir el archivo (foto)
        if(newphoto=='Y' and request.files['photo']):
            file     = request.files['photo']
            fotoForm = recibeFoto(file)
            photo = 'profileph/' + fotoForm
            resultData = getUpdates(name, lastname, typeUserId, username, email, photo, idUser)
            
        elif(newphoto=='N'):
            resultData = getUpdates2(name, lastname, typeUserId, username, email, idUser)

        if(resultData):
            return  redirect(url_for('home', msg = 'Datos del usuario actualizados', tipo=1))
        else:
            return  redirect(url_for('home', msg = 'No se pudo actualizar el usuario', tipo=1))

# función llamada recibeFoto que toma un argumento llamado file. 
def recibeFoto(file):
    print(file)
    basepath = os.path.dirname (__file__) #La ruta donde se encuentra el archivo actual
    filename = secure_filename(file.filename) #Nombre original del archivo

    #capturando extensión del archivo ejemplo: (.png, .jpg, .pdf ...etc)
    # os.path.splitext para dividir el nombre del archivo (filename) en su raíz y su extensión. La extensión del archivo se almacena en la variable extension.
    extension           = os.path.splitext(filename)[1]
    nuevoNombreFile     = stringAleatorio() + extension
    #print(nuevoNombreFile)
        
    upload_path = os.path.join (basepath, 'static\profileph', nuevoNombreFile) 
    file.save(upload_path)

    return nuevoNombreFile

#metodo para eliminar usuario
@app.route('/form-delete-user/<string:idUser>', methods=['GET', 'POST'])
@login_required
def formViewDelete(idUser):
    if request.method == 'GET':
        data = detallesdelusuario(idUser)
        delete = deleteUser(idUser, data)
        
        
        if delete:
            return redirect(url_for('home',msg='Usuario eliminado con éxito', tipo=1))
        else:
            return redirect(url_for('home',msg='Ha ocurrido un error intentanto eliminar el usuario', tipo=1))

    # Si la solicitud no es POST, puedes manejarla según tus necesidades
    # Por ejemplo, puedes redirigir a otra página o renderizar un formulario GET.
    # Aquí simplemente renderizamos un mensaje de advertencia.
    return redirect(url_for('crudUsuarios',msg='XXXXXXX', tipo=1))
     
#metodo para el registro de usuarios PEDN
@app.route('/registrarUsuarios', methods=['GET','POST'],  endpoint='addUser')
@login_required
def addUser():
    return render_template('actions/add.html')

#Registrando nuevo usuario
@app.route('/usuario', methods=['POST'])
@login_required
def formAddUser():
    if request.method == 'POST':
        name = request.form['name']
        lastname = request.form['lastname']
        username  = request.form['username']
        mail = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password)
        typeUserId   = request.form['typeUserId']
        
        if(request.files['photo']):
            file     = request.files['photo']
            fotoForm = recibeFoto(file)
            photo = 'profileph/' + fotoForm
            resultQuery = createUser(name, lastname, hashed_password, typeUserId, username, mail, photo)
        
        if(resultQuery):
            return  redirect(url_for('home', msg = 'Usuario creado', tipo=1))
        else:
            return  redirect(url_for('home', msg = 'No se pudo crear el usuario', tipo=1))
        
#validación de extensiones 
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
 #Cargue de documento x administrador          
@app.route('/upload', methods = ['POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            print ('No existe el archivo')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            print('No seleccionado archivo')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  # Asegurar el nombre del archivo
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
        else:
            flash('Archivo no compatible')
            print ('Archivo no compatible')
            
    return  redirect(url_for('home', msg = 'No se pudo crear el documento')) 
                        
@app.route('/uploads/<filename>')
@login_required
def uploaded_file(filename):
    nameDoc = filename
    pathDoc = 'forms/' + filename
    varDoc=createDocs(nameDoc, pathDoc, 1)
    
    if(varDoc):
        flash (f'Cargue con exito de documento {filename}')
        return redirect(url_for('home', msg = f'Documento creado con exito file{filename}', tipo=1))
  
#funcionalidad offline 
@app.route('/offline', methods=['GET'])
def offline():
    if request.method == 'GET':
        return render_template('offline.html') 

if __name__ == '__main__':
    app.secret_key = 'my_secret_key_123'
    csrf.init_app(app)
    app.run(debug=True)


