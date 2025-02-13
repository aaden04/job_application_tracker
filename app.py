from flask import Flask, render_template, request
from lib.database_connection import DatabaseConnection
from lib.user_repository import UserRepository
from lib.user import User

from lib.job_application import Application

app = Flask(__name__, 
            template_folder="frontend/templates",
            static_folder="frontend/staticgit")


db_connection = DatabaseConnection()
db_connection.connect()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password_attempt = request.form['password']
        
        user_repo = UserRepository(db_connection)
        
        if user_repo.check_password(email, password_attempt):  
            user = user_repo.find_by_email(email)  

            return f"Welcome, {user.name}!"  
        else:
            return "Invalid credentials, please try again."

    return render_template('login.html')

@app.route('/applications', methods=['GET', 'POST', 'DELETE', 'PUT'])
def applications():
    return ":)"
    






@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        return f"User {username} signed up successfully!"

    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
