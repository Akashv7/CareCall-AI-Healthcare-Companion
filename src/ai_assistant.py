import google.generativeai as genai
import os

from dotenv import load_dotenv

from src.rag_engine import retrieve_context


# ================= LOAD API KEY =================

load_dotenv()


genai.configure(

    api_key=os.getenv(
        "GEMINI_API_KEY"
    )

)



# ================= GEMINI MODEL =================


model = genai.GenerativeModel(

    "gemini-2.0-flash"

)





# ================= OFFLINE AI =================


def offline_health_ai(message):


    message = message.lower()



    if "fever" in message:


        return """

🤖 CareCall AI Analysis

Possible Reason:
- Viral infection
- Seasonal changes
- Weak immunity


Health Suggestions:
✔ Drink enough water
✔ Take proper rest
✔ Monitor body temperature


Prevention:
✔ Maintain hygiene
✔ Eat healthy food


Consult doctor if:
- Fever continues for several days
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
✔ Drink enough water
✔ Rest properly
✔ Reduce screen time


"""



    elif "chest" in message:


        return """

🤖 CareCall AI Analysis

Possible Heart Related Symptoms


Suggestions:
✔ Monitor BP
✔ Avoid heavy physical activity
✔ Seek medical help if pain continues


"""



    elif "sugar" in message or "diabetes" in message:


        return """

🤖 CareCall AI Analysis

Possible Diabetes Related Symptoms


Suggestions:
✔ Monitor glucose level
✔ Maintain healthy diet
✔ Exercise regularly


"""



    elif "urine" in message or "kidney" in message:


        return """

🤖 CareCall AI Analysis

Possible Kidney Related Symptoms


Suggestions:
✔ Drink adequate water
✔ Monitor symptoms
✔ Consult healthcare professional


"""



    else:


        return """

🤖 CareCall AI Analysis


General Suggestions:

✔ Maintain proper sleep
✔ Stay hydrated
✔ Eat nutritious food
✔ Monitor symptoms


Consult doctor if symptoms continue.

"""







# ================= RAG + GEMINI AI =================


def ask_ai(message):


    try:


        # -------- Retrieve medical knowledge --------

        context = retrieve_context(

            message

        )



        prompt = f"""


You are CareCall AI,
an elderly healthcare assistant.


Use the verified medical knowledge below:


{context}



Patient Symptoms:

{message}



Provide:

1. Possible reason

2. Health suggestions

3. Prevention tips

4. When to consult doctor



Rules:

- Explain simply
- Do not prescribe medicine
- Do not provide dangerous advice


"""



        response = model.generate_content(

            prompt

        )



        return response.text





    except Exception:


        return offline_health_ai(

            message

        )