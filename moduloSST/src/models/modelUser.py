from .entities.user import User

class ModelUser():
    
    @classmethod
    def login(self, db, user):
        try:
            cursor=db.connection.cursor()
            sql = """SELECT idUser, username, password FROM users 
            WHERE name = '{}'""".format(user.username)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password))
                return user
            else: 
                return None
        except Exception as e:
            raise Exception(e)
    
    @classmethod
    def getId (self, db, id):
        try:
            cursor=db.connection.cursor()
            sql = "SELECT idUser, name, lastname, typeUserId FROM users WHERE idUser = {}".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            cursor.close()
            if row != None:
                return User(row[0], row[1], None)
            else: 
                return None 
        except Exception as e:
            raise Exception(e)