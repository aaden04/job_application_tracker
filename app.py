from flask import Flask, render_template, request, render_template, session, redirect, url_for
from lib.database_connection import *
from lib.user_repository import UserRepository
from lib.user import *
from lib.job_application_repository import ApplicationsRepository
from lib.job_application import *

from dotenv import load_dotenv
import os


load_dotenv()
app = Flask(__name__, 
            template_folder="frontend/templates",
            static_folder="frontend/static")
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



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)

        existing_user = user_repository.find_by_email(email)
        if existing_user:
            return "User already exists. Try logging in.", 400

        user_repository.create(name, email, password)
        print(f"User {email} created successfully.")
        
        
        new_user = user_repository.find_by_email(email)
        if new_user:
            session["id"] = new_user.id
            return render_template('login.html')  

        return "An error occurred. Please try again.", 500  

    return render_template('signup.html')  





@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    return "Placeholder for dashboard"

# connection = get_flask_database_connection(app)
# user_repository = UserRepository(connection)





@app.route('/myprofile', methods=['GET', 'POST', 'DELETE', 'PUT'])
def myprofile():
    return "Placeholder for myprofile"

# connection = get_flask_database_connection(app)
# user_repository = UserRepository(connection)
# job_application_repository = ApplicationsRepository(connection)





@app.route('/addjobs', methods=['GET', 'POST', 'DELETE', 'PUT'])
def addjobs():
    if request.method == 'POST':
        company = request.form.get('company')
        title = request.form.get('title')
        location = request.form.get('location')
        salary = request.form.get('salary')
        date_applied = request.form.get('date_applied')

        user_id = session.get("id")

        connection = get_flask_database_connection(app)
        job_application_repository = ApplicationsRepository(connection)
        print(job_application_repository)
        job_application_repository.add_application(company, title, location, salary, date_applied)

        
        
    return render_template('add_jobs.html')

    




if __name__ == '__main__':
    app.run(debug=True)






