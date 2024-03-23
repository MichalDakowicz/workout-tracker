from database import *
    # if (group === "Chest") {
    #     // Upper Chest, Middle Chest, Lower Chest
    #     muscle.innerHTML =
    #         '<option value="Upper Chest">Upper Chest</option><option value="Middle Chest">Middle Chest</option><option value="Lower Chest">Lower Chest</option>';
    # } else if (group === "Back") {
    #     // Lat, Middle Back, Lower Back
    #     muscle.innerHTML =
    #         '<option value="Lat">Lat</option><option value="Middle Back">Middle Back</option><option value="Lower Back">Lower Back</option>';
    # } else if (group === "Legs") {
    #     // Quads, Hamstrings, Calves, Glutes, Adductors, Abductors, Tibialis Anterior
    #     muscle.innerHTML =
    #         '<option value="Quads">Quads</option><option value="Hamstrings">Hamstrings</option><option value="Calves">Calves</option><option value="Glutes">Glutes</option><option value="Adductors">Adductors</option><option value="Abductors">Abductors</option><option value="Tibialis">Tibialis</option>';
    # } else if (group === "Shoulders") {
    #     // Front Delts, Side Delts, Rear Delts, Traps, Rotator Cuff
    #     muscle.innerHTML =
    #         '<option value="Front Delts">Front Delts</option><option value="Side Delts">Side Delts</option><option value="Rear Delts">Rear Delts</option><option value="Traps">Traps</option><option value="Rotator Cuff">Rotator Cuff</option>';
    # } else if (group === "Arms") {
    #     // Biceps, Triceps, Forearms
    #     muscle.innerHTML =
    #         '<option value="Biceps">Biceps</option><option value="Triceps">Triceps</option><option value="Forearms">Forearms</option>';
    # } else if (group === "Core") {
    #     // Upper Abs, Middle Abs, Lower Abs, Oblique
    #     muscle.innerHTML =
    #         '<option value="Upper Abs">Upper Abs</option><option value="Middle Abs">Middle Abs</option><option value="Lower Abs">Lower Abs</option><option value="Oblique">Oblique</option>';
    # }
exercises = [
    # Chest
    {"name": "Bench Press", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts, Triceps"}, 
    {"name": "Incline Bench Press", "muscle_group": "Chest", "muscle": "Upper Chest, Front Delts, Triceps"}, 
    {"name": "Decline Bench Press", "muscle_group": "Chest", "muscle": "Lower Chest, Front Delts, Triceps"}, 
    {"name": "Dumbbell Flyes", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts"}, 
    {"name": "Chest Dips", "muscle_group": "Chest", "muscle": "Lower Chest, Triceps"}, 
    {"name": "Push Ups", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts, Triceps"}, 
    {"name": "Dumbbell Press", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts, Triceps"},
    {"name": "Incline Dumbbell Press", "muscle_group": "Chest", "muscle": "Upper Chest, Front Delts, Triceps"},
    {"name": "Decline Dumbbell Press", "muscle_group": "Chest", "muscle": "Lower Chest, Front Delts, Triceps"},
    {"name": "Cable Chest Press", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts"},
    {"name": "Cable Flyes", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts"},
    {"name": "Machine Chest Press", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts"},
    {"name": "Pec Deck", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts"},
    {"name": "Machine Flyes", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts"},
    {"name": "Incline Cable Flyes", "muscle_group": "Chest", "muscle": "Upper Chest, Front Delts"},
    {"name": "Decline Cable Flyes", "muscle_group": "Chest", "muscle": "Lower Chest, Front Delts"},
    {"name": "Plyo Push-Ups", "muscle_group": "Chest", "muscle": "Middle Chest, Front Delts, Triceps, Core"},
        
    # Back
    {"name": "Pull Ups", "muscle_group": "Back", "muscle": "Lat, Biceps, Middle Back"}, 
    {"name": "Barbell Row", "muscle_group": "Back", "muscle": "Lat, Middle Back, Rear Delts, Biceps"}, 
    {"name": "Pulldown", "muscle_group": "Back", "muscle": "Lat, Middle Back, Biceps"}, 
    {"name": "Seated Row", "muscle_group": "Back", "muscle": "Middle Back, Lat, Rear Delts, Biceps"}, 
    {"name": "T-Bar Row", "muscle_group": "Back", "muscle": "Middle Back, Lat, Rear Delts, Biceps"},
    {"name": "Hyperextensions", "muscle_group": "Back", "muscle": "Lower Back, Hamstrings, Glutes"}, 
    {"name": "Inverted Rows", "muscle_group": "Back", "muscle": "Lats, Middle Back, Rear Delts, Biceps"}, 
    {"name": "One Arm Dumbbell Row", "muscle_group": "Back", "muscle": "Lats, Middle Back, Rear Delts, Biceps"}, 
    {"name": "Cable Row", "muscle_group": "Back", "muscle": "Middle Back, Lat, Rear Delts, Biceps"},
    {"name": "Machine Row", "muscle_group": "Back", "muscle": "Middle Back, Lat, Rear Delts, Biceps"},
    {"name": "Dumbbell Pullover", "muscle_group": "Back", "muscle": "Lat, Chest, Triceps"},
    {"name": "Chest Supported Row", "muscle_group": "Back", "muscle": "Middle Back, Lat, Rear Delts, Biceps"},
    {"name": "Pullover", "muscle_group": "Back", "muscle": "Lat, Middle Back, Triceps"},
    {"name": "Bent Over Row", "muscle_group": "Back", "muscle": "Lats, Middle Back, Rear Delts, Biceps"},
    {"name": "Chin-Ups", "muscle_group": "Back", "muscle": "Lats, Biceps, Middle Back"},
    {"name": "Lat Pulldown (Wide Grip)", "muscle_group": "Back", "muscle": "Lats (Outer), Middle Back, Biceps"},
    {"name": "Lat Pulldown (Close Grip)", "muscle_group": "Back", "muscle": "Lats (Inner), Middle Back, Biceps"},
    
    # Legs
    {"name": "Deadlift", "muscle_group": "Legs", "muscle": "Hamstrings, Glutes, Lower Back"},
    {"name": "Leg Press", "muscle_group": "Legs", "muscle": "Quads, Glutes, Hamstrings"}, 
    {"name": "Squats", "muscle_group": "Legs", "muscle": "Quads, Glutes, Hamstrings, Adductors"}, 
    {"name": "Lunges", "muscle_group": "Legs", "muscle": "Quads, Glutes, Hamstrings, Adductors"}, 
    {"name": "Leg Curls", "muscle_group": "Legs", "muscle": "Hamstrings"}, 
    {"name": "Leg Extensions", "muscle_group": "Legs", "muscle": "Quads"}, 
    {"name": "Front Squats", "muscle_group": "Legs", "muscle": "Quads, Glutes, Hamstrings, Adductors"},
    {"name": "Hack Squats", "muscle_group": "Legs", "muscle": "Quads, Glutes, Hamstrings"},
    {"name": "Bulgarian Split Squat", "muscle_group": "Legs", "muscle": "Quads, Glutes, Hamstrings"},
    {"name": "Romanian Deadlift (RDL)", "muscle_group": "Legs", "muscle": "Hamstrings, Glutes, Lower Back"},
    {"name": "Goblet Squat", "muscle_group": "Legs", "muscle": "Quads, Glutes, Hamstrings, Adductors"}, 
    {"name": "Sumo Deadlift", "muscle_group": "Legs", "muscle": "Hamstrings, Glutes, Lower Back, Adductors"},
    {"name": "Stiff Leg Deadlift", "muscle_group": "Legs", "muscle": "Hamstrings, Glutes, Lower Back"},
    {"name": "Seated Calf Raise", "muscle_group": "Legs", "muscle": "Calves, Tibialis Anterior"},
    {"name": "Standing Calf Raise", "muscle_group": "Legs", "muscle": "Calves, Tibialis Anterior"},
    {"name": "Good Mornings", "muscle_group": "Legs", "muscle": "Hamstrings, Glutes, Lower Back"},  
    {"name": "Box Jumps", "muscle_group": "Legs", "muscle": "Quads, Glutes, Hamstrings, Calves"}, 
    {"name": "Hip Thrusts", "muscle_group": "Legs", "muscle": "Glutes, Hamstrings"},
    {"name": "Nordic Hamstring Curl", "muscle_group": "Legs", "muscle": "Hamstrings"}, 
    
    # Shoulders
    {"name": "Lateral Raises", "muscle_group": "Shoulders", "muscle": "Side Delts"}, 
    {"name": "Rear Delt Flyes", "muscle_group": "Shoulders", "muscle": "Rear Delts, Middle Back"}, 
    {"name": "Barbell Shrugs", "muscle_group": "Shoulders", "muscle": "Traps, Upper Back"}, 
    {"name": "Dumbbell Shrugs", "muscle_group": "Shoulders", "muscle": "Traps, Upper Back"},
    {"name": "Upright Rows", "muscle_group": "Shoulders", "muscle": "Traps, Front Delts, Side Delts, Biceps"},
    {"name": "Face Pulls", "muscle_group": "Shoulders", "muscle": "Rear Delts, Rotator Cuff, Middle Back"},
    {"name": "Arnold Press", "muscle_group": "Shoulders", "muscle": "Front Delts, Side Delts, Triceps"},
    {"name": "Front Raises", "muscle_group": "Shoulders", "muscle": "Front Delts, Upper Chest"}, 
    {"name": "Bent Over Rear Delt Raises", "muscle_group": "Shoulders", "muscle": "Rear Delts, Middle Back"},
    {"name": "Overhead Press", "muscle_group": "Shoulders", "muscle": "Front Delts, Side Delts, Triceps, Upper Chest"},
    {"name": "Dumbbell Shoulder Press", "muscle_group": "Shoulders", "muscle": "Front Delts, Side Delts, Triceps, Upper Chest"},
    {"name": "Machine Shoulder Press", "muscle_group": "Shoulders", "muscle": "Front Delts, Side Delts, Triceps, Upper Chest"},
    {"name": "Military Press", "muscle_group": "Shoulders", "muscle": "Front Delts, Side Delts, Triceps, Upper Chest"}, 
    {"name": "Pike Push-Ups", "muscle_group": "Shoulders", "muscle": "Front Delts, Side Delts, Triceps"},
    {"name": "Cable Upright Rows", "muscle_group": "Shoulders", "muscle": "Traps, Front Delts, Side Delts, Biceps"},

    # Arms
    {"name": "Bicep Curls", "muscle_group": "Arms", "muscle": "Biceps, Forearms"}, 
    {"name": "Tricep Pushdown", "muscle_group": "Arms", "muscle": "Triceps"}, 
    {"name": "Skull Crushers", "muscle_group": "Arms", "muscle": "Triceps"}, 
    {"name": "Hammer Curls", "muscle_group": "Arms", "muscle": "Biceps, Forearms"}, 
    {"name": "Reverse Curls", "muscle_group": "Arms", "muscle": "Forearms, Biceps"}, 
    {"name": "Wrist Curls", "muscle_group": "Arms", "muscle": "Forearms"},
    {"name": "Reverse Wrist Curls", "muscle_group": "Arms", "muscle": "Forearms"},
    {"name": "Concentration Curls", "muscle_group": "Arms", "muscle": "Biceps, Forearms"},
    {"name": "Tricep Dips", "muscle_group": "Arms", "muscle": "Triceps, Front Delts, Middle Chest"},
    {"name": "Close-Grip Bench Press", "muscle_group": "Arms", "muscle": "Triceps, Middle Chest"},
    {"name": "Overhead Tricep Extension", "muscle_group": "Arms", "muscle": "Triceps"},
    {"name": "Preacher Curl", "muscle_group": "Arms", "muscle": "Biceps, Forearms"},
    {"name": "Cable Curls", "muscle_group": "Arms", "muscle": "Biceps, Forearms"},
    {"name": "Cable Tricep Extension", "muscle_group": "Arms", "muscle": "Triceps"},
    {"name": "Machine Bicep Curl", "muscle_group": "Arms", "muscle": "Biceps, Forearms"},
    {"name": "Machine Tricep Extension", "muscle_group": "Arms", "muscle": "Triceps"},
    {"name": "Dumbbell Bicep Curl", "muscle_group": "Arms", "muscle": "Biceps, Forearms"},
    {"name": "Dumbbell Tricep Extension", "muscle_group": "Arms", "muscle": "Triceps"},
    {"name": "Machine Preacher Curl", "muscle_group": "Arms", "muscle": "Biceps, Forearms"},
    {"name": "Zottman Curl", "muscle_group": "Arms", "muscle": "Biceps, Forearms"},
    {"name": "Incline Dumbbell Curls", "muscle_group": "Arms", "muscle": "Biceps, Forearms" },
    {"name": "Overhead Dumbbell Tricep Extension", "muscle_group": "Arms", "muscle": "Triceps"},
    
    # Core
    {"name": "Crunches", "muscle_group": "Core", "muscle": "Upper Abs"}, 
    {"name": "Leg Raises", "muscle_group": "Core", "muscle": "Lower Abs"}, 
    {"name": "Russian Twists", "muscle_group": "Core", "muscle": "Oblique"}, 
    {"name": "Plank", "muscle_group": "Core", "muscle": "Middle Abs"},
    {"name": "Side Plank", "muscle_group": "Core", "muscle": "Oblique"},
    {"name": "Mountain Climbers", "muscle_group": "Core", "muscle": "Lower Abs"},
    {"name": "Hanging Leg Raises", "muscle_group": "Core", "muscle": "Lower Abs"}
]

def add_exercises():
    conn = connect_db()
    cursor = conn.cursor()

    for exercise in exercises:
        cursor.execute("SELECT * FROM exercises WHERE exercise = ?", (exercise["name"],))
        existing_exercise = cursor.fetchone()
        if existing_exercise is None:
            cursor.execute("INSERT INTO exercises (exercise, muscle_group, muscle) VALUES (?, ?, ?)", (exercise["name"], exercise["muscle_group"], exercise["muscle"]))
        
    conn.commit()
    conn.close()