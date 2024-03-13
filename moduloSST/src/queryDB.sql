CREATE DATABASE DB_MODULO;

CREATE TABLE users 
(
	idUser INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
	name VARCHAR(50) NOT NULL,
	lastname VARCHAR(50) NOT NULL,
	password CHAR(102) NOT NULL,
	typeUserId INT NOT NULL,
	)

CREATE TABLE typeUsers 
(
	idtypeUser INT PRIMARY KEY NOT NULL,
	typeUser INT,
	rol VARCHAR(20)
	)

ALTER TABLE users
ADD CONSTRAINT FK_typeUser_typeUserId
FOREIGN KEY(typeUserId) REFERENCES
typeUsers(idTypeUser)


INSERT INTO typeUsers (idtypeUser,typeUser,rol) values (1, 1, 'Administrador')
INSERT INTO typeUsers (idtypeUser,typeUser,rol) values (2,2, 'Supervisor')
INSERT INTO typeUsers (idtypeUser,typeUser,rol)	values (3,3, 'Tecnico')

SELECT * FROM typeUsers

SELECT * FROM users