import streamlit as st

from streamlit_autorefresh import st_autorefresh

from src.report_generator import create_report
from src.database import create_database

create_database()

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
    save_medicine,
    get_user_medicine
)


from src.scheduler import start_scheduler





from src.database import (

    create_database,

    save_history,
    get_history,

    save_medicine,
    get_medicine,

    save_ai_review,
    get_pending_reviews,
    approve_review,
    get_patient_reviews

)





from src.monitoring import (

    create_monitoring,

    save_monitoring,

    get_monitoring,

    check_trend

)





from src.alerts import emergency_alert




from src.auth import (

    login_page,

    register_page

)







# ================= CONFIG =================


st.set_page_config(

    page_title="CareCall AI",

    page_icon="🩺",

    layout="wide"

)






# ================= AUTO REFRESH =================


st_autorefresh(

    interval=60000,

    key="medicine_refresh"

)







# ================= DATABASE =================


create_database()


create_monitoring()


start_scheduler()







# ================= LOGIN =================



if "login" not in st.session_state:


    st.session_state.login=False






if st.session_state.login==False:



    st.title(

        "🩺 CareCall AI Login"

    )



    option=st.sidebar.selectbox(

        "Account",

        [

            "Login",

            "Register"

        ]

    )






    if option=="Login":


        login_page()



    else:


        register_page()





    st.stop()








# ================= TITLE =================



st.title(

    "🩺 CareCall AI - Elder Healthcare Companion"

)





st.write(
"""

AI Healthcare Companion


✔ ML Disease Prediction

✔ RAG + Gemini

✔ Doctor Approval

✔ Emergency Alert

✔ Medicine Reminder

✔ Monitoring


"""
)








# ================= USER =================



st.sidebar.success(

    f"👤 User: {st.session_state.user}"

)



st.sidebar.info(

    f"Role: {st.session_state.role}"

)





if st.sidebar.button(

    "Logout"

):



    st.session_state.login=False



    st.rerun()







# ================= MENU =================



if st.session_state.role=="Patient":



    pages=[


        "Dashboard",


        "Diabetes Prediction",


        "Heart Prediction",


        "Kidney Prediction",


        "Health Monitoring",


        "Medicine Reminder",


        "AI Health Assistant"


    ]






elif st.session_state.role=="Doctor":



    pages=[


        "Dashboard",


        "Patient History",


        "Health Monitoring",


        "Doctor Review",


        "Model Performance"


    ]







else:



    pages=[


        "Dashboard",


        "Patient History",


        "Health Monitoring"


    ]







menu=st.sidebar.selectbox(

    "Services",

    pages

)








# ================= DASHBOARD =================


if menu=="Dashboard":



    st.header(

        "📊 Dashboard"

    )




    c1,c2,c3,c4=st.columns(4)



    c1.metric(

        "ML Models",

        "3"

    )



    c2.metric(

        "Algorithm",

        "Random Forest"

    )



    c3.metric(

        "AI",

        "Gemini + RAG"

    )



    c4.metric(

        "Database",

        "SQLite"

    )





    st.success(

        """

🩸 Diabetes

❤️ Heart

🩺 Kidney

📈 Monitoring

👨‍⚕️ Doctor Approval

🚨 Alerts

"""

    )
# ================= DIABETES =================


elif menu=="Diabetes Prediction":


    st.header(
        "🩸 Diabetes Prediction"
    )


    name=st.text_input(
        "Patient Name"
    )

    age=st.number_input(
        "Age"
    )

    glucose=st.number_input(
        "Glucose"
    )

    bp=st.number_input(
        "Blood Pressure"
    )

    bmi=st.number_input(
        "BMI"
    )


    family=st.selectbox(
        "Family History",
        ["No","Yes"]
    )



    if st.button(
        "Predict Diabetes"
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


        risk="HIGH" if result==1 else "LOW"


        st.info(
            f"Risk: {risk}"
        )


        st.info(
            f"Confidence: {confidence}%"
        )


        save_history(
            name,
            "Diabetes",
            risk,
            confidence
        )
        report=create_report(

            name,

            "Diabetes",

            risk,

            confidence

        )



        with open(

            report,

            "rb"

        ) as file:


            st.download_button(

                "📄 Download Medical Report",

                file,

                file_name="Diabetes_Report.pdf"

            )

        if risk=="HIGH":


            st.warning(

                emergency_alert(

                    name,
                    "Diabetes",
                    confidence

                )

            )









# ================= HEART =================


elif menu=="Heart Prediction":


    st.header(
        "❤️ Heart Prediction"
    )


    name=st.text_input(
        "Patient Name"
    )


    age=st.number_input(
        "Age"
    )


    gender=st.selectbox(
        "Gender",
        ["Female","Male"]
    )


    bp=st.number_input(
        "Blood Pressure"
    )


    cholesterol=st.number_input(
        "Cholesterol"
    )


    heart=st.number_input(
        "Heart Rate"
    )



    if st.button(
        "Predict Heart"
    ):


        data=[

            age,

            1 if gender=="Male" else 0,

            0,

            bp,

            cholesterol,

            0,

            0,

            heart,

            0,

            1,

            1,

            0,

            2

        ]



        result=predict_heart(data)


        confidence=heart_confidence(data)


        risk="HIGH" if result==1 else "LOW"



        st.info(
            f"Risk: {risk}"
        )



        st.info(
            f"Confidence: {confidence}%"
        )



        save_history(

            name,

            "Heart",

            risk,

            confidence

        )

        report=create_report(

            name,

            "Heart Disease",

            risk,

            confidence

        )



        with open(

            report,

            "rb"

        ) as file:


            st.download_button(

                "📄 Download Medical Report",

                file,

                file_name="Heart_Report.pdf"

            )


        if risk=="HIGH":


            st.warning(

                emergency_alert(

                    name,

                    "Heart",

                    confidence

                )

            )



# ================= KIDNEY =================


elif menu=="Kidney Prediction":


    st.header(
        "🩺 Kidney Prediction"
    )


    name=st.text_input(
        "Patient Name"
    )


    age=st.number_input(
        "Age"
    )


    bp=st.number_input(
        "Blood Pressure"
    )


    hemo=st.number_input(
        "Hemoglobin"
    )



    if st.button(
        "Predict Kidney"
    ):



        data=[

            age,
            bp,
            1.020,
            0,
            0,
            120,
            40,
            1.2,
            hemo,
            40

        ]



        result=predict_kidney(data)


        confidence=kidney_confidence(data)



        risk="HIGH" if result==1 else "LOW"



        st.info(
            f"Risk: {risk}"
        )



        save_history(

            name,

            "Kidney",

            risk,

            confidence

        )
        report=create_report(

            name,

            "Kidney Disease",

            risk,

            confidence

        )



        with open(

            report,

            "rb"

        ) as file:


            st.download_button(

                "📄 Download Medical Report",

                file,

                file_name="Kidney_Report.pdf"

            )


# ================= MONITORING =================


elif menu=="Health Monitoring":



    st.header(
        "📈 Health Monitoring"
    )



    name=st.text_input(
        "Patient"
    )



    bp=st.number_input(
        "BP"
    )



    glucose=st.number_input(
        "Glucose"
    )



    heart=st.number_input(
        "Heart Rate"
    )



    risk=st.selectbox(

        "Risk",

        ["LOW","HIGH"]

    )





    if st.button(
        "Save Record"
    ):



        save_monitoring(

            name,

            bp,

            glucose,

            heart,

            risk

        )



        st.success(
            "Saved"
        )






    if st.button(
        "View Timeline"
    ):



        records=get_monitoring(

            name

        )



        st.write(

            records

        )



        st.warning(

            check_trend(

                records

            )

        )

# ================= HISTORY =================

elif menu=="Patient History":


    st.header(
        "📄 Patient Records"
    )


    records = get_history()


    if len(records)==0:

        st.info(
            "No patient records available"
        )


    for r in records:


        st.success(
            f"""

Patient: {r[1]}

Disease: {r[2]}

Risk: {r[3]}

Confidence: {r[4]}%

Date: {r[5]}

"""
        )


        if r[3]=="HIGH":


            st.error(
                f"""

🚨 Emergency Alert

Patient {r[1]} has HIGH {r[2]} Risk

Please check immediately

"""
            )




# ================= MODEL =================


elif menu=="Model Performance":



    st.header(
        "📊 Model Performance"
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









## ================= MEDICINE =================

elif menu == "Medicine Reminder":

    st.header("💊 Medicine Reminder")

    medicine = st.text_input("Medicine Name")

    dosage = st.text_input("Dosage (Example: 500 mg)")

    frequency = st.selectbox(

        "Frequency",

        [

            "Daily",

            "Alternate Day",

            "Weekly"

        ]

    )

    start_date = st.date_input("Start Date")

    end_date = st.date_input("End Date")

    time = st.time_input("Medicine Time")

    if st.button("Save Medicine"):

        save_medicine(

            st.session_state.user,

            medicine,

            dosage,

            frequency,

            str(start_date),

            str(end_date),

            str(time)

        )

        st.success("✅ Medicine Saved Successfully")

        st.info("📧 Email and 📞 Voice reminders will be sent automatically.")

    st.subheader("Your Medicines")

    medicines = get_user_medicine(st.session_state.user)

    for med in medicines:

        st.write("Patient :", med[1])

        st.write("Medicine :", med[2])

        st.write("Dosage :", med[3])

        st.write("Frequency :", med[4])

        st.write("Start Date :", med[5])

        st.write("End Date :", med[6])

        st.write("Time :", med[7])

        st.divider()









# ================= AI CHAT =================

elif menu=="AI Health Assistant":

    st.header(
        "🤖 CareCall AI Assistant"
    )


    query = st.text_area(
        "Describe symptoms"
    )


    if st.button("Ask AI"):

        if query.strip() == "":

            st.warning(
                "Please enter symptoms"
            )

        else:

            response = ask_ai(query)


            st.write(response)


            save_ai_review(
                st.session_state.user,
                query,
                response
            )


            st.success(
                "Request sent to doctor approval 👨‍⚕️"
            )


    st.subheader(
        "Doctor Approved Advice"
    )


    reviews = get_patient_reviews(
        st.session_state.user
    )


    for r in reviews:

        if r[5]=="APPROVED":

            st.success(
                r[4]
            )







    st.subheader(
        "Doctor Approved Advice"
    )



    reviews=get_patient_reviews(

        st.session_state.user

    )



    for r in reviews:



        if r[5]=="APPROVED":



            st.success(

                r[4]

            )









# ================= DOCTOR REVIEW =================


elif menu=="Doctor Review":



    st.header(
        "👨‍⚕️ Doctor Approval Dashboard"
    )



    reviews=get_pending_reviews()




    if len(reviews)==0:



        st.success(

            "No pending requests"

        )







    for r in reviews:



        st.write(
            "Patient:",
            r[1]
        )



        st.write(
            "Question:",
            r[2]
        )



        st.warning(
            "AI Suggestion"
        )



        st.write(
            r[3]
        )




        doctor_reply=st.text_area(

            "Doctor Advice",

            key=r[0]

        )




        if st.button(

            "Approve",

            key="approve"+str(r[0])

        ):



            approve_review(

                r[0],

                doctor_reply

            )



            st.success(
                "Approved Successfully"
            )



            st.rerun()