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
    email = request.form['email']
    password = request.form['password']

    connection = get_flask_database_connection(app)

    user_repository = UserRepository(connection)

    users = user_repository.all()
    
    if user_repository.check_password(email, password):

        id = user_repository.find_by_email(email).id
        session["id"] = id
        return redirect(f"/applications")

    else:
        
        return render_template("login.html", error=True, email=email, password=password)



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
