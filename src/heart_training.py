import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load dataset

data = pd.read_csv(
    "dataset/heart.csv"
)


X = data.drop(
    "target",
    axis=1
)

y = data["target"]


# split

X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Model

model = RandomForestClassifier(
    n_estimators=100
)


model.fit(
    X_train,
    y_train
)


pred = model.predict(
    X_test
)


print(
    "Heart Model Accuracy:",
    accuracy_score(
        y_test,
        pred
    )
)


# Save

joblib.dump(
    model,
    "models/heart_model.pkl"
)


print(
    "Heart Model Saved")