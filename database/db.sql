-- Eliminar la base de datos si existe
DROP DATABASE IF EXISTS db_app;

-- Crear una nueva base de datos
CREATE DATABASE db_app;

-- Usar la base de datos recién creada
USE db_app;

-- Crear tabla usuario
CREATE TABLE usuario (
  id_usuario int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  nombres varchar(50) NOT NULL,
  apellidos varchar(50) NOT NULL,
  email varchar(50) NOT NULL UNIQUE,
  password varchar(50) NOT NULL,
  rol varchar(20) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

-- Crear tabla camara
CREATE TABLE camara (
  id_camara int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  camara_id varchar(10) UNIQUE,
  ip varchar(50) NOT NULL,
  ubicacion varchar(70) NOT NULL,
  estado varchar(20)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

-- Crear tabla calle
CREATE TABLE calle (
  id_calle int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  direccion varchar(50) NOT NULL,
  id_camara int,
  CONSTRAINT FK_calle_camara FOREIGN KEY (id_camara) REFERENCES camara(id_camara)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

-- Crear tabla traking
CREATE TABLE traking (
  id_traking int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  vehicle_type varchar(70) NOT NULL,
  color varchar(20) NOT NULL,
  id_camara int,
  fecha_comienzo datetime,
  id_usuario int,
  estado varchar(20) NOT NULL,
  CONSTRAINT FK_traking_camara FOREIGN KEY (id_camara) REFERENCES camara(id_camara),
  CONSTRAINT FK_traking_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

-- Crear tabla traking_regs
CREATE TABLE traking_regs(
  id_traking_reg int(10) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  id_traking int,
  id_calle int,
  fecha datetime,
  CONSTRAINT FK_traking_regs_trakings FOREIGN KEY (id_traking) REFERENCES traking(id_traking),
  CONSTRAINT FK_traking_regs_calle FOREIGN KEY (id_calle) REFERENCES calle(id_calle)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;

-- Crear trigger para generar camara_id
DELIMITER //

CREATE TRIGGER before_insert_camara
BEFORE INSERT ON camara
FOR EACH ROW
BEGIN
  DECLARE next_id INT;
  -- Obtener el siguiente valor de AUTO_INCREMENT
  SET next_id = (SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA=DATABASE() AND TABLE_NAME='camara');
  -- Generar el camara_id basado en el siguiente valor de AUTO_INCREMENT
  SET NEW.camara_id = CONCAT('CAM', LPAD(next_id, 3, '0'));
END;
//

DELIMITER ;
DELIMITER ;

INSERT INTO camara (ip, ubicacion, estado) VALUES ('rtsp://192.168.57.247:8080/h264.sdp', 'AVENIDA A', 'Active');
INSERT INTO camara (ip, ubicacion, estado) VALUES ('rtsp://192.168.57.121:8080/h264.sdp', 'AVENIDA B', 'Active');
INSERT INTO camara (ip, ubicacion, estado) VALUES ('rtsp://192.168.57.135:8080/h264.sdp', 'AVENIDA C', 'Active');
INSERT INTO camara (ip, ubicacion, estado) VALUES ('rtsp://192.168.0.10:8080/h264.sdp', 'AVENIDA D', 'Active');
INSERT INTO camara (ip, ubicacion, estado) VALUES ('rtsp://192.168.0.17:8080/h264.sdp', 'AVENIDA E', 'Active');
