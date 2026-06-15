import google.generativeai as genai




model = genai.GenerativeModel(
    "gemini-2.0-flash"
)



def offline_health_ai(message):


    message = message.lower()


    if "fever" in message:


        return """

🤖 CareCall AI Analysis

Possible Reason:
- Viral infection
- Weather changes
- Weak immunity

Health Suggestions:
✔ Drink enough water
✔ Take proper rest
✔ Monitor temperature

Consult a doctor if:
- Fever continues for more than 2-3 days
- Temperature becomes very high

"""


    elif "headache" in message:


        return """

🤖 CareCall AI Analysis

Possible Reason:
- Stress
- Lack of sleep
- Dehydration

Health Suggestions:
✔ Drink water
✔ Rest properly
✔ Reduce screen time

"""


    elif "chest" in message:


        return """

🤖 CareCall AI Analysis

Possible Heart Related Symptoms.

Suggestions:
✔ Check BP
✔ Avoid heavy activity
✔ Consult doctor if pain continues

"""


    elif "sugar" in message:


        return """

🤖 CareCall AI Analysis

Possible Diabetes Related Symptoms.

Suggestions:
✔ Monitor glucose level
✔ Maintain healthy diet
✔ Exercise regularly

"""


    else:


        return """

🤖 CareCall AI Analysis

Maintain:
✔ Proper sleep
✔ Hydration
✔ Healthy food

Monitor symptoms and consult doctor if needed.

"""





def ask_ai(message):


    prompt=f"""

    You are CareCall AI,
    an elderly healthcare assistant.

    Patient:
    {message}

    Give simple healthcare advice.

    Do not prescribe medicines.

    """


    try:


        response=model.generate_content(
            prompt
        )


        return response.text



    except Exception:


        return offline_health_ai(
            message
        )