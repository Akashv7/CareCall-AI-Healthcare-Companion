import streamlit as st
from src.weekly_summary import generate_weekly_summary
from src.database import (
    get_total_patients,
    get_pending_count,
    get_taken_count,
    get_medicine_status
)

st.set_page_config(
    page_title="Doctor Dashboard",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 CareCall Doctor Dashboard")

# ================= KPI CARDS =================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👨‍⚕️ Total Patients",
        get_total_patients()
    )

with col2:
    st.metric(
        "💊 Pending Medicines",
        get_pending_count()
    )

with col3:
    st.metric(
        "✅ Medicines Taken",
        get_taken_count()
    )

st.divider()

st.subheader("💊 Medicine Status")

records = get_medicine_status()

if len(records) == 0:

    st.info("No medicine records found.")

else:

    for record in records:

        st.write("---")

        st.write(f"👤 **Patient :** {record[1]}")
        st.write(f"💊 **Medicine :** {record[2]}")
        st.write(f"🕒 **Time :** {record[3]}")
        st.write(f"📌 **Status :** {record[4]}")
        st.write(f"🔁 **Retry :** {record[5]}")

        if record[6]:
            st.success(f"Taken at : {record[6]}")
st.divider()

patient = st.text_input(
    "Enter Patient Name"
)

if st.button("Generate AI Weekly Summary"):

    summary = generate_weekly_summary(patient)

    st.subheader("🤖 AI Weekly Health Summary")

    st.write(summary)