ALTER TABLE users
ADD correo VARCHAR(255),
    username VARCHAR(25);

SELECT * FROM users

UPDATE users
SET correo = 'admin1@sgta.com', username = 'adminmaster'
WHERE idUser = 1;

UPDATE users
SET correo = 'tecnico1@sgta.com', username = 'tecnicoM'
WHERE idUser = 5;

UPDATE users
SET correo = 'cera@sgta.com', username = 'Cristian Rivera'
WHERE idUser = 6;

UPDATE users
SET correo = 'jllp@sgta.com', username = 'Jorge Pajarito'
WHERE idUser = 7;

delete from users where idUser = 8

-- Cambio de nombre de correo a email
-- 1. Agregar una nueva columna
ALTER TABLE users
ADD mail VARCHAR(255);

-- 2. Copiar los datos de la columna antigua a la nueva
UPDATE users
SET mail = correo;

-- 3. Eliminar la columna antigua
ALTER TABLE users
DROP COLUMN correo;

ALTER TABLE users
ADD photo VARCHAR(25)

UPDATE users
SET photo = 'profileph/jorge.JPG' 
WHERE idUser = 7

UPDATE users
SET photo = 'profileph/cristian.jpg'
WHERE idUser = 6

UPDATE users
SET photo = 'profileph/admin.png'
WHERE idUser=1

UPDATE users 
SET photo = 'profileph/tecnico.png'
WHERE idUser =5

--Alteración de tabla users columna photo para poder generar nombre aleatorio
ALTER TABLE users
ALTER COLUMN photo VARCHAR(100);

SELECT * FROM users ORDER BY idUSer ASC

-- AGREGAR DOCUMENTOS

CREATE TABLE documents
(
	idDoc INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	nameDoc VARCHAR(55),
	pathDoc VARCHAR(100),
	enableDoc BIT
	)

CREATE TABLE documentsTemp
(
	idDoc INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	nameDoc VARCHAR(55),
	pathDoc VARCHAR(100),
	enableDoc BIT
	)