import sqlite3

class User:
    def __init__(self, _id, username, password):
        self.id=_id
        self.username= username
        self.password= password

    @classmethod
    def find_by_username(cls, username):
        connection= sqlite3.connect('mydata.db')
        cursor= connection.cursor()

        query= "SELECT * FROM users WHERE username=?"
        result= cursor.execute(query, (username,))      #参数的格式一定要是tuple,单个元素的tuple后面要加个comma.
        row= result.fetchone()
        if row:
            user= cls(*row)
        else:
            user= None

        connection.close()

        return user


    @classmethod
    def find_by_id(cls, _id):
        connection= sqlite3.connect('mydata.db')
        cursor= connection.cursor()

        query= "SELECT * FROM users WHERE id=?"
        result= cursor.execute(query, (_id,))      #参数的格式一定要是tuple,单个元素的tuple后面要加个comma.
        row= result.fetchone()
        if row:
            user= cls(*row)
        else:
            user= None

        connection.close()

        return user

