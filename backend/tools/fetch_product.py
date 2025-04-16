# tools/fetch_product.py

def Tool(name, description=""):
    def decorator(fn):
        fn.tool_name = name
        fn.tool_description = description
        return fn
    return decorator

import requests
import os

@Tool(name="fetch_product_details", description="Fetch product details using Serper API or similar.")
def fetch_product_details(query: str):
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
    headers = {"X-API-KEY": SERPER_API_KEY}
    params = {"q": query, "gl": "us", "hl": "en"}
    res = requests.post("https://google.serper.dev/search", headers=headers, json=params)
    
    products = []
    for r in res.json().get("shopping", []):
        products.append({
            "name": r["title"],
            "price": r.get("price", "N/A"),
            "features": r.get("extensions", [])
        })
    return products
