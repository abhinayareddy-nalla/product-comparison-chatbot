import google.generativeai as genai

# Function to compare products using Gemini
def compare_products(user_input: str) -> str:
    # Send the user input to Gemini for a real-time response
    prompt = f"Compare the following products based on features, price, and reviews: {user_input}"
    response = genai.GenerativeModel("gemini-1.5-pro").generate_content(prompt)
    
    if hasattr(response, 'text'):
        return response.text
    else:
        return "I couldn't compare the products at this moment."

# Function to fetch product details using Gemini
def fetch_product_details(user_input: str) -> str:
    # Send the user input to Gemini to fetch detailed information
    prompt = f"Provide detailed information about this product: {user_input}"
    response = genai.GenerativeModel("gemini-1.5-pro").generate_content(prompt)
    
    if hasattr(response, 'text'):
        return response.text
    else:
        return "I couldn't retrieve product details at this moment."
