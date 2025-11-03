import re

BAD_WORDS = {"idiot", "stupid", "dumb", "fool"}

def contains_bad_language(text):
    words = re.findall(r'\w+', text.lower())
    return any(w in BAD_WORDS for w in words)
