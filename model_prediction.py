import pandas as pd
from autogluon.tabular import TabularPredictor

experience_level_dict = {
    "Beginner": 1,
    "Intermediate": 2,
    "Advanced": 3,
    "Professional": 4,
}

def predict(entry):
    
    predictor = TabularPredictor.load("AutogluonModel")

    gender = entry.pop("Gender", None)
    if gender:
        entry["Gender_Male"] = 1
        entry["Gender_Female"] = 0
    else:
        entry["Gender_Male"] = 0
        entry["Gender_Female"] = 1

    entry["Workout_Type_Cardio"] = int(entry["Workout_Type_Cardio"])
    entry["Workout_Type_HIIT"] = int(entry["Workout_Type_HIIT"])
    entry["Workout_Type_Strength"] = int(entry["Workout_Type_Strength"])
    entry["Workout_Type_Yoga"] = int(entry["Workout_Type_Yoga"])

    entry["Experience_Level"] = experience_level_dict[entry["Experience_Level"]]

    entry = {k:[v] for k,v in entry.items()}
    df = pd.DataFrame(entry)

    y_unknown = predictor.predict(df)[0]
    y_unknown = f'{y_unknown:.2f}'

    return y_unknown
