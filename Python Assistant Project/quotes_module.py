# quotes_module.py
import requests
import random

def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random", timeout=5)
        data = response.json()
        quote = data.get("content")
        author = data.get("author")
        return f"{quote} — {author}"
    except Exception:

        quotes = [
            "Believe you can and you're halfway there. — Theodore Roosevelt",
            "The future depends on what you do today. — Mahatma Gandhi",
            "Don’t watch the clock; do what it does. Keep going. — Sam Levenson",
            "Success is not final, failure is not fatal: it is the courage to continue that counts. — Winston Churchill",
            "It always seems impossible until it’s done. — Nelson Mandela"
        ]
        return random.choice(quotes)
