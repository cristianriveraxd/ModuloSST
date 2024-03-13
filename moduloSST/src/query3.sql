-- EN DOCUMENTS SE ENCUENTRAN LOS DOCUMENTOS QUE CREA EL ADMINISTRADOR --

SELECT * FROM documents

SELECT * FROM users ORDER BY idUser ASC

SELECT * FROM users WHERE typeUserId = '2'

-- Tabla para guardar los trabajos creados o asignados
CREATE TABLE works
(
    idWork INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
    nameTec VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    idUserTec INT NOT NULL,
    idUserSup INT NOT NULL,
    mail VARCHAR(25) NOT NULL,
    nameDoc VARCHAR(55),
    pathDoc VARCHAR(100),
    enableWork BIT,
	FOREIGN KEY (idUserSup) REFERENCES users(idUser)
)

--No es neceario lastname, con id es suficiente
ALTER TABLE works
DROP COLUMN nameTec

--Se agregan dos controles, checkSup cuando el supervisor da el okey, workDone cual el trabajo se ha realizado
ALTER TABLE works
ADD checkSup BIT,
	workDone BIT

ALTER TABLE works
ADD	typeWork VARCHAR(25),
	ubicacion VARCHAR(25),
	dateWork DATE

ALTER TABLE works
DROP COLUMN mail

SELECT * FROM works

--15,