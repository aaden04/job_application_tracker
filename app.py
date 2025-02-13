from flask import Flask, render_template, request, render_template, session, redirect 
from lib.database_connection import *
from lib.user_repository import UserRepository
from lib.user import *
from lib.job_application import *
from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__, 
            template_folder="frontend/templates",
            static_folder="frontend/staticgit")
secret_key = os.environ.get("SECRET_KEY")
if secret_key == None:
    raise Exception("Secret key is required! Add SECRET_KEY to .env file")
app.secret_key = secret_key.encode()


db_connection = DatabaseConnection()
db_connection.connect()

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Placeholder logic - replace with actual authentication

        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)
        users = user_repository.all()
        print(users)
        if user_repository.check_password(email, password):
            id = user_repository.find_by_email(email).id
            session["id"] = id
            return render_template('applications.html')
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

@app.route('/test-repository', methods=['GET'])
def test_repository():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)

    # Check if the email exists and the password is correct
    email = 'jenny@gmail.com'  # Replace with a test email in your DB
    password = 'password'       # Replace with the corresponding password

    if user_repository.check_password(email, password):
        user = user_repository.find_by_email(email)
        return f"User found: {user.name}, ID: {user.id}"
    else:
        return "Login failed: Invalid email or password"


if __name__ == '__main__':
    app.run(debug=True)






