from flask import Flask, render_template, request, session, redirect, url_for
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
if secret_key is None:
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
        
        if user_repository.check_password(email, password):
            user = user_repository.find_by_email(email)
            session["id"] = user.id
            return redirect(url_for('dashboard'))
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
        new_user = user_repository.find_by_email(email)
        if new_user:
            session["id"] = new_user.id
            return redirect(url_for('dashboard'))

        return "An error occurred. Please try again.", 500  

    return render_template('signup.html')  

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if "id" not in session:
        return redirect(url_for('login'))  

    user_id = session["id"]
    connection = get_flask_database_connection(app)
    job_application_repository = ApplicationsRepository(connection)

    applications = job_application_repository.get_user_applications(user_id)

    return render_template('dashboard.html', applications=applications)

@app.route('/myprofile', methods=['GET', 'POST'])
def myprofile():
    if "id" not in session:
        return redirect(url_for('login'))  

    user_id = session["id"]
    connection = get_flask_database_connection(app)
    job_application_repository = ApplicationsRepository(connection)

    if request.method == 'GET':
        applications = job_application_repository.get_user_applications(user_id)
        return render_template('myprofile.html', applications=applications)

    elif request.method == 'POST':
        action = request.form.get('action')
        application_id = request.form.get('id')

        if not application_id:
            return "Error: Application ID is required.", 400  

        try:
            if action == "delete":
                job_application_repository.delete_application(application_id, user_id)
                connection.commit()  

            elif action == "update":
                company = request.form.get('company')
                title = request.form.get('title')
                location = request.form.get('location')
                salary = request.form.get('salary')
                date_applied = request.form.get('date_applied')

                job_application_repository.update_application(
                    company, title, location, salary, date_applied, application_id, user_id
                )
                connection.commit()  

            return redirect(url_for('myprofile'))  

        except Exception as e:
            return f"An error occurred: {str(e)}", 500  

@app.route('/addjobs', methods=['GET', 'POST'])
def addjobs():
    if "id" not in session:
        return redirect(url_for('login'))  

    if request.method == 'POST':
        company = request.form.get('company')
        title = request.form.get('title')
        location = request.form.get('location')
        salary = request.form.get('salary')
        date_applied = request.form.get('date_applied')

        user_id = session["id"]

        connection = get_flask_database_connection(app)
        job_application_repository = ApplicationsRepository(connection)
        job_application_repository.add_application(company, title, location, salary, date_applied, user_id)
        return redirect(url_for('dashboard'))

    return render_template('add_jobs.html')

if __name__ == '__main__':
    app.run(debug=True)







