from flask import Flask, render_template, request, url_for, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import secrets
import json

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Function to calculate strength scores
def calculate_strength(exercises, info):
    one_rep_maxes = {}
    gender = info.get('gender')
    user_weight = info.get('weight')

    if gender == 'male':
        coefficient = 1.0
    elif gender == 'female':
        coefficient = 0.75
    else:
        raise ValueError("Invalid gender specified")

    for exercise_name, data in exercises.items():
        weight = data['weight']
        reps = data['reps']

        if reps == 1:
            estimated_one_rep_max = weight
        else:
            estimated_one_rep_max = weight / (1.0278 - 0.0278 * reps)

        one_rep_maxes[exercise_name] = estimated_one_rep_max

    print(one_rep_maxes)
    print(user_weight)
    print(gender)
    return one_rep_maxes

    

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
            password TEXT NOT NULL,
            strength_scores TEXT,
            body_measurements TEXT
        )
        """
    )
    conn.commit()
    conn.close()

# Exercise table
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

# Create a table to store workout information if not exists
def create_table_workout():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            date TEXT NOT NULL,
            exercises TEXT NOT NULL
            )
        """
    )
    conn.commit()
    conn.close()

@app.route("/", methods=['GET', 'POST'])
def home():
    if "username" in session:
        conn = connect_db()
        cursor = conn.cursor()

        if request.method == 'POST':
            bodyfat = request.form['body-fat']
            left_arm_fat = request.form['left-arm-fat']
            right_arm_fat = request.form['right-arm-fat']
            trunk_fat = request.form['trunk-fat']
            left_leg_fat = request.form['left-leg-fat']
            right_leg_fat = request.form['right-leg-fat']
            muscle = request.form['muscle']
            left_arm_muscle = request.form['left-arm-muscle']
            right_arm_muscle = request.form['right-arm-muscle']
            trunk_muscle = request.form['trunk-muscle']
            left_leg_muscle = request.form['left-leg-muscle']
            right_leg_muscle = request.form['right-leg-muscle']

            data = {
                'body_fat': bodyfat,
                'left_arm_fat': left_arm_fat,
                'right_arm_fat': right_arm_fat,
                'trunk_fat': trunk_fat,
                'left_leg_fat': left_leg_fat,
                'right_leg_fat': right_leg_fat,
                'muscle': muscle,
                'left_arm_muscle': left_arm_muscle,
                'right_arm_muscle': right_arm_muscle,
                'trunk_muscle': trunk_muscle,
                'left_leg_muscle': left_leg_muscle,
                'right_leg_muscle': right_leg_muscle
            }
            
            cursor.execute("UPDATE users SET body_measurements=? WHERE username=?", (str(data), session["username"]))

        cursor.execute("SELECT * FROM workouts WHERE username=?", (session["username"],))
        workouts = cursor.fetchall()
        
        for i in range(len(workouts)):
            workout = list(workouts[i])
            exercises = workout[3].split(",")
            exercises = [exercise.split("\xa0")[0] for exercise in exercises if 'kg' not in exercise and exercise.strip()]
            workout[3] = "\n".join(exercises)
            workouts[i] = tuple(workout)
        
        for i in range(len(workouts)):
            workout = list(workouts[i])
            exercises = workout[3].split("\n")
            exercises = [exercise for exercise in exercises if exercise.strip()]
            workout[3] = "\n".join(exercises)
            workouts[i] = tuple(workout)
            
        conn.close()
        
        return render_template("home.html", workouts=workouts)

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
        conn = connect_db()
        cursor = conn.cursor()

        if request.method == "POST":
            action = request.form["action"]

            if action == "add_exercise":
                exercise = request.form["exercise"]
                if exercise in [ex[0] for ex in cursor.execute("SELECT exercise FROM exercises").fetchall()]:
                    pass
                else:
                    muscle_group = request.form["muscle_group"]
                    muscle = request.form["muscle"]

                    cursor.execute("INSERT INTO exercises (exercise, muscle_group, muscle) VALUES (?, ?, ?)", (exercise, muscle_group, muscle))

            elif action == "remove_exercise":
                exercise_id = request.form["exercise_id"]

                cursor.execute("DELETE FROM exercises WHERE id=?", (exercise_id,))

            elif action == "remove_user":
                user_id = request.form["user_id"]

                cursor.execute("DELETE FROM users WHERE id=?", (user_id,))

            elif action == "remove_workout":
                workout_id = request.form["workout_id"]

                cursor.execute("DELETE FROM workouts WHERE id=?", (workout_id,))

            conn.commit()

        # Fetch all users, exercises, and workouts from the database
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        cursor.execute("SELECT * FROM exercises")
        exercises = cursor.fetchall()

        cursor.execute("SELECT * FROM workouts")
        workouts = cursor.fetchall()

        conn.close()

        # Pass the users, exercises, and workouts to the template
        return render_template("admin.html", users=users, exercises=exercises, workouts=workouts)

    return redirect(url_for("login"))

# Workout page
@app.route("/workout", methods=["GET", "POST"])
def workout():
    if "username" in session:
        conn = connect_db()
        cursor = conn.cursor()

        # Fetch exercises from the database
        cursor.execute("SELECT exercise FROM exercises")
        exercises_db = cursor.fetchall()

        # Convert the result to a list of exercise names
        exercises_list = [exercise[0] for exercise in exercises_db]

        if request.method == "POST":
            username = session["username"]
            date = request.form["date"]
            exercises = request.form["exercises"]
            
            exercises = exercises[1:-1]

            cursor.execute("INSERT INTO workouts (username, date, exercises) VALUES (?, ?, ?)", (username, date, exercises))

            conn.commit()

        conn.close()

        # Pass the list of exercises to the template
        return render_template("workout.html", exercises=exercises_list)

    return redirect(url_for("home"))

# Exercises list page
@app.route("/exercises", methods=["GET", "POST"])
def exercises():
    if "username" in session:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM exercises WHERE muscle_group=?", ("Chest",))
        chest_exercises = cursor.fetchall()
        
        cursor.execute("SELECT * FROM exercises WHERE muscle_group=?", ("Back",))
        back_exercises = cursor.fetchall()
        
        cursor.execute("SELECT * FROM exercises WHERE muscle_group=?", ("Legs",))
        legs_exercises = cursor.fetchall()
        
        cursor.execute("SELECT * FROM exercises WHERE muscle_group=?", ("Shoulders",))
        shoulders_exercises = cursor.fetchall()
        
        cursor.execute("SELECT * FROM exercises WHERE muscle_group=?", ("Arms",))
        arms_exercises = cursor.fetchall()
        
        cursor.execute("SELECT * FROM exercises WHERE muscle_group=?", ("Core",))
        abs_exercises = cursor.fetchall()
        
        conn.close()
        
        return render_template("exercises.html", chest_exercises=chest_exercises, back_exercises=back_exercises, legs_exercises=legs_exercises, shoulders_exercises=shoulders_exercises, arms_exercises=arms_exercises, abs_exercises=abs_exercises)

    return redirect(url_for("home"))

# Strength levels page
@app.route("/strength", methods=["GET", "POST"])
def strength():
    if "username" in session:        
        if request.method == "POST":
            exercises = {}
            info = {}
            for exercise in ['bench_press', 'deadlift', 'squat', 'overhead_press', 'barbell_row']:
                weight_key = exercise + '_weight'
                reps_key = exercise + '_reps'
                if weight_key in request.form and reps_key in request.form:
                    exercises[exercise] = {
                        'weight': float(request.form[weight_key]),
                        'reps': int(request.form[reps_key])
                    }
            gender = request.form.get('gender')  # Extract gender from form data
            weight = float(request.form.get('weight'))  # Extract weight from form data
            info['gender'] = gender
            info['weight'] = weight

            if gender not in ['male', 'female']:
                return "Invalid gender specified"

            strength_scores = calculate_strength(exercises, info)
            return render_template("strength.html", strength_scores=strength_scores)
        return render_template("strength.html")
    return redirect(url_for("login"))





# Progress page
@app.route("/progress", methods=["GET", "POST"])
def progress():
    if "username" in session:
        conn = connect_db()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM workouts WHERE username=?", (session["username"],))
        workouts = cursor.fetchall()
        
        for i in range(len(workouts)):
            workout = list(workouts[i])
            exercises = workout[3].split(",")
            exercises = [exercise.split("\xa0")[0] for exercise in exercises if 'kg' not in exercise and exercise.strip()]
            workout[3] = "\n".join(exercises)
            workouts[i] = tuple(workout)
        
        for i in range(len(workouts)):
            workout = list(workouts[i])
            exercises = workout[3].split("\n")
            exercises = [exercise for exercise in exercises if exercise.strip()]
            workout[3] = "\n".join(exercises)
            workouts[i] = tuple(workout)
            
        conn.close()
        
        return render_template("progress.html", workouts=workouts)

    return redirect(url_for("login"))

# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    create_table()
    create_table_ex()
    create_table_workout()
    app.run(debug=True)