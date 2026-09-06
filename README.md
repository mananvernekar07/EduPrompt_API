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
├── .env.example
│   └── Environment variable template
│
├── .gitignore
│   └── Files excluded from Git
│
└── README.md
    └── Project documentation
