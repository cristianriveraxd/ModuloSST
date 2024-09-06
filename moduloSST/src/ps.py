import os
import pyodbc
from werkzeug.security import generate_password_hash
import uuid

# Función para generar un nuevo usuario
def create_user(name, lastname, password, typeUserId, username, mail, photo):
    # Generar un id único para el usuario
    idUser = str(uuid.uuid4())
    
    # Generar el hash de la contraseña
    hashed_password = generate_password_hash(password)
    
    # Conexión a la base de datos (Asegúrate de modificar con tus credenciales)
    connection_string = (
        "DRIVER={SQL Server};"
        "SERVER=CRISTIAN\\SQLEXPRESS01;"
        "DATABASE=DB_MODULO;"
        "Trusted_Connection=yes"
    )
    
    try:
        # Conectar a la base de datos
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # Insertar el nuevo usuario en la base de datos
        insert_query = """
        INSERT INTO Users ( name, lastname, password, typeUserId, username, mail, photo)
        VALUES ( ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(insert_query, ( name, lastname, hashed_password, typeUserId, username, mail, photo))
        
        # Confirmar los cambios
        conn.commit()
        print("Usuario creado exitosamente")
    
    except Exception as e:
        print(f"Error al crear el usuario: {e}")
    
    finally:
        # Cerrar la conexión
        cursor.close()
        conn.close()

# Ejemplo de uso
if __name__ == '__main__':
    name = "tecnico"
    lastname = "Doe"
    password = "tecnico"
    typeUserId = 2
    username = "johndoe"
    mail = "johndoe@example.com"
    photo = "profile_photo.jpg"

    create_user(name, lastname, password, typeUserId, username, mail, photo)
