drop database db_app;

create database db_app;

use db_app;

CREATE TABLE usuario (
  id_usuario int(10) NOT NULL primary key auto_increment,
  nombres varchar(50) NOT NULL,
  apellidos varchar(50) NOT NULL,
  email varchar(50) NOT NULL,
  password varchar(50) NOT NULL,
  rol varchar(20) NOT NULL

) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE camara (
  id_camara int(10) NOT NULL primary key auto_increment,
  ip varchar(50) NOT NULL,
  ubicacion varchar(70) NOT NULL,
  estado varchar(20)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;



CREATE TABLE calle (
  id_calle int(10) NOT NULL primary key auto_increment,
  direccion varchar(50) NOT NULL,
  id_camara int constraint FK_calle_camara foreign key references camara(id_camara),
  
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE traking (
  id_traking int(10) NOT NULL primary key auto_increment,
  vehicle_type varchar(70) NOT NULL,
  color varchar(20) NOT NULL,
  id_camara int constraint FK_traking_camara foreign key references camara(id_camara),
  fecha_comienzo datetime,
  id_usuario int constraint FK_traking_usuario foreign key references usuario(id_usuario),
  estado varchar(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

CREATE TABLE traking_regs(
  id_traking_reg int(10) NOT NULL primary key auto_increment,
  id_traking int constraint FK_traking_regs_trakings foreign key references traking(id_traking),
  id_calle int constraint FK_traking_regs_calle foreign key references calle(id_calle),
  fecha datetime
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;



