import pymysql

class DAOusuario:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_app" )

    def read_usuario(self, id):
        con = DAOusuario.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM usuario order by id_usuario asc")
            else:
                cursor.execute("SELECT * FROM usuario where email = %s order by email asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


    def insert_usuario(self,data):
        con = DAOusuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO usuario(nombres,apellidos,email,password,rol) VALUES(%s, %s, %s, %s, %s)", (data['nombres'],data['apellidos'],data['email'],data['password'],data['rol'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def update_usuario(self, id, data):
        con = DAOusuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE usuario set nombres = %s, apellidos = %s, email = %s, password = %s, rol = %s where id = %s",  (data['nombres'],data['apellidos'],data['email'],data['password'],data['rol'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete_usuario(self, id):
        con = DAOusuario.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM usuario where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()