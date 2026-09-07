# 🎓 EduPrompt API

EduPrompt API is a **Flask-based REST API for educational AI queries**.

The project connects a Flask backend with **MongoDB** for prompt management and transaction history, and uses the **Groq API through the OpenAI Python SDK** to generate AI-powered educational responses.

The API supports both **single educational queries** and **asynchronous batch processing**, while automatically storing query and response information in MongoDB.

---

## 🚀 Features

- 🎓 AI-powered educational question answering
- 🌐 REST API built with Flask
- 🤖 Groq LLM integration using the OpenAI SDK
- 🍃 MongoDB integration
- 📝 Dynamic prompt management
- 💾 Automatic query and response history
- ⚡ Asynchronous batch query processing
- 🔐 API key configuration through environment variables
- 📦 Simple and beginner-friendly project structure

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| 🐍 Python 3.10+ | Programming language |
| 🌐 Flask | REST API framework |
| 🍃 MongoDB | Database and history storage |
| 🤖 Groq API | Large Language Model inference |
| 📦 OpenAI Python SDK | LLM API client |
| ⚡ AsyncIO | Asynchronous batch processing |
| 🔑 Environment Variables | API key management |

The current project uses Flask, MongoDB, and the OpenAI Python SDK with Groq's OpenAI-compatible endpoint. :contentReference[oaicite:1]{index=1}

---

# 📂 Project Structure

```text
EduPrompt_API/
│
├── app.py
│   └── Main Flask REST API
│
├── seedprompt.py
│   └── Adds/updates the educational prompt in MongoDB
│
├── fetchdata.py
│   └── Displays stored API transaction history
│
├── requirements.txt
│   └── Python dependencies
│
└── README.md
    └── Project documentation
```
## 📥 How to Clone & Setup

1. Clone the Repository

git clone [https://github.com/mananvernekar07/EduPrompt_API.git(https://github.com/mananvernekar07/EduPrompt_API.git)cd EduPrompt_API


2. Install Dependencies

pip install -r requirements.txt


3. Configure Environment Variables

$env:GROQ_API_KEY="gsk_your_actual_groq_api_key_here"


4. Seed System Prompt (Populate MongoDB with the default system prompt configuration)

python seedprompt.py


5. Start the Server

python app.py


6. Single Query Endpoint (POST /api/query)

PowerShell (Windows):
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/query" -Method Post -ContentType "application/json" -Body '{"userinput": "How much should I score in each subject to pass CA final?"}'

cURL (Linux / macOS / Git Bash):
curl -X POST [http://127.0.0.1:5000/api/query](http://127.0.0.1:5000/api/query) \
     -H "Content-Type: application/json" \
     -d '{"userinput": "How much should I score in each subject to pass CA final?"}'
     

7. Batch Query Endpoint (POST /api/batch-query)

PowerShell (Windows):
Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/batch-query" -Method Post -ContentType "application/json" -Body '{"userinputs": ["What is Bloom Taxonomy?", "Explain formative vs summative assessment."]}'

cURL (Linux / macOS / Git Bash):
curl -X POST [http://127.0.0.1:5000/api/batch-query](http://127.0.0.1:5000/api/batch-query) \
     -H "Content-Type: application/json" \
     -d '{"userinputs": ["What is Bloom Taxonomy?", "Explain formative vs summative assessment."]}'
     

8. Viewing Saved History Logs
python fetchdata.py
