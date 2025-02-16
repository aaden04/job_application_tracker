from flask import Flask, render_template, request, session, redirect, url_for, flash
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
            flash("Invalid credentials, please try again.", 'error')
            return redirect(url_for('login'))
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
            flash("User already exists. Try logging in.", 'error')
            return redirect(url_for('login'))

        user_repository.create(name, email, password)
        new_user = user_repository.find_by_email(email)
        if new_user:
            session["id"] = new_user.id
            flash("Account created successfully!", 'success')
            return redirect(url_for('dashboard'))

        flash("An error occurred. Please try again.", 'error')
        return redirect(url_for('signup'))

    return render_template('signup.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if "id" not in session:
        return redirect(url_for('login'))

    user_id = session["id"]
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    job_application_repository = ApplicationsRepository(connection)

    user = user_repository.get_user(user_id)
    applications = job_application_repository.get_user_applications(user_id)

    return render_template('dashboard.html', applications=applications, user=user)

@app.route('/myprofile', methods=['GET', 'POST'])
def myprofile():
    if "id" not in session:
        return redirect(url_for('login'))

    user_id = session["id"]
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    job_application_repository = ApplicationsRepository(connection)

    user = user_repository.get_user(user_id)
    
    if request.method == 'GET':
        applications = job_application_repository.get_user_applications(user_id)
        return render_template('myprofile.html', applications=applications, user=user)

    elif request.method == 'POST':
        action = request.form.get('action')

        if action == "update_profile":
            name = request.form.get('name')
            email = request.form.get('email')
            
            user_repository.update_user(user_id, name, email)
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('myprofile'))

        application_id = request.form.get('id')
        if not application_id:
            flash("Error: Application ID is required.", 'error')
            return redirect(url_for('myprofile'))

        try:
            if action == "delete":
                job_application_repository.delete_application(application_id, user_id)
                flash('Application deleted successfully!', 'success')
                return redirect(url_for('myprofile'))
                
            elif action == "update":
                company = request.form.get('company')
                title = request.form.get('title')
                location = request.form.get('location')
                salary = request.form.get('salary')
                date_applied = request.form.get('date_applied')

                job_application_repository.update_application(
                    company, title, location, salary, date_applied, application_id, user_id
                )
                flash('Job application updated successfully!', 'success')
                return redirect(url_for('myprofile'))

        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'error')
            return redirect(url_for('myprofile'))

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
        
        try:
            job_application_repository.add_application(company, title, location, salary, date_applied, user_id)
            flash('Job application added successfully!', 'success')
            return redirect(url_for('dashboard'))
        except Exception as e:
            flash(f"Error adding application: {str(e)}", 'error')
            return redirect(url_for('addjobs'))

    return render_template('add_jobs.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)