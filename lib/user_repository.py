from lib.database_connection import *
import hashlib
from lib.user import *

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, name, email, password):
        
        self._connection.execute(

            'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', 
            [name, email, password]

        )

    def check_password(self, email, password_attempt):
        rows = self._connection.execute(
            "SELECT * FROM users WHERE email = %s AND password = %s", 
            [email, password_attempt]
        )
        return len(rows) > 0
    



    def find_by_email(self, email):
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s", [email])
        if not rows:  
            return None  

        user_data = rows[0]  
        if 'id' not in user_data or 'name' not in user_data or 'password' not in user_data:
            return None  
        user = User(user_data['id'], user_data['name'], email, user_data['password'])
        return user


    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            person = User(
                row["id"],
                row["name"],
                row["email"],
                row["password"]

            )
            users.append(person)
        return users
    
    

    def find(self, user_id):
        result = self._connection.execute("SELECT * FROM users WHERE id = %s", [user_id])
        row = result[0]
        return User(
            row["id"], 
            row["name"], 
            row["email"], 
            row["password"]

        )
    


    


