from twilio.rest import Client
import os
from dotenv import load_dotenv

# ================= LOAD ENV =================

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")


# ================= MAKE VOICE CALL =================

def make_call(phone, message):

    print("\n========== TWILIO DEBUG ==========")

    try:

        print("make_call() function called")

        # Check credentials
        if not ACCOUNT_SID:
            print("❌ TWILIO_ACCOUNT_SID Missing")
            return False

        if not AUTH_TOKEN:
            print("❌ TWILIO_AUTH_TOKEN Missing")
            return False

        if not TWILIO_PHONE:
            print("❌ TWILIO_PHONE Missing")
            return False

        if not phone:
            print("❌ Destination phone number missing")
            return False

        print("ACCOUNT SID :", ACCOUNT_SID[:10] + "...")
        print("FROM NUMBER :", TWILIO_PHONE)
        print("TO NUMBER   :", phone)

        client = Client(
            ACCOUNT_SID,
            AUTH_TOKEN
        )

        voice_message = message.replace("\n", " ")

        print("Creating call...")

        call = client.calls.create(

            twiml=f"""
<Response>
    <Say voice="alice" language="en">
        {voice_message}
    </Say>
</Response>
""",

            from_=TWILIO_PHONE,

            to=phone

        )

        print("✅ CALL CREATED SUCCESSFULLY")
        print("CALL SID :", call.sid)

        return True

    except Exception as e:

        print("\n❌ TWILIO CALL FAILED")
        print(type(e).__name__)
        print(str(e))

        return False