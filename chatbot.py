import random

def load_data():
    files = ["data/hr_policies.txt", "data/it_support.txt", "data/company_events.txt"]
    data = {}
    for f in files:
        with open(f, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    q, a = line.strip().split(":", 1)
                    data[q.lower()] = a.strip()
    return data

faq_data = load_data()

def get_response(user_input):
    user_input = user_input.lower()
    for q, a in faq_data.items():
        if q in user_input:
            return a
    return random.choice([
        "I'm not sure about that. Please check with HR.",
        "Let me check with the IT department.",
        "Can you please rephrase your question?"
    ])
