"""
This script trains a model using the Autogluon library 
and returns the best model name from the leaderboard
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor

data = pd.read_csv("gym_members_exercise_tracking_prepared.csv", index_col=0)

shuffled_data = data.sample(frac=1, random_state=101)
train_size = int(0.9 * len(data))

train_data, test_data = train_test_split(data, test_size=0.1, random_state=101)

SAVE_PATH = "AutogluonModel"

LABEL = "Time_Week"
predictor = TabularPredictor(label=LABEL, path=SAVE_PATH).fit(train_data)
y_pred = predictor.predict(test_data.drop(columns=[LABEL]))

def get_best_model_name():
    """Function to get the best model name from the leaderboard"""
    return predictor.leaderboard(test_data).iloc[0, 0]
