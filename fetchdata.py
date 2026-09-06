from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["ca_exam_db"]
history_collection = db["history"]

print("\n--- MONGO DB TRANSACTION HISTORY LOGS ---")
records = list(history_collection.find())

if not records:
    print("No history records found in MongoDB.")
else:
    for idx, doc in enumerate(records, 1):
        log_type = doc.get("type", "single")
        user_in = doc.get("user_input", "N/A")
        ai_out = doc.get("ai_response") or doc.get("response")

        print(f"\n[Record {idx}] | Type: {log_type}")
        print(f"Input : {user_in}")
        print(f"Output: {str(ai_out)[:120]}...")