import streamlit as st

from src.database import (
    get_medicine_status,
    update_medicine_status
)

st.set_page_config(
    page_title="Family Dashboard",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Family Medicine Confirmation")

records = get_medicine_status()

if not records:

    st.info("No medicine reminders available.")

else:

    for record in records:

        record_id = record[0]
        patient = record[1]
        medicine = record[2]
        medicine_time = record[3]
        status = record[4]
        retry = record[5]
        taken_time = record[6]

        with st.container():

            st.subheader(f"👤 {patient}")

            st.write(f"**💊 Medicine :** {medicine}")
            st.write(f"**🕒 Scheduled Time :** {medicine_time}")
            st.write(f"**📌 Status :** {status}")
            st.write(f"**🔁 Retry Count :** {retry}")

            if taken_time:
                st.write(f"**✅ Taken At :** {taken_time}")

            if status == "Pending":

                if st.button(
                    "✅ Medicine Taken",
                    key=f"taken_{record_id}"
                ):

                    update_medicine_status(record_id)

                    st.success("Medicine marked as Taken.")

                    st.rerun()

            else:

                st.success("Medicine already confirmed.")

            st.divider()