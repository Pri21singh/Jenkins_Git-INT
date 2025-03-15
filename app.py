import mysql.connector
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Software@2025',
    'host': 'localhost',
    'database': 'my_test_db'
}

def get_db_connection():
    """Create and return a MySQL database connection."""
    conn = mysql.connector.connect(**db_config)
    conn.autocommit = True  # Ensure autocommit is enabled
    return conn

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
        print(f"Inserting user {username} into database...")  # Debugging log
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()  # Commit transaction to ensure data is saved
        print(f"User {username} inserted successfully!")  # Log success
    except mysql.connector.Error as e:
        print(f"Database error: {e}")  # Print error in Flask logs
        conn.rollback()  # Rollback transaction in case of error
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
