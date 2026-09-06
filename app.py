import asyncio
import os
from flask import Flask, jsonify, request
from openai import AsyncOpenAI, OpenAI
from pymongo import MongoClient

app = Flask(__name__)

# --- CONFIGURATION ---
API_KEY = os.environ.get("GROQ_API_KEY")
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
MODEL_NAME = "openai/gpt-oss-120b"

# OpenAI SDK Clients
client = OpenAI(api_key=API_KEY, base_url=GROQ_BASE_URL)
async_client = AsyncOpenAI(api_key=API_KEY, base_url=GROQ_BASE_URL)

# MongoDB Connection Setup
try:
    mongo_client = MongoClient(
        "mongodb://localhost:27017/", serverSelectionTimeoutMS=2000
    )
    mongo_client.admin.command("ping")
    db = mongo_client["ca_exam_db"]
    prompts_collection = db["prompts"]
    history_collection = db["history"]
    print("[EduPrompt_API] Connected to MongoDB database: ca_exam_db")
except Exception as e:
    print(f"[EduPrompt_API Error] MongoDB Connection Failed: {e}")


# --- STEP 1 TO 5: SINGLE QUERY ENDPOINT ---
@app.route("/api/query", methods=["POST"])
def handle_user_query():
    data = request.get_json()
    if not data or "userinput" not in data:
        return (
            jsonify({"status": "error", "message": "'userinput' is required."}),
            400,
        )

    user_input = data["userinput"]

    # Step 2: Fetch prompt template from MongoDB
    prompt_doc = prompts_collection.find_one({"_id": "Education_Prompt"})
    if not prompt_doc:
        return (
            jsonify(
                {"status": "error", "message": "Prompt template not found."}
            ),
            500,
        )

    # Step 3: Replace template placeholder and execute LLM call
    template = prompt_doc["template"]
    final_prompt = template.replace("{{userinput}}", user_input)

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": final_prompt}],
        )
        ai_response = completion.choices[0].message.content
    except Exception as e:
        return (
            jsonify(
                {"status": "error", "message": f"LLM API Error: {str(e)}"}
            ),
            500,
        )

    # Step 4: Persist transaction pair into history collection
    history_collection.insert_one(
        {
            "user_input": user_input,
            "final_prompt": final_prompt,
            "ai_response": ai_response,
            "type": "single",
        }
    )

    # Step 5: Return JSON response
    return jsonify({"response": ai_response}), 200


# --- STEP 6: ASYNCHRONOUS BATCH QUERY ENDPOINT ---
async def call_llm_async(user_input, template):
    """Helper function to execute LLM call and persist history asynchronously."""
    final_prompt = template.replace("{{userinput}}", user_input)

    try:
        completion = await async_client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": final_prompt}],
        )
        ai_response = completion.choices[0].message.content
    except Exception as e:
        ai_response = f"Error processing query: {str(e)}"

    # Save individual batch transaction to MongoDB
    history_collection.insert_one(
        {
            "user_input": user_input,
            "final_prompt": final_prompt,
            "ai_response": ai_response,
            "type": "batch_item",
        }
    )

    return ai_response


@app.route("/api/batch-query", methods=["POST"])
def handle_batch_query():
    data = request.get_json()
    if (
        not data
        or "userinputs" not in data
        or not isinstance(data["userinputs"], list)
    ):
        return (
            jsonify(
                {
                    "status": "error",
                    "message": "'userinputs' list field is required.",
                }
            ),
            400,
        )

    user_inputs = data["userinputs"]

    prompt_doc = prompts_collection.find_one({"_id": "Education_Prompt"})
    if not prompt_doc:
        return (
            jsonify(
                {"status": "error", "message": "Prompt template not found."}
            ),
            500,
        )

    template = prompt_doc["template"]

    # Gather tasks for concurrent asynchronous processing
    async def process_all():
        tasks = [call_llm_async(inp, template) for inp in user_inputs]
        return await asyncio.gather(*tasks)

    responses = asyncio.run(process_all())

    return jsonify({"responses": responses}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)