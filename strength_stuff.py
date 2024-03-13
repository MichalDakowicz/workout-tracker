import numpy as np
from scipy.interpolate import interp1d
import json

# Function to calculate the one rep max's
def calc_one_rep_max(exercises):
    one_rep_maxes = {}

    for exercise_name, data in exercises.items():
        weight = data['weight']
        reps = data['reps']

        if reps == 1:
            estimated_one_rep_max = weight
        else:
            estimated_one_rep_max = weight / (1.0278 - 0.0278 * reps)

        one_rep_maxes[exercise_name] = estimated_one_rep_max

    return one_rep_maxes

# Load exercise data from JSON files
def load_exercise_data():
    exercises = ['barbell_row', 'bench_press', 'deadlift', 'overhead_press', 'squat']
    data = {}
    for exercise in exercises:
        with open(f'{exercise}.json') as f:
            data[exercise] = json.load(f)[exercise]
    return data

# Calculate percentile
def calculate_percentile(exercise_data, gender, body_weight, lifted_weight):
    gender_data = exercise_data[gender]
    body_weights = np.array(list(gender_data.keys())).astype(float)
    closest_weights = np.sort(np.array([w for w in body_weights if w <= body_weight])[-1:] \
                              .tolist() + np.array([w for w in body_weights if w >= body_weight])[:1].tolist())
    
    if len(closest_weights) == 1:
        closest_weight = closest_weights[0]
    else:
        lower_weight, upper_weight = closest_weights
        if body_weight - lower_weight < upper_weight - body_weight:
            closest_weight = lower_weight
        else:
            closest_weight = upper_weight
    
    weight_data = gender_data[str(int(closest_weight))]  # Convert to string
    lifted_weights = np.array(list(map(float, weight_data.keys())))
    percentiles = np.array(list(weight_data.values()))
    lifted_weight_func = interp1d(lifted_weights, percentiles, bounds_error=False, fill_value="extrapolate")
    return float(lifted_weight_func(lifted_weight))

# Categorize percentile
def categorize_percentile(percentile):
    if percentile < 40:
        return 'Novice'
    elif percentile < 60:
        return 'Intermediate'
    elif percentile < 75:
        return 'Advanced'
    elif percentile < 90:
        return 'Elite'
    else:
        return 'World Class'

# Main function to load data, calculate percentile, and categorize for all exercises
def calculate_scores(gender, body_weight, lifted_weights):
    exercise_data = load_exercise_data()
    results = {}
    for exercise, weight in lifted_weights.items():
        percentile = calculate_percentile(exercise_data[exercise], gender, body_weight, weight)
        category = categorize_percentile(percentile)
        results[exercise] = (percentile, category)
    return results
