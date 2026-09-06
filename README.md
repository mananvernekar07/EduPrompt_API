# EduPrompt_API 🚀

EduPrompt_API is a Flask-based REST API designed to process educational LLM queries. It features dynamic NoSQL prompt management, asynchronous batch execution, and automatic transaction audit logging in MongoDB.

---

## 🛠️ Tech Stack
* **Language:** Python 3.10+
* **Framework:** Flask
* **Database:** MongoDB (`mongodb://localhost:27017/`)
* **LLM Client:** OpenAI Python SDK (Groq / OpenAI compatible)

---

## 📂 Project Structure
```text
EduPrompt_API/
├── app.py              # Main Flask REST API
├── seedprompt.py       # MongoDB seeding script
├── fetchdata.py        # Audit history viewer
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
└── README.md           # Documentation