import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

import uuid
from pinecone import Pinecone
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer('all-MiniLM-L6-v2')

def _get_index():
    api_key = os.getenv("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME")

    if not api_key:
        raise ValueError("Missing PINECONE_API_KEY in .env")
    if not index_name:
        raise ValueError("Missing PINECONE_INDEX_NAME in .env")

    pc = Pinecone(api_key=api_key)
    return pc.Index(index_name)

def save_insight(review_text: str, insight: dict) -> str:
    index = _get_index()
    namespace = os.getenv("PINECONE_NAMESPACE", "insights")

    text_to_embed = review_text + '\nProblem: ' + insight['main_problem']
    vector = embedder.encode(text_to_embed).tolist()

    record_id = str(uuid.uuid4())

    metadata = {
        "review" : review_text,
        "sentiment" : insight['sentiment'],
        "main_problem" : insight['main_problem'],
        "business_recommendation" : insight['business_recommendation'],
        "category" : insight['category'],
        "urgency" : insight['urgency']
    }

    index.upsert(
        vectors = [(record_id, vector, metadata)],
        namespace = namespace
    )

    return record_id

def search_similar_reviews(review_text: str, top_k: int = 5) -> list[dict]:
    index = _get_index()
    namespace = os.getenv("PINECONE_NAMESPACE", "insights")

    query_vector = embedder.encode(review_text).tolist()

    result = index.query(
        vector = query_vector,
        top_k = top_k,
        namespace = namespace,
        include_metadata=True
    )

    matches = []
    for m in result.get('matches', []):
        matches.append({
            "id": m['id'],
            "score": m['score'],
            "metadata": m.get("metadata", {})
        })

    return matches




