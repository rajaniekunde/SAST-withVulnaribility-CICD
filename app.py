# app.py
from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Vulnerable to SQL Injection - user input directly used in SQL query without sanitization
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Vulnerable SQL query
    cursor.execute(f"SELECT * FROM users WHERE name = '{query}'")  # SQL injection vulnerability
    results = cursor.fetchall()
    conn.close()
    return str(results)

@app.route('/greet', methods=['GET'])
def greet():
    user_input = request.args.get('name')
    # Vulnerable to XSS if user input is not sanitized
    return f"Hello, {user_input}!"  # XSS vulnerability (no escaping)

@app.route('/write', methods=['POST'])
def write():
    user_input = request.form['data']
    # Insecure file writing (allows user to write arbitrary data to the server)
    with open('user_data.txt', 'w') as file:
        file.write(user_input)  # File writing vulnerability

    return "Data written to file!"

if __name__ == '__main__':
    app.run(debug=True)
