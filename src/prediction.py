import joblib


# Load Models

diabetes_model = joblib.load(
    "models/diabetes_model.pkl"
)

heart_model = joblib.load(
    "models/heart_model.pkl"
)

kidney_model = joblib.load(
    "models/kidney_model.pkl"
)



# ================= DIABETES =================

def predict_diabetes(data):

    return diabetes_model.predict(
        [data]
    )[0]



def diabetes_confidence(data):

    prob = diabetes_model.predict_proba(
        [data]
    )

    return round(
        max(prob[0]) * 100,
        2
    )




# ================= HEART =================

def predict_heart(data):

    return heart_model.predict(
        [data]
    )[0]



def heart_confidence(data):

    prob = heart_model.predict_proba(
        [data]
    )

    return round(
        max(prob[0])*100,
        2
    )





# ================= KIDNEY =================


def predict_kidney(data):

    return kidney_model.predict(
        [data]
    )[0]



def kidney_confidence(data):

    prob = kidney_model.predict_proba(
        [data]
    )


    return round(
        max(prob[0])*100,
        2
    )