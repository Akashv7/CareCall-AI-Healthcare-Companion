import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib


# load data

data=pd.read_csv(
"dataset/diabetes.csv"
)


X=data.drop(
"Outcome",
axis=1
)

y=data["Outcome"]


# split

X_train,X_test,y_train,y_test=train_test_split(
X,
y,
test_size=0.2,
random_state=42
)


# model

model=RandomForestClassifier(
n_estimators=100
)


model.fit(
X_train,
y_train
)


prediction=model.predict(
X_test
)


accuracy=accuracy_score(
y_test,
prediction
)


print(
"Accuracy:",
accuracy
)


# save

joblib.dump(
model,
"models/diabetes_model.pkl"
)


print(
"Model Saved Successfully"
)