# 🎓 EduPrompt API

**EduPrompt API** is a Flask-based REST API for educational AI queries.

The project connects a **Flask backend** with **MongoDB** for prompt management and transaction history, and uses the **Groq API through the OpenAI Python SDK** to generate AI-powered educational responses.

The API supports both **single educational queries** and **asynchronous batch processing**, while automatically storing query and response information in MongoDB.

---

## 🚀 Features

* 🎓 AI-powered educational question answering
* 🌐 REST API built with Flask
* 🤖 Groq LLM integration using the OpenAI Python SDK
* 🍃 MongoDB integration
* 📝 Dynamic prompt management
* 💾 Automatic query and response history
* ⚡ Asynchronous batch query processing
* 🔐 API key configuration through environment variables
* 📦 Simple and beginner-friendly project structure

---

## 🛠️ Tech Stack

| Technology               | Purpose                        |
| ------------------------ | ------------------------------ |
| 🐍 Python 3.10+          | Programming language           |
| 🌐 Flask                 | REST API framework             |
| 🍃 MongoDB               | Database and history storage   |
| 🤖 Groq API              | Large Language Model inference |
| 📦 OpenAI Python SDK     | LLM API client                 |
| ⚡ AsyncIO                | Asynchronous batch processing  |
| 🔑 Environment Variables | API key management             |

The project uses Flask, MongoDB, and the OpenAI Python SDK with Groq's OpenAI-compatible API endpoint.

---

## 📂 Project Structure

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

---

# 📥 Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/mananvernekar07/EduPrompt_API.git
cd EduPrompt_API
```

---

## 2. Install Dependencies

It is recommended to use a virtual environment.

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Configure Environment Variables

The API requires a **Groq API key**.

### Windows PowerShell

```powershell
$env:GROQ_API_KEY="gsk_your_actual_groq_api_key_here"
```

### Linux / macOS

```bash
export GROQ_API_KEY="gsk_your_actual_groq_api_key_here"
```

---

## 4. Configure MongoDB

Make sure MongoDB is running and that your application is configured with the appropriate MongoDB connection string.

For example:

```text
mongodb://localhost:27017/
```

The application uses MongoDB for:

* System prompt storage
* User query history
* AI response history
* API transaction records

---

## 5. Seed the System Prompt

Run the following command to populate MongoDB with the default educational system prompt:

```bash
python seedprompt.py
```

---

## 6. Start the Flask Server

```bash
python app.py
```

The API will normally be available at:

```text
http://127.0.0.1:5000
```

---

# 🔌 API Endpoints

## 🎓 Single Query

### `POST /api/query`

Send a single educational question to the AI.

### PowerShell

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/query" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"userinput": "How much should I score in each subject to pass CA final?"}'
```

### cURL

```bash
curl -X POST http://127.0.0.1:5000/api/query \
  -H "Content-Type: application/json" \
  -d '{"userinput": "How much should I score in each subject to pass CA final?"}'
```

### Request Body

```json
{
  "userinput": "How much should I score in each subject to pass CA final?"
}
```

---

## ⚡ Batch Query

### `POST /api/batch-query`

Send multiple educational questions for asynchronous processing.

### PowerShell

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/api/batch-query" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"userinputs": ["What is Bloom Taxonomy?", "Explain formative vs summative assessment."]}'
```

### cURL

```bash
curl -X POST http://127.0.0.1:5000/api/batch-query \
  -H "Content-Type: application/json" \
  -d '{"userinputs": ["What is Bloom Taxonomy?", "Explain formative vs summative assessment."]}'
```

### Request Body

```json
{
  "userinputs": [
    "What is Bloom Taxonomy?",
    "Explain formative vs summative assessment."
  ]
}
```

---

# 📊 View Transaction History

The project automatically stores query and response information in MongoDB.

To view the saved transaction history, run:

```bash
python fetchdata.py
```

This allows you to inspect previously processed API requests and their corresponding AI responses.

---

# 🔄 How It Works

```text
                ┌──────────────────┐
                │   Client/User    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │   Flask REST API │
                └────────┬─────────┘
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
     ┌─────────────────┐     ┌─────────────────┐
     │    MongoDB      │     │    Groq API     │
     │                 │     │                 │
     │ Prompts & Logs  │     │   LLM Response  │
     └────────┬────────┘     └────────┬────────┘
              │                       │
              └───────────┬───────────┘
                          ▼
                  ┌───────────────┐
                  │ API Response  │
                  └───────────────┘
```

### Request Flow

1. The client sends an educational question to the Flask API.
2. Flask receives and validates the request.
3. The configured educational system prompt is retrieved from MongoDB.
4. The question and prompt are sent to the Groq LLM through the OpenAI Python SDK.
5. The generated educational response is returned to the client.
6. The query and response information is stored in MongoDB.
7. Batch requests are processed asynchronously using `asyncio`.

---

# 🔐 Security

API credentials should **never be hardcoded** in the source code.

Use environment variables:

```text
GROQ_API_KEY
```

---

# 🧪 Example Questions

You can test the API with educational questions such as:

```text
What is Bloom's Taxonomy?

Explain formative vs summative assessment.

What is the difference between supervised and unsupervised learning?

Explain photosynthesis in simple terms.

How does Newton's second law work?
```

---

# 📌 Future Improvements

Possible improvements for future versions include:

* 🔐 Authentication and authorization
* 🧑‍🎓 User-specific query history
* 📚 Subject/category-based prompts
* 🗄️ Improved MongoDB schema
* 📈 API usage analytics
* 🚦 Rate limiting
* 🧪 Automated API tests
* 🐳 Docker support
* ☁️ Cloud deployment
* 📖 Swagger/OpenAPI documentation
* 🔄 Streaming LLM responses

---

# 👨‍💻 Author

**Manan Vernekar**

GitHub:
https://github.com/mananvernekar07

---

## ⭐ Contributing

Contributions, issues, and feature requests are welcome!

If you find this project useful, consider giving it a ⭐ on GitHub.
