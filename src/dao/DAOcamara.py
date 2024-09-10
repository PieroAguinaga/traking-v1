"""."""
import pymysql

class DAOcamara:
    """."""
    def connect(self):
        """."""
        return pymysql.connect(host="localhost",user="root",password="",db="db_app" )

    def read_camara(self, id = None):
        """."""
        con = DAOcamara.connect(self)
        cursor = con.cursor()

        try:
            if id is None:
                cursor.execute("SELECT * FROM camara order by id_camara asc")
            else:
                cursor.execute("SELECT * FROM camara where id_camara = %s order by id_camara asc", (id,))
            return cursor.fetchall()
        except Exception:
            print(f"Error reading cameras: {Exception}")
            return []
        finally:
            con.close()

    def insert_camara(self,data):
        """."""
        con = DAOcamara.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO camara(ip, ubicacion, estado) VALUES(%s, %s, %s)", (data['ip'],data['ubicacion'], data['estado']))
            con.commit()
            return True 
        except Exception:
            print(f"Error inserting camera:{Exception}")
            con.rollback()
            return False
        finally:
            con.close()

    def update_camara(self, id, data):
        """."""
        con = DAOcamara.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE camara set ip = %s, ubicacion = %s, estado = %s where id = %s",  (data['ip'],data['ubicacion'],data['estado'],id,))
            con.commit()
            return True
        except Exception:
            print(f"Error updating camera: {Exception}")
            con.rollback()
            return False
        finally:
            con.close()


    def delete_camara(self, id):
        """."""
        con = DAOcamara.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM camara where id = %s", (id,))
            con.commit()
            return True
        except Exception:
            print(f"Error deleting camera: {Exception}")
            con.rollback()
            return False
        finally:
            con.close()
