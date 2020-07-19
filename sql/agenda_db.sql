CREATE DATABASE IF NOT EXISTS escuela;
USE escuela;
SELECT DATABASE();

DROP TABLE IF EXISTS alumnos;
CREATE TABLE IF NOT EXISTS alumnos(
id_alumno	     		INT(4)          	NOT NULL        AUTO_INCREMENT          PRIMARY KEY,
matricula               CHAR(10)     		NOT NULL,
nombre           		VARCHAR(30)    		NOT NULL,
apellido_paterno		VARCHAR(20)			NOT NULL,
apellido_materno        VARCHAR(20)         NOT NULL,
edad					CHAR(2)				NOT NULL,
fecha_nacimiento		DATE,
sexo					CHAR(10)			NOT NULL,
estado_civil			CHAR(10)			NOT NULL
)ENGINE= InnoDB DEFAULT CHARSET=latin1;

/*INSERCION DE DOS ALUMNOS*/
INSERT INTO alumnos(id_alumno, matricula, nombre, apellido_paterno, apellido_materno, edad, fecha_nacimiento, sexo, estado_civil) VALUES 
(NULL, '1718110399', 'Diana Marlen', 'Meneses', 'Alegria', '20', '2000/03/12', 'Femenino', 'Soltera');

INSERT INTO alumnos(id_alumno, matricula, nombre, apellido_paterno, apellido_materno, edad, fecha_nacimiento, sexo, estado_civil) VALUES 
(NULL, '1718110300', 'Dania Jimena', 'Meneses', 'Alegria', '17', '2002/11/01', 'Femenino', 'Soltera');

