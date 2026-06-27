from src.database import get_weekly_health_data
from src.ai_assistant import model   # Your Gemini model


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

Keep it under 200 words.
"""

    response = model.generate_content(prompt)

    return response.text