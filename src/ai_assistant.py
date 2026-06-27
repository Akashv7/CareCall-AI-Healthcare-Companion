from google import genai

import os

from dotenv import load_dotenv

from src.rag_engine import retrieve_context


# ================= LOAD API KEY =================

load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ================= GEMINI MODEL =================

MODEL_NAME = "gemini-2.0-flash"


# ================= OFFLINE HEALTH AI =================

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
✔ Monitor temperature

Prevention:
✔ Maintain hygiene
✔ Eat healthy food

Consult doctor if fever continues.

📚 Source:
Offline CareCall Knowledge
"""


    elif "headache" in message:

        return """
🤖 CareCall AI Analysis

Possible Reason:
- Stress
- Lack of sleep
- Dehydration

Health Suggestions:
✔ Rest properly
✔ Drink enough water
✔ Reduce screen time

📚 Source:
Offline CareCall Knowledge
"""


    elif "chest" in message:

        return """
🤖 CareCall AI Analysis

Possible Heart Related Symptoms

Suggestions:
✔ Monitor BP
✔ Avoid heavy activity
✔ Seek medical help if pain continues

📚 Source:
Offline CareCall Knowledge
"""


    elif "diabetes" in message or "sugar" in message:

        return """
🤖 CareCall AI Analysis

Possible Diabetes Related Symptoms

Suggestions:
✔ Monitor glucose
✔ Maintain healthy diet
✔ Exercise regularly

📚 Source:
Offline CareCall Knowledge
"""


    else:

        return """
🤖 CareCall AI Analysis

General Suggestions:

✔ Maintain proper sleep
✔ Stay hydrated
✔ Eat nutritious food

Consult healthcare professional if symptoms continue.

📚 Source:
Offline CareCall Knowledge
"""



# ================= RAG + GEMINI AI =================

def ask_ai(message):

    try:


        # -------- RAG SEARCH --------

        context, sources = retrieve_context(message)



        # -------- PROMPT --------

        prompt = f"""

You are CareCall AI,
an elderly healthcare assistant.

Use ONLY the verified medical knowledge below.


Medical Knowledge:

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

- Do not prescribe medicines

- Do not give unsafe advice

- Recommend doctor for serious symptoms

"""


        # -------- GEMINI RESPONSE --------

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )


        answer = response.text



        # -------- ADD SOURCES --------

        answer += """

📚 Medical Sources:

"""


        if len(sources) > 0:

            unique_sources = list(set(sources))


            for source in unique_sources:

                answer += f"""
📄 {source}
"""


        else:

            answer += """
CareCall Medical Knowledge Base
"""


        return answer



    except Exception as e:

        print(
            "AI ERROR:",
            e
        )


        return offline_health_ai(message)