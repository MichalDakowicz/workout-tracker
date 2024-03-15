from flask import Flask, render_template, request, url_for, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

# private code imports
from strength import *
from database import *

app = Flask(__name__)

conn = connect_db()
cursor = conn.cursor()
cursor.execute("SELECT * FROM workouts WHERE username=?", ("ADMIN",))
workouts = cursor.fetchall()
workouts_list = []
for workout in workouts:
    if workout[3] == "[]":
        pass
    else:
        workout = "{" + workout[3] + "}"
        workouts_list.append(eval(workout))
        

print(workouts)
print(workouts_list)