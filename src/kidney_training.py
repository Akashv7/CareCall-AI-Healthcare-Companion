import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load dataset

data = pd.read_csv("dataset/kidney.csv")


# remove id column if exists

if "id" in data.columns:
    data = data.drop("id", axis=1)


# fill missing values

for col in data.columns:

    if data[col].dtype == "object":

        data[col] = data[col].fillna(
            data[col].mode()[0]
        )

    else:

        data[col] = data[col].fillna(
            data[col].mean()
        )



# convert text to numbers

encoder = LabelEncoder()


for col in data.columns:

    if data[col].dtype=="object":

        data[col] = encoder.fit_transform(
            data[col]
        )


X = data.drop(
    "classification",
    axis=1
)


y = data["classification"]



X_train,X_test,y_train,y_test=train_test_split(

    X,
    y,
    test_size=0.2,
    random_state=42

)


model = RandomForestClassifier(
    n_estimators=100
)


model.fit(
    X_train,
    y_train
)


prediction=model.predict(
    X_test
)


print(
    "Kidney Accuracy:",
    accuracy_score(
        y_test,
        prediction
    )
)


joblib.dump(
    model,
    "models/kidney_model.pkl"
)


print(
"Kidney Model Saved Successfully"
)