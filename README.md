# 🩺 CareCall AI - Elder Healthcare Companion

## AI-Powered Healthcare Monitoring System using Machine Learning + LLM

CareCall AI is an intelligent healthcare companion designed to help elderly users monitor their health conditions using Machine Learning and AI-powered conversational assistance.

The system predicts multiple disease risks, provides confidence scores, stores patient health history, generates reports, and offers AI-based health guidance using Large Language Models (LLM).

---

# 📌 Problem Statement

Elderly people often face difficulties in continuously monitoring their health conditions and understanding early warning symptoms.

Traditional healthcare systems usually work after diagnosis, but early prediction and proactive monitoring can help reduce health risks.

CareCall AI solves this problem by combining:

- Machine Learning prediction models
- AI healthcare assistant
- Patient history tracking
- Automated health recommendations

---

# 🎯 Objectives

- Predict possible health risks using ML models
- Provide AI-based healthcare suggestions
- Maintain patient medical history
- Generate health reports
- Improve accessibility for elderly users
- Build a smart preventive healthcare platform

---

# 🚀 Features

## 🩸 1. Diabetes Risk Prediction

Predicts diabetes possibility using patient health parameters.

### Inputs:

- Age
- Glucose Level
- Blood Pressure
- BMI
- Family Diabetes History


### Output:

- Diabetes Risk Status
- ML Confidence Score
- Health Report


---

## ❤️ 2. Heart Disease Prediction

Analyzes possible heart disease risk.

### Inputs:

- Age
- Gender
- Chest Pain
- Blood Pressure
- Cholesterol
- Heart Rate


### Output:

- Heart Disease Risk
- Prediction Confidence
- Healthcare Suggestions


---

## 🩺 3. Kidney Disease Prediction

Predicts kidney-related health risks.

### Inputs:

- Age
- Blood Pressure
- Sugar Level
- Hemoglobin


### Output:

- Kidney Risk Prediction
- Confidence Percentage


---

# 🤖 AI Health Assistant (LLM)

CareCall AI includes an intelligent chatbot powered by Gemini LLM.

Users can describe symptoms naturally.

Example:

User:

```
I have fever and headache
```

AI Response:

```
Possible Reasons:

- Viral infection
- Dehydration
- Stress

Suggestions:

- Stay hydrated
- Take proper rest
- Monitor symptoms

Consult doctor if symptoms continue.
```

The system also contains an offline fallback AI response mechanism if API limits or network failures occur.

---

# 📊 Machine Learning Models

Multiple ML algorithms were trained and compared.

| Algorithm | Performance |
|---------|------------|
| Logistic Regression | 84% |
| Decision Tree | 88% |
| Random Forest | 94% |


## Selected Algorithm

🌲 Random Forest Classifier


### Why Random Forest?

- Handles healthcare datasets effectively
- Works well with multiple features
- Reduces overfitting
- Provides better accuracy


---

# 🧠 Machine Learning Workflow


```
Dataset Collection

        ↓

Data Cleaning

        ↓

Feature Engineering

        ↓

Model Training

        ↓

Model Evaluation

        ↓

Save Model (.pkl)

        ↓

Deploy with Streamlit
```

---

# 🗄️ Database Integration

SQLite database is integrated for continuous patient monitoring.


## Stored Information

- Patient Name
- Disease Checked
- Risk Level
- Confidence Score
- Date & Time


Database Flow:


```
Patient Input

      ↓

ML Prediction

      ↓

Save Result

      ↓

SQLite Database

      ↓

Patient History Dashboard
```

---

# 🏗️ System Architecture


```

                 User

                  |
                  ↓

        Streamlit Web Application


                  |
        -------------------------

        |                       |


 Machine Learning Engine       LLM Assistant


        |                       |


 Random Forest Models        Gemini API


        |                       |


 Disease Prediction       Health Suggestions


                  |

                  ↓

            SQLite Database


                  |

                  ↓

        Patient History + Reports


```

---

# 🛠️ Technology Stack


## Programming

- Python


## Machine Learning

- Scikit-Learn
- Pandas
- NumPy


## Artificial Intelligence

- Gemini LLM
- Prompt Engineering


## Web Framework

- Streamlit


## Database

- SQLite


## Development Tools

- VS Code
- Git
- GitHub


---

# 📂 Project Structure


```
CareAI

│
├── app.py
│
├── requirements.txt
│
├── carecall.db
│

├── datasets
│
│── diabetes.csv
│
│── heart.csv
│
│── kidney.csv
│

├── models
│
│── diabetes_model.pkl
│
│── heart_model.pkl
│
│── kidney_model.pkl
│

├── src
│
│── prediction.py
│
│── database.py
│
│── ai_assistant.py
│
│── diabetes_train.py
│
│── heart_train.py
│
└── kidney_train.py

```

---

# ⚙️ Installation & Setup


## 1. Clone Repository


```bash
git clone <repository-link>

cd CareAI
```


---

## 2. Install Requirements


```bash
pip install -r requirements.txt
```


---

## 3. Add Gemini API Key


Open:

```
src/ai_assistant.py
```

Add:

```python
api_key="YOUR_API_KEY"
```


---

## 4. Run Application


```bash
python -m streamlit run app.py
```


---

# 📈 Application Modules


```
Dashboard

    |

    |---- Diabetes Prediction

    |

    |---- Heart Prediction

    |

    |---- Kidney Prediction

    |

    |---- Patient History

    |

    |---- Model Performance

    |

    |---- Medicine Reminder

    |

    |---- AI Health Assistant
```


---

# 📄 Report Generation

Each prediction generates:

- Patient Details
- Disease Category
- Risk Level
- Model Confidence


Reports can be downloaded for future reference.

---

# 🔮 Future Enhancements


- Voice-based AI interaction

- Mobile application

- Smart watch integration

- Real-time health monitoring

- Emergency family alerts

- Cloud deployment

- Agentic AI healthcare assistant


---

# 💡 Interview Explanation

CareCall AI is an AI-powered elderly healthcare companion that combines Machine Learning models and Large Language Models to provide preventive healthcare monitoring.

The system predicts disease risks using trained ML models, provides AI recommendations through Gemini LLM, stores patient history using SQLite, and delivers personalized health insights.

---

# 👨‍💻 Developer

Akash V

AI / ML Developer

```
Python | Machine Learning | LLM | Streamlit | SQLite
```
