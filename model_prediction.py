"""
This script loads a trained model and makes predictions based on user input.
"""

import pandas as pd
from autogluon.tabular import TabularPredictor

# Mapping for experience levels
experience_level_dict = {
    "Beginner": 1,
    "Intermediate": 2,
    "Advanced": 3,
    "Professional": 4,
}

def predict(entry):
    # Load the trained model
    predictor = TabularPredictor.load("AutogluonModel")

    # Process gender information
    gender = entry.pop("Gender", None)
    if gender:
        entry["Gender_Male"] = 1
        entry["Gender_Female"] = 0
    else:
        entry["Gender_Male"] = 0
        entry["Gender_Female"] = 1

    # Convert workout types to integers
    entry["Workout_Type_Cardio"] = int(entry["Workout_Type_Cardio"])
    entry["Workout_Type_HIIT"] = int(entry["Workout_Type_HIIT"])
    entry["Workout_Type_Strength"] = int(entry["Workout_Type_Strength"])
    entry["Workout_Type_Yoga"] = int(entry["Workout_Type_Yoga"])

    # Map experience level to numeric values
    entry["Experience_Level"] = experience_level_dict[entry["Experience_Level"]]

    # Convert entry to DataFrame
    entry = {k:[v] for k,v in entry.items()}
    df = pd.DataFrame(entry)

    # Make prediction
    y_unknown = predictor.predict(df)[0]
    y_unknown = f'{y_unknown:.2f}'

    return y_unknown
