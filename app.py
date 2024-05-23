from flask import Flask, request, render_template, redirect, url_for
import pyodbc

app = Flask(__name__)

# Database configuration
server = 'server0210.database.windows.net'
database = 'server0210'
username = 'CloudSAe7252128'
password = 'rC$02101998rC'
driver = '{ODBC Driver 17 for SQL Server}'

# Function to connect to the database
def get_db_connection():
    conn = pyodbc.connect('DRIVER=' + driver +
                          ';SERVER=' + server +
                          ';PORT=1433;DATABASE=' + database +
                          ';UID=' + username +
                          ';PWD=' + password)
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
