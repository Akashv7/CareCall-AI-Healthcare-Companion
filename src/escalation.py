from src.database import (
    get_pending_medicine,
    increase_retry,
    get_family_phone
)

from src.voice_call import make_call


def check_escalation():

    pending = get_pending_medicine()

    for record in pending:

        record_id = record[0]

        patient = record[1]

        medicine = record[2]

        retry = record[5]

        phone = get_family_phone(patient)

        if retry < 2:

            if phone:

                make_call(

                    phone,

                    f"""

Hello.

This is CareCall AI.

Reminder.

{patient} has not yet confirmed taking

{medicine}.

Please remind the patient immediately.

Thank you.

"""

                )

            increase_retry(record_id)

            print("Escalation Reminder Sent")