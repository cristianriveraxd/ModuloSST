# Modulo de gestión de flujos SST

Este desarrollo web consistio en una pagina en la cual se podian cargar documentos como permisos en alturas, en espacios confinados, entre otros... Esto con el fin de agilizar el proceso de autorización de los trabajos pasando el permiso a nivel de usuarios. 

El objetivo de la implementación de este aplicativo web es eliminar el tiempo de recolección de firmas para los permisos necesarios para el trabajo. 


## Desarrollo 
El desarrollo web se realizo con Flask para el back-end de la pagina, bootstrap para el front-end del aplicativo, librerias de python para el manejo de la documentación y MySqlServer como base de datos de usuarios, estados y rutas de documentación.

Esta aplicacipon esta desarrollado con protección contra ataques de inyección sql, uso de tokens de sesión y jerarquia a nivel de usuarios. 

## Instalación 

1) Clone este repositorio
2) Corra la aplicación bajo un entorno virtual. Abra su terminal desde la carpeta y ejecute:
```bash
  --Creación de entorno virtual
  python -m venv .venv

  --Activación de entorno virtual
  .venv\Scripts\activate
```
3) Instale las dependencias necesarias para ejecutar el proyecto ubicandose en la carpeta del modulo.

```bash
  pip install -r requirements.txt
```
4) Ejecute el archivo **scriptDB** mysql en su servidor mysql para poder crear la base de datos necesaria.
5) Una vez creada la base de datos con las tablas correspondientes modifique el archivo **conect.py** con sus credenciales para garantizar la conexión entre el aplicativo y la base de datos.
5) Modifique el archivo ps.py en la linea 48 la variable name, creando el usuario que desee y asignandole una contraseña en la linea 50, adicional agregue que tipo de usuario es:

-1 Administrador
-2 Supervisor
-3 Tecnico

```bash
 # Ejemplo de uso
if __name__ == '__main__':
    name = "tecnico"     #Linea a modificar
    lastname = "Doe"
    password = "tecnico" #Linea a modificar
    typeUserId = 2       #Linea a modificar
    username = "johndoe"
    mail = "johndoe@example.com"
    photo = "profile_photo.jpg"
```
Esto con el fin de crear los usuarios en la base de datos y crearle un hash a su contraseña

![image](https://github.com/user-attachments/assets/70f56a12-991d-4b80-ba2d-b34a9e1d7281)

6) Corra el archivo ps.py a través de la consola para poder crear los usuarios correspondientes y asi poder hacer uso del aplicativo

```bash
  python ps.py
```

7) Una vez realizados los anteriores pasos ejecute la app. Esta le creara una versión en debug para pruebas y ajustes.

```bash
  python app.py
```

## Ejecucción 

El aplicativo siempre solicita credenciales para asi mismo servir a nivel de usurios:

![image](https://github.com/user-attachments/assets/135d26a9-f6cc-43d2-83d3-de1af6cf6b8a)

El aplicativo detecta si hay usuarios existentes, contraseñas errones y redirije a los usuarios por su nivel.

### Nivel Administrador
Este nivel de administración del aplicativo web. 

![image](https://github.com/user-attachments/assets/d4b972b3-ef97-4372-905b-4a040df3e051)

Permite crear documentos de trabajo, los cuales podran descargar los tecnicos y supervisores.

![image](https://github.com/user-attachments/assets/e0992288-83f1-4c9a-a446-0aef10daf504)

Permite crear, actualizar, ver y borrar usuarios del aplicativo:

![image](https://github.com/user-attachments/assets/3ef7092c-2db9-4421-be52-ce868bb5bd96)

En futuras actualizaciones se agregara una bandeja de tareas para el administrador

### Nivel Supervisor

En este nivel el supervisor puede crear trabajos y asignarlos a los tecnicos disponibles, generar PQRS para ser atentidas y autorizar trabajos solicitados por los tecnicos.

![image](https://github.com/user-attachments/assets/02a715b7-3545-498a-8c61-2ce1c2212e9f)

La interfaz entre usuarios es la misma, solo se habilitan funcionalidades a nivel de jerarquia.

A medida que se asignen los trabajos se realiza el control del flujo de los mismos.

![WORKS](https://github.com/user-attachments/assets/0cc7aadf-4710-4038-988c-f3a03460a347)



