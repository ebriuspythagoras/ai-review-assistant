import json

from ai_review_assistant.config import load_env
from ai_review_assistant.chains import build_chain
from ai_review_assistant.schemas import REQUIRED_KEYS, ALLOWED_SENTIMENTS, ALLOWED_CATEGORIES

def analyze_review(review: str) -> dict:
    load_env()
    chain = build_chain()
    response = chain.invoke({'review': review})
    text = response.content

    data = json.loads(text)

    for key in REQUIRED_KEYS:
        if key not in data:
            raise KeyError(f"Required key {key} is missing")

    if data["sentiment"] not in ALLOWED_SENTIMENTS:
        raise KeyError(f"Sentiment {data["sentiment"]} is not allowed")

    if data["category"] not in ALLOWED_CATEGORIES:
        raise KeyError(f"Category {data["category"]} is not allowed")

    urg = data["urgency"]
    if not isinstance(urg, int) or urg < 1 or urg > 5:
        raise KeyError(f"Urgency {urg} is not allowed! The value must be between 1 and 5")

    return data
