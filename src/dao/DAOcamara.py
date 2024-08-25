import pymysql

class DAOcamara:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_app" )

    def read_camara(self, id):
        con = DAOcamara.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM camara order by id asc")
            else:
                cursor.execute("SELECT * FROM camara where id = %s order by id asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


    def insert_camara(self,data):
        con = DAOcamara.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO camara(ip,ubicacion) VALUES(%s, %s)", (data['ip'],data['ubicacion'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()




    def update_camara(self, id, data):
        con = DAOcamara.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE camara set ip = %s, ubicacion = %s, estado = %s where id = %s",  (data['ip'],data['ubicacion'],data['estado'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def delete_camara(self, id):
        con = DAOcamara.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM camara where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()