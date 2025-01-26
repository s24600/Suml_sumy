"""
This script downloads the gym members exercise dataset from Kaggle and prepares it for training a model.
"""

import kagglehub
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split

# Download the dataset from Kaggle
path = kagglehub.dataset_download("valakhorasani/gym-members-exercise-dataset")
print("Path to dataset files:", path)
shutil.copy(f"{path}/gym_members_exercise_tracking.csv", "./gym_members_exercise_tracking.csv")

# Load the dataset
exercise_tracking = pd.read_csv("./gym_members_exercise_tracking.csv")

# Convert categorical variables to numeric
exercise_tracking_numeric = pd.get_dummies(exercise_tracking, dtype=int)

# Calculate the time spent at the gym per week and drop unnecessary columns
exercise_tracking_numeric['Time_Week'] = exercise_tracking_numeric['Session_Duration (hours)'] * exercise_tracking_numeric['Workout_Frequency (days/week)']
exercise_tracking_numeric = exercise_tracking_numeric.drop(columns=['Session_Duration (hours)', 'Workout_Frequency (days/week)'])
exercise_tracking_numeric = exercise_tracking_numeric.drop(columns=['Calories_Burned', 'Water_Intake (liters)'])

# Save the prepared dataset to a new CSV file
exercise_tracking_numeric.to_csv('./gym_members_exercise_tracking_prepared.csv')
