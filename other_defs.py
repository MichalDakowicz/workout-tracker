# Extracts the names of all exercises from the workout data
def extract_exercise_names(workout_data):
    exercise_names = []
    for workout in workout_data:
        for exercise_group in workout[1]:
            for exercise in exercise_group['workout']:
                exercise_names.append(exercise['name'])
    return exercise_names