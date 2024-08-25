import pymysql

class DAOtraking:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_app" )

    def read_traking(self, id):
        con = DAOtraking.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM traking order by id asc")
            else:
                cursor.execute("SELECT * FROM traking where id = %s order by id asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


    def insert_traking(self,data):
        con = DAOtraking.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO traking(vehicle_type,color,id_camera,fecha_comienzo,id_usuario) VALUES(%s, %s, %s, %s, %s)", (data['vehicle_type'],data['color'],data['id_camera'],data['fecha_comienzo'],data['id_usuario'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def update_traking(self, id, data):
        con = DAOtraking.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE traking set vehicle_type = %s, color = %s, id_camera = %s, fecha_comienzo = %s, id_usuario = %s where id = %s",  (data['vehicle_type'],data['color'],data['id_camera'],data['fecha_comienzo'],data['id_usuario'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()

    def delete_traking(self, id):
        con = DAOtraking.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM traking where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()