from datetime import datetime

from src.reminder_message import generate_english_reminder

from src.database import (
    get_medicine,
    get_family_email,
    get_family_phone,
    save_medicine_status
)

from src.notification import send_email
from src.voice_call import make_call


# ================= MEMORY CACHE =================

sent_reminders = set()


# ================= MEDICINE CHECKER =================

def check_medicine_time():

    medicines = get_medicine()

    current_time = datetime.now().strftime("%H:%M")

    today = datetime.now().date()

    for med in medicines:

        patient = med[1]
        medicine = med[2]
        dosage = med[3]
        frequency = med[4]
        start_date = med[5]
        end_date = med[6]
        medicine_time = med[7][:5]

        # ================= DATE CHECK =================

        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()

        if not (start <= today <= end):
            continue

        # ================= FREQUENCY CHECK =================

        if frequency == "Alternate Day":

            days = (today - start).days

            if days % 2 != 0:
                continue

        elif frequency == "Weekly":

            if today.weekday() != start.weekday():
                continue

        # Daily → no extra check

        reminder_id = f"{patient}_{medicine}_{medicine_time}_{today}"

        if current_time == medicine_time and reminder_id not in sent_reminders:

            family_email = get_family_email(patient)
            family_phone = get_family_phone(patient)

            # ================= EMAIL MESSAGE =================

            message = f"""
💊 CARECALL MEDICINE REMINDER

Hello Family,

Patient : {patient}

Medicine : {medicine}

Dosage : {dosage}

Time : {medicine_time}

Please remind the patient to take the medicine.

Thank you.

- CareCall AI
"""

            # ================= SEND EMAIL =================

            if family_email:

                send_email(
                    family_email,
                    "💊 CareCall Medicine Reminder",
                    message
                )

            # ================= SAVE STATUS =================

            save_medicine_status(
                patient,
                medicine,
                medicine_time
            )

            # ================= VOICE CALL =================

            if family_phone:

                call_message = generate_english_reminder(
                    patient,
                    medicine,
                    medicine_time
                )

                make_call(
                    family_phone,
                    call_message
                )

            # ================= REMINDER CACHE =================

            sent_reminders.add(reminder_id)

            print(f"MEDICINE REMINDER SENT : {patient}")

            return True

    return False