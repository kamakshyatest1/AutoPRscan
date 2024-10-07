import sqlite3
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Vulnerable route to demonstrate SQL Injection
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        return "Login successful!"
    else:
        return "Invalid credentials!"

# Vulnerable route to demonstrate XSS
@app.route("/greet", methods=["GET"])
def greet():
    name = request.args.get("name")
    
    # Vulnerable to Cross-Site Scripting (XSS)
    greeting = f"<h1>Hello, {name}!</h1>"
    return render_template_string(greeting)

# Vulnerable route to demonstrate file handling issues
@app.route("/read_file", methods=["GET"])
def read_file():
    filename = request.args.get("filename")
    
    # Vulnerable to Path Traversal
    with open(f"./uploads/{filename}", "r") as f:
        content = f.read()

    return content

if __name__ == "__main__":
    app.run(debug=True)
