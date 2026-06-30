from src.database import get_weekly_health_data

from src.ai_assistant import client, MODEL_NAME


def generate_weekly_summary(patient):

    health, medicine = get_weekly_health_data(patient)

    prompt = f"""
You are an experienced healthcare assistant.

Patient Name:
{patient}

Health Records:
{health}

Medicine Records:
{medicine}

Generate a professional weekly health summary.

Include:

1. Overall Health

2. Blood Pressure Trend

3. Glucose Trend

4. Heart Rate Trend

5. Medicine Adherence

6. Health Risks

7. Lifestyle Suggestions

8. Doctor Recommendation

Keep the report under 200 words.
"""

    try:

        response = client.models.generate_content(

            model=MODEL_NAME,

            contents=prompt

        )

        return response.text

    except Exception as e:

        print("WEEKLY SUMMARY ERROR:", e)

        return "Unable to generate weekly health summary."