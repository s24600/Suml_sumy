"""
This script trains a model using the Autogluon library 
and returns the best model name from the leaderboard
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from autogluon.tabular import TabularPredictor

data = pd.read_csv("gym_members_exercise_tracking_prepared.csv", index_col=0)

shuffled_data = data.sample(frac=1, random_state=101)

train_data, test_data = train_test_split(data, test_size=0.2, random_state=101)

SAVE_PATH = "AutogluonModel"

LABEL = "Time_Week"
predictor = TabularPredictor(label=LABEL, path=SAVE_PATH).fit(train_data, presets='high_quality',time_limit=1200)
predictor.delete_models(models_to_keep='best', delete_from_disk=True, dry_run=False)
y_pred = predictor.predict(test_data.drop(columns=[LABEL]))

best_model_name = predictor.leaderboard(test_data).iloc[0, 0]
best_model = predictor._trainer.load_model(best_model_name)

