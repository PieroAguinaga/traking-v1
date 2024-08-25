import pymysql

class DAOcalle:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_app" )

    def read_calle(self, id):
        con = DAOcalle.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM calle order by id asc")
            else:
                cursor.execute("SELECT * FROM calle where id = %s order by id asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


    def insert_calle(self,data):
        con = DAOcalle.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO calle(direccion,id_camara) VALUES(%s, %s)", (data['direccion'],data['id_camara'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()




    def update_calle(self, id, data):
        con = DAOcalle.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE calle set direccion = %s, id_camara = %s where id = %s",  (data['direccion'],data['id_camara'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def delete_calle(self, id):
        con = DAOcalle.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM calle where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()





