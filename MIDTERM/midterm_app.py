from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # Implement your login logic here
    return f"Logged in as {username}"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        # Implement your registration logic here
        return f"Registered {username}"
    return render_template('registration.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
