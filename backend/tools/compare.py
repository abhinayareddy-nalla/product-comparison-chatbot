# tools/compare.py

def Tool(name, description=""):
    def decorator(fn):
        fn.tool_name = name
        fn.tool_description = description
        return fn
    return decorator


@Tool(name="compare_products", description="Compare two or more products based on features and price.")
def compare_products(product_list: list):
    comparisons = []
    for product in product_list:
        comparisons.append(f"Name: {product['name']}\nPrice: {product['price']}\nFeatures: {', '.join(product['features'])}\n")
    return "\n---\n".join(comparisons)
