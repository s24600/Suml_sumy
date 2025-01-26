import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor

data = pd.read_csv("gym_members_exercise_tracking_prepared.csv", index_col=0)

shuffled_data = data.sample(frac=1, random_state=101)
train_size = int(0.9 * len(data))

train_data = TabularDataset(shuffled_data[:train_size])
test_data = TabularDataset(shuffled_data[train_size:])

save_path = "AutogluonModel"

label = "Time_Week"
predictor = TabularPredictor(label=label, path=save_path).fit(train_data)
y_pred = predictor.predict(test_data.drop(columns=[label]))

def get_best_model_name():
    return predictor.leaderboard(test_data).iloc[0, 0]
