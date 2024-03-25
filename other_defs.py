def extract_exercise_names(workout_data):
    exercise_names = []
    for workout_name, exercises in workout_data.items():
        for exercise_dict in exercises:
            for exercise_name in exercise_dict.keys():
                exercise_names.append(exercise_name)
    return exercise_names

def get_workout_name(workout_data):
    return list(workout_data.keys())[0]