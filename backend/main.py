from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from tools import compare_products, fetch_product_details

# Initialize Gemini with your API key
genai.configure(api_key="AIzaSyBcjHfJ8O9eN-N0b_kh6sOan7sSWS2gCAE")  # Replace with your actual Gemini API key
model = genai.GenerativeModel("gemini-1.5-pro")

# Memory manager
user_memory = {}

# FastAPI app
app = FastAPI()

# CORS Middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Adjust for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for incoming chat requests
class ChatRequest(BaseModel):
    user_id: str
    message: str

# Simple agent class with memory functionality
class Agent:
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.memory = user_memory.setdefault(user_id, [])

    def remember(self, message: str):
        self.memory.append(message)
        if len(self.memory) > 20:
            self.memory.pop(0)

    def build_prompt(self, user_input: str):
        history = "\n".join(self.memory)
        return f"{history}\nUser: {user_input}\nAI:"

    def reply(self, user_input: str) -> str:
        self.remember(f"User: {user_input}")
        prompt = self.build_prompt(user_input)

        # Check for specific commands like "compare" or "details"
        if "compare" in user_input.lower():
            return compare_products(user_input)  # This calls the function for real responses
        elif "details" in user_input.lower():
            return fetch_product_details(user_input)  # Fetches real product details

        # Generate response using Gemini
        response = model.generate_content(prompt)
        if hasattr(response, 'text'):
            ai_response = response.text
        else:
            ai_response = "Sorry, I couldn’t understand that."

        self.remember(f"AI: {ai_response}")
        return ai_response

# Endpoint to handle chat requests
@app.post("/chat")
async def chat(request: ChatRequest):
    agent = Agent(request.user_id)
    reply = agent.reply(request.message)
    return {"response": reply}
