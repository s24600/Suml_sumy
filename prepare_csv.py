import kagglehub
import shutil
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


path = kagglehub.dataset_download("valakhorasani/gym-members-exercise-dataset")
print("Path to dataset files:", path)
shutil.copy(f"{path}/gym_members_exercise_tracking.csv", "./gym_members_exercise_tracking.csv")

exercise_tracking = pd.read_csv("./gym_members_exercise_tracking.csv")

exercise_tracking_numeric = pd.get_dummies(exercise_tracking, dtype=int)

exercise_tracking_numeric['Time_Week'] = exercise_tracking_numeric['Session_Duration (hours)'] * exercise_tracking_numeric['Workout_Frequency (days/week)']
exercise_tracking_numeric = exercise_tracking_numeric.drop(columns=['Session_Duration (hours)', 'Workout_Frequency (days/week)'])
exercise_tracking_numeric = exercise_tracking_numeric.drop(columns=['Calories_Burned', 'Water_Intake (liters)'])

exercise_tracking_numeric.to_csv('./gym_members_exercise_tracking_prepared.csv')

X_train, X_test, y_train, y_test = train_test_split(exercise_tracking_numeric.drop('Time_Week', axis=1), exercise_tracking_numeric['Time_Week'], test_size=0.3, random_state=1337)
