from flask import Flask, render_template, request, url_for, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Function to connect to the SQLite database
def connect_db():
    return sqlite3.connect("tracker.db", check_same_thread=False)

# Create a table to store user information if not exists
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

# Excercise table
def create_table_ex():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise TEXT NOT NULL,
            muscle_group TEXT NOT NULL,
            muscle TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()

# Home page
@app.route("/")
def home():
    if "username" in session:
        return render_template("home.html")
    return redirect(url_for("login"))

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cursor.fetchone()

        conn.close()

        if user and check_password_hash(user[2], password):
            session["username"] = username
            return redirect(url_for("home"))
        else:
            return "Invalid username or password"

    return render_template("login.html")

# Register page
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]

        # Check if passwords match
        if password != password2:
            return "Passwords do not match"

        # Check if the username is already in the database
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        existing_user = cursor.fetchone()

        conn.close()

        if existing_user:
            return "Username already exists. Please choose a different one."

        # If all checks pass, proceed with registration
        conn = connect_db()
        cursor = conn.cursor()

        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")

# Admin page
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "username" in session:
        if request.method == "POST":
            exercise = request.form["exercise"]
            muscle_group = request.form["muscle_group"]
            muscle = request.form["muscle"]

            conn = connect_db()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO exercises (exercise, muscle_group, muscle) VALUES (?, ?, ?)", (exercise, muscle_group, muscle))

            conn.commit()
            conn.close()

            return redirect(url_for("admin"))

        return render_template("admin.html")
    return redirect(url_for("login"))


# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    create_table()
    create_table_ex()
    app.run(debug=True)
