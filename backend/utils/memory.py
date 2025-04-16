from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
supabase = create_client(supabase_url, supabase_key)

def store_message(user_id, message, response):
    supabase.table("chat_memory").insert({
        "user_id": user_id,
        "message": message,
        "response": response
    }).execute()

def get_memory(user_id):
    result = supabase.table("chat_memory").select("*").eq("user_id", user_id).order("id").execute()
    return result.data if result.data else []
