from flask import Flask, render_template, request, url_for, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

# private code imports
from strength import *
from database import *
from other_defs import *
from exercises import *

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route("/", methods=['GET', 'POST'])
def home():
    if "username" in session:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM workouts WHERE username=?", (session["username"],))
        workouts = cursor.fetchall()
        workouts_return = []
        for workout in workouts:
            if workout[3] == "[]":
                pass
            else:
                workout_date = workout[2]
                workout_data = eval("{" + workout[3] + "}")
                print(workout_data)
                workout_name = get_workout_name(workout_data)
                exercise_names = extract_exercise_names(workout_data)
                workouts_return.append([workout_name, workout_date, exercise_names])
        
        conn.close()            
        
        print(workouts_return)
                                                
        return render_template("home.html", workouts=workouts_return, subdomain_tag="Home")

    return redirect(url_for("login"))

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    session["profile_picture"] = None
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
            session["profile_picture"] = user[3]
            return redirect(url_for("home"))
        else:
            return "Invalid username or password"

    return render_template("login.html", subdomain_tag="Login")

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

    return render_template("register.html", subdomain_tag="Register")

# Admin page
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if "username" in session:
        if session["username"] == "ADMIN":
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
            return render_template("admin.html", users=users, exercises=exercises, workouts=workouts, subdomain_tag="Admin")
        else:
            return redirect(url_for("home"))

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
            
            if exercises != None:
                conn.close()
                return redirect(url_for("home"))

        conn.close()
        
        

        # Pass the list of exercises to the template
        return render_template("workout.html", exercises=exercises_list, subdomain_tag="Workout")

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
        
        return render_template("exercises.html", 
                               chest_exercises=chest_exercises, 
                               back_exercises=back_exercises, 
                               legs_exercises=legs_exercises, 
                               shoulders_exercises=shoulders_exercises, 
                               arms_exercises=arms_exercises, 
                               abs_exercises=abs_exercises,
                               subdomain_tag="Exercises"
                               )
        

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
            gender = request.form.get('gender')
            weight = float(request.form.get('weight'))

            if gender not in ['male', 'female']:
                return "Invalid gender specified"

            one_rep_maxes = calc_one_rep_max(exercises)
            print(one_rep_maxes)

            results = calculate_scores(gender, weight, one_rep_maxes)
            print(results)
            
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET strength_scores = ? WHERE username = ?", (str(results), session["username"]))
            
            conn.commit()
            conn.close()
            
            return render_template("strength.html", one_rep_maxes=one_rep_maxes, strength_scores=results, exercises=exercises, info=info, subdomain_tag="Strength")
        return render_template("strength.html", subdomain_tag="Strength")
    return redirect(url_for("login"))

# Profile page
@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "username" in session:
        conn = connect_db()
        cursor = conn.cursor()

        if request.method == "GET":          
            username = session["username"]
            cursor.execute("SELECT * FROM users WHERE username=?", (username,))
            user = cursor.fetchone()
            username = user[1]
            if user[4] == None:
                strength_scores = {
                    'deadlift': 0,
                    'bench_press': 0,
                    'squat': 0,
                    'overhead_press': 0,
                    'barbell_row': 0
                }
            else:
                strength_scores = eval(str(user[4]))
            if user[5] == None:
                segmented_bodyfat = {
                    'body_fat': 0,
                    'left_arm_fat': 0,
                    'right_arm_fat': 0,
                    'trunk_fat': 0,
                    'left_leg_fat': 0,
                    'right_leg_fat': 0
                }
            else:
                segmented_bodyfat = eval(user[5])
            if user[6] == None:
                segmented_muscle = {
                    'muscle': 0,
                    'left_arm_muscle': 0,
                    'right_arm_muscle': 0,
                    'trunk_muscle': 0,
                    'left_leg_muscle': 0,
                    'right_leg_muscle': 0
                }
            else:
                segmented_muscle = eval(user[6])
            if user[7] == None:
                body_measurements = [0, 0]
            else:
                body_measurements = eval(user[7])
            
            deadlift = strength_scores['deadlift']
            bench_press = strength_scores['bench_press']
            squat = strength_scores['squat']
            overhead_press = strength_scores['overhead_press']
            barbell_row = strength_scores['barbell_row']
            
            body_fat = segmented_bodyfat['body_fat']
            left_arm_bodyfat = segmented_bodyfat['left_arm_fat']
            right_arm_bodyfat = segmented_bodyfat['right_arm_fat']
            trunk_bodyfat = segmented_bodyfat['trunk_fat']
            left_leg_bodyfat = segmented_bodyfat['left_leg_fat']
            right_leg_bodyfat = segmented_bodyfat['right_leg_fat']
            
            muscle_mass = segmented_muscle['muscle']
            left_arm_muscle = segmented_muscle['left_arm_muscle']
            right_arm_muscle = segmented_muscle['right_arm_muscle']
            trunk_muscle = segmented_muscle['trunk_muscle']
            left_leg_muscle = segmented_muscle['left_leg_muscle']
            right_leg_muscle = segmented_muscle['right_leg_muscle']
            
            height = body_measurements[0]
            weight = body_measurements[1]
            
            return render_template("profile.html", 
                                    username=username, 
                                    deadlift=deadlift, 
                                    bench_press=bench_press, 
                                    squat=squat, 
                                    overhead_press=overhead_press, 
                                    barbell_row=barbell_row, 
                                    body_fat=body_fat, 
                                    left_arm_bodyfat=left_arm_bodyfat, 
                                    right_arm_bodyfat=right_arm_bodyfat, 
                                    trunk_bodyfat=trunk_bodyfat, 
                                    left_leg_bodyfat=left_leg_bodyfat, 
                                    right_leg_bodyfat=right_leg_bodyfat, 
                                    muscle_mass=muscle_mass, 
                                    left_arm_muscle=left_arm_muscle,
                                    right_arm_muscle=right_arm_muscle,
                                    trunk_muscle=trunk_muscle,
                                    left_leg_muscle=left_leg_muscle,
                                    right_leg_muscle=right_leg_muscle,
                                    height=height,
                                    weight=weight,
                                    subdomain_tag="Profile"
                                    )

        if request.method == "POST":
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
            
            height = request.form['height']
            weight = request.form['weight']
            
            body_measurements = [height, weight]

            data_bodyfat = {
                'body_fat': bodyfat,
                'left_arm_fat': left_arm_fat,
                'right_arm_fat': right_arm_fat,
                'trunk_fat': trunk_fat,
                'left_leg_fat': left_leg_fat,
                'right_leg_fat': right_leg_fat,
            }
            data_muscle = {
                'muscle': muscle,
                'left_arm_muscle': left_arm_muscle,
                'right_arm_muscle': right_arm_muscle,
                'trunk_muscle': trunk_muscle,
                'left_leg_muscle': left_leg_muscle,
                'right_leg_muscle': right_leg_muscle
            }
            
            cursor.execute("UPDATE users SET segmented_bodyfat = ?, segmented_muscle = ?, body_measurements = ? WHERE username = ?",
                           (str(data_bodyfat), str(data_muscle), str(body_measurements), session["username"]))

        conn.commit()
        conn.close()

        return render_template("profile.html", subdomain_tag="Profile")

    return redirect(url_for("login"))

# change profile picture
@app.route("/change_pfp", methods=["GET", "POST"])
def change_pfp():
    if "username" in session:
        conn = connect_db()
        cursor = conn.cursor()

        if request.method == "POST":
            username = session["username"]
            cursor.execute("UPDATE users SET icon_link = ? WHERE username = ?", (request.form["profile_picture_link"], username))
            session["profile_picture"] = request.form["profile_picture_link"]
            
            
        conn.commit()
        conn.close()
        
        return redirect(url_for("profile"))
    return redirect(url_for("login"))

# Progress page
@app.route("/progress", methods=["GET", "POST"])
def progress():
    if "username" in session:
        # fetch the exercise history from users workouts then display it on a graph
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM workouts WHERE username=?", (session["username"],))
        workouts = cursor.fetchall()
        workout_data = []
        for workout in workouts:
            workout_date = workout[2]
            workout = "{" + workout[3] + "}"
            workouts_list = [eval(workout)]
            workout_data.append([workout_date, workouts_list])
        
        exercise_names = extract_exercise_names(workout_data)
        print(exercise_names)
        # exercise_data = extract_exercise_data(workout_data, user)
        # print(exercise_data)
        
# Logout
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    create_tables()
    add_exercises()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    if "ADMIN" not in [user[1] for user in users]:
        create_admin()
    app.run(debug=True)