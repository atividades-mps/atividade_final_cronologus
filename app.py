from datetime import date

import connexion
from flask import render_template

app = connexion.App(__name__, specification_dir='./src/api/routes')
app.add_api('swagger.yml')

@app.route('/')
def home():
    return render_template('splash.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/create-event')
def create_event():
    return render_template('create-event.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
