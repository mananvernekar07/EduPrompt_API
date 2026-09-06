from pymongo import MongoClient

mongo_client = MongoClient("mongodb://localhost:27017/")
db = mongo_client["ca_exam_db"]
prompts_collection = db["prompts"]

prompts_collection.update_one(
    {"_id": "Education_Prompt"},
    {
        "$set": {
            "template": (
                "You are an expert in the education domain. Provide a concise,"
                " direct, 2-3 sentence answer to the following query without"
                " unnecessary fluff: {{userinput}}"
            )
        }
    },
    upsert=True,
)

print(
    "[SUCCESS] Updated 'Education_Prompt' in MongoDB to produce concise"
    " responses."
)