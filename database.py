import sqlite3

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
            icon_link TEXT,
            strength_scores TEXT,
            segmented_bodyfat TEXT,
            segmented_muscle TEXT,
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
    
# create all the tables
def create_tables():
    create_table()
    create_table_ex()
    create_table_workout()

def create_admin():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES ('ADMIN', 'pbkdf2:sha256:600000$Ayp01LytbMpmXqK7$0b2d8c750bb1142939181e47f85dd0377fd2eeb13c4e0493cf89e31fadfdfd30')")
    conn.commit()
    conn.close()