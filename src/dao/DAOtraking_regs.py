import pymysql

class DAOtraking_regs:
    def connect(self):
        return pymysql.connect(host="localhost",user="root",password="",db="db_app" )

    def read_traking_regs(self, id):
        con = DAOtraking_regs.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM traking_regs order by id_traking asc")
            else:
                cursor.execute("SELECT * FROM traking_regs where id = %s order by id_traking asc", (id,))
            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()


    def insert_traking_regs(self,data):
        con = DAOtraking_regs.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO traking_regs(id_traking,id_calle,fecha) VALUES(%s, %s,%s)", (data['id_traking'],data['id_calle'],data['fecha'],))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()




    def update_traking_regs(self, id, data):
        con = DAOtraking_regs.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE traking_regs set id_traking = %s, id_calle = %s,fecha = %s  where id = %s",  (data['id_traking'],data['id_calle'],data['fecha'],id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()


    def delete_traking_regs(self, id):
        con = DAOtraking_regs.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM traking_regs where id = %s", (id,))
            con.commit()
            return True
        except:
            con.rollback()
            return False
        finally:
            con.close()