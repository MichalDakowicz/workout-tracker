def extract_exercise_names(workout_data):
    exercise_names = []
    for workout in workout_data:
        for exercise_group in workout[1]:  # Iterate over exercise groups
            for exercise in exercise_group['workout']:  # Iterate over individual exercises 
                exercise_names.append(exercise['name'])
    return exercise_names
                