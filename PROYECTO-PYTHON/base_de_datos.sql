CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios(
id         int(255) AUTO_INCREMENT NOT NULL,
nombres    varchar(100) ,
apellidos  varchar(200) ,
email      varchar(50) not null,
password   varchar(255) not null,
fecha      date not null,
CONSTRAINT pk_usuarios PRIMARY KEY(id),
CONSTRAINT up_email UNIQUE(email),
)ENGINE=InnoDB;

"""LAS CONSTRAINT son rescricciones que le pones a tu tabla como tienes 
que ponerle una PRIMARY KEY() que es para poder relacionar los valores
tambien la up UNIQUE que quiere decir q un valor es unico es decir
que te guarda que un usuario se resgristre con un solo correo,,
luego esta el ENGENE=InnoDB; eso es para poder relacionar las tablas"""

CREATE TABLE notas(
id           int(25) AUTO_INCREMENT not null,
usuario_id   int(25) not null,
titulo       varchar(255) not null,
descripcion  MEDIUMTEXT,
fecha        date not null,
CONSTRAINT pk_notas PRIMARY KEY(id),
CONSTRAINT fk_notas_usuario FOREIGN KEY(usuario_id) REFERENCES usuario(id)
)ENGINE=InnoDB;
 