from lib.database_connection import *
from lib.user import *

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, name, email, password):
        with self._connection.connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', 
                [name, email, password]
            )

    def check_password(self, email, password_attempt):
        with self._connection.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", [email, password_attempt])
            return cursor.fetchone() is not None  

    def find_by_email(self, email):
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s", [email])
    
        if not rows:  
            return None  

        user_data = rows[0]  

        return User(user_data["id"], user_data["name"], user_data["email"], user_data["password"])  



    def all(self):
        with self._connection.connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users')
            rows = cursor.fetchall()

        return [User(row[0], row[1], row[2], row[3]) for row in rows]  

    def get_user(self, user_id):
        with self._connection.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE id = %s", [user_id])
            return cursor.fetchone()


    def delete_user(self, user_id):
        with self._connection.connection.cursor() as cursor:
            cursor.execute("DELETE FROM users WHERE id = %s", [user_id])
        self._connection.commit()

    def update_user(self, user_id, name, email):
        with self._connection.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE users SET name = %s, email = %s WHERE id = %s",
                [name, email, user_id]
            )
        self._connection.connection.commit()
