from collections import Counter
from ai_review_assistant.insights_db import _get_index
import os

def get_top_problems(top_n : int = 5) -> dict:
    index = _get_index()
    namespace = os.getenv("PINECONE_NAMESPACE", "insights")

    id_list = []
    for ids in index.list(namespace=namespace):
        id_list.extend(ids)

    vectors = index.fetch(ids=id_list, namespace=namespace).get('vectors', {})

    category_counter, problem_counter = Counter(), Counter()
    for ids, item in vectors.items():
        category = item.get('metadata').get('category')
        problem = item.get('metadata').get('main_problem')
        category_counter[category] += 1
        problem_counter[problem] += 1

    return {
        "total_records": len(id_list),
        "top_categories": category_counter.most_common(top_n),
        "top_main_problems": problem_counter.most_common(top_n)
    }
