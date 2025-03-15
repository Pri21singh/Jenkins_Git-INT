from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database configuration - Update with your MySQL credentials
db_config = {
    'user': 'root',
    'password': 'Software@2025',
    'host': 'localhost',
    'database': 'my_test_db'
}

def get_db_connection():
    """Create and return a MySQL database connection."""
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    """Render the login form."""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    """Handle form submission, insert user into the database."""
    username = request.form['username']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)