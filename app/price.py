
import random

def get_price_estimate(labels):
    # Dummy-Logik zur Preissimulation
    keywords = ", ".join(labels)
    price = round(random.uniform(5, 50), 2)
    return {
        "keywords": keywords,
        "estimated_price": f"{price} €"
    }
