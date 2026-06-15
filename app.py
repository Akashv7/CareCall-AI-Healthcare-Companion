import streamlit as st


from src.prediction import (
    predict_diabetes,
    predict_heart,
    predict_kidney,

    diabetes_confidence,
    heart_confidence,
    kidney_confidence
)


from src.ai_assistant import ask_ai


from src.database import (
    create_database,
    save_history,
    get_history
)


create_database()



# ================= CONFIG =================

st.set_page_config(
    page_title="CareCall AI",
    page_icon="🩺",
    layout="wide"
)



# ================= TITLE =================


st.title(
    "🩺 CareCall AI - Elder Healthcare Companion"
)


st.write(
"""

AI-powered healthcare assistant using Machine Learning and LLM.

✔ Multi Disease Prediction  
✔ Confidence Score  
✔ Patient History  
✔ Model Performance Analysis  
✔ AI Chat Assistant  
✔ Medicine Reminder  

"""
)



# ================= SIDEBAR =================


menu = st.sidebar.selectbox(

    "Services",

    [

        "Dashboard",
        "Diabetes Prediction",
        "Heart Prediction",
        "Kidney Prediction",
        "Patient History",
        "Model Performance",
        "Medicine Reminder",
        "AI Health Assistant"

    ]

)



# ================= DASHBOARD =================


if menu=="Dashboard":


    st.header(
        "📊 Healthcare Dashboard"
    )


    c1,c2,c3,c4 = st.columns(4)


    c1.metric(
        "ML Models",
        "3"
    )


    c2.metric(
        "Algorithm",
        "Random Forest"
    )


    c3.metric(
        "AI Engine",
        "Gemini LLM"
    )


    c4.metric(
        "Database",
        "SQLite"
    )



    st.success(
    """

    🩸 Diabetes Prediction

    ❤️ Heart Prediction

    🩺 Kidney Prediction

    📊 Model Analysis

    📄 Patient Records

    🤖 AI Health Chat

    💊 Medicine Reminder

    """
    )





# ================= DIABETES =================


elif menu=="Diabetes Prediction":


    st.header(
        "🩸 Diabetes Analysis"
    )


    patient_name=st.text_input(
        "Patient Name"
    )


    col1,col2=st.columns(2)


    with col1:


        age=st.number_input("Age")

        glucose=st.number_input("Glucose")

        bp=st.number_input("Blood Pressure")

        bmi=st.number_input("BMI")


    with col2:


        cholesterol=st.number_input(
            "Cholesterol"
        )


        family=st.selectbox(
            "Family History?",
            ["No","Yes"]
        )



    if st.button(
        "Analyze Diabetes"
    ):


        data=[
            0,
            glucose,
            bp,
            20,
            80,
            bmi,
            1 if family=="Yes" else 0.3,
            age
        ]


        result=predict_diabetes(data)

        confidence=diabetes_confidence(data)



        if result==1:

            risk="HIGH"

            st.error(
                "⚠ Diabetes Risk"
            )


        else:

            risk="LOW"

            st.success(
                "✅ Low Diabetes Risk"
            )



        st.info(
            f"Confidence : {confidence}%"
        )



        save_history(
            patient_name,
            "Diabetes",
            risk,
            confidence
        )


        st.download_button(

            "📄 Download Report",

f"""

CARECALL AI REPORT

Patient:
{patient_name}

Disease:
Diabetes

Risk:
{risk}

Confidence:
{confidence} %

""",

            "diabetes_report.txt"

        )






# ================= HEART =================


elif menu=="Heart Prediction":


    st.header(
        "❤️ Heart Analysis"
    )


    patient_name=st.text_input(
        "Patient Name"
    )


    age=st.number_input("Age")

    gender=st.selectbox(
        "Gender",
        ["Female","Male"]
    )


    chest=st.selectbox(
        "Chest Pain?",
        ["No","Yes"]
    )


    bp=st.number_input(
        "Blood Pressure"
    )


    cholesterol=st.number_input(
        "Cholesterol"
    )


    heart_rate=st.number_input(
        "Heart Rate"
    )



    if st.button(
        "Analyze Heart"
    ):


        data=[

            age,
            1 if gender=="Male" else 0,
            1 if chest=="Yes" else 0,
            bp,
            cholesterol,
            0,
            0,
            heart_rate,
            0,
            1,
            1,
            0,
            2

        ]


        result=predict_heart(data)

        confidence=heart_confidence(data)



        if result==1:

            risk="HIGH"

            st.error(
                "⚠ Heart Risk"
            )


        else:

            risk="LOW"

            st.success(
                "💚 Healthy Heart"
            )



        st.info(
            f"Confidence : {confidence}%"
        )



        save_history(

            patient_name,
            "Heart Disease",
            risk,
            confidence

        )



        st.download_button(

            "📄 Download Report",

f"""

CARECALL AI REPORT

Patient:
{patient_name}

Disease:
Heart Disease

Risk:
{risk}

Confidence:
{confidence}%

""",

"heart_report.txt"

        )






# ================= KIDNEY =================


elif menu=="Kidney Prediction":


    st.header(
        "🩺 Kidney Analysis"
    )


    patient_name=st.text_input(
        "Patient Name"
    )


    age=st.number_input("Age")

    bp=st.number_input("Blood Pressure")


    sugar=st.selectbox(
        "High Sugar?",
        ["No","Yes"]
    )


    hemo=st.number_input(
        "Hemoglobin"
    )



    if st.button(
        "Analyze Kidney"
    ):


        data=[
            age,
            bp,
            1.020,
            0,
            1 if sugar=="Yes" else 0,
            120,
            40,
            1.2,
            hemo,
            40
        ]


        result=predict_kidney(data)

        confidence=kidney_confidence(data)



        if result==1:

            risk="HIGH"

            st.error(
                "⚠ Kidney Risk"
            )

        else:

            risk="LOW"

            st.success(
                "✅ Kidney Normal"
            )



        st.info(
            f"Confidence : {confidence}%"
        )


        save_history(

            patient_name,
            "Kidney Disease",
            risk,
            confidence

        )





# ================= HISTORY =================


elif menu=="Patient History":


    st.header(
        "📄 Patient Records"
    )


    records=get_history()


    for r in records:


        st.write(
f"""

👤 Patient : {r[1]}

🏥 Disease : {r[2]}

⚠ Risk : {r[3]}

🤖 Confidence : {r[4]}%

📅 Date : {r[5]}

-----------------------------

"""
        )






# ================= MODEL PERFORMANCE =================


elif menu=="Model Performance":


    st.header(
        "📊 ML Model Performance"
    )


    st.table(
        {
        "Model":[
            "Logistic Regression",
            "Decision Tree",
            "Random Forest"
        ],

        "Accuracy":[
            "84%",
            "88%",
            "94%"
        ]

        }
    )


    st.success(
    """

    Selected Model:

    🌲 Random Forest Classifier


    Reasons:

    ✔ Better Accuracy

    ✔ Handles Medical Features

    ✔ Avoids Overfitting

    ✔ Works well with healthcare data

    """
    )






# ================= MEDICINE =================


elif menu=="Medicine Reminder":


    st.header(
        "💊 Medicine Reminder"
    )


    medicine=st.text_input(
        "Medicine"
    )


    time=st.time_input(
        "Time"
    )


    if st.button(
        "Save Reminder"
    ):


        st.success(
            f"Reminder: Take {medicine} at {time}"
        )






# ================= AI CHAT =================


elif menu=="AI Health Assistant":


    st.header(
        "🤖 CareCall AI Chat"
    )


    query=st.text_area(
        "Describe your symptoms"
    )


    if st.button(
        "Ask AI"
    ):


        with st.spinner(
            "CareCall AI thinking..."
        ):


            reply=ask_ai(query)


            st.write(reply)