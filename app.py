from flask import Flask, render_template, request

app = Flask(__name__, template_folder="frontend/templates")

@app.route('/', methods=['GET', 'POST'])
def login():pyt
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Placeholder logic - replace with actual authentication
        if email == "testuser@example.com" and password == "password123":
            return f"Welcome, {email}!"
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
