from gtts import gTTS
import os

VOICE_FOLDER = "voice_files"

if not os.path.exists(VOICE_FOLDER):
    os.makedirs(VOICE_FOLDER)


def create_tamil_voice(patient, medicine, medicine_time):

    message = f"""
வணக்கம்.

இது CareCall AI.

{patient} அவர்களுக்கு

{medicine} மருந்தை

{medicine_time} மணிக்கு

எடுத்துக்கொள்ள வேண்டிய நேரம் வந்துவிட்டது.

தயவுசெய்து மருந்தை எடுத்துக்கொள்ளுங்கள்.

நன்றி.
"""

    filename = os.path.join(
        VOICE_FOLDER,
        "tamil_reminder.mp3"
    )

    tts = gTTS(
        text=message,
        lang="ta",
        slow=False
    )

    tts.save(filename)

    return filename