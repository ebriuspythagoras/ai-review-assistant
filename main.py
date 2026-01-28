from ai_review_assistant.analytics import get_top_problems
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    n_top = 2
    print(f"Here are top {n_top} main customer problems: {get_top_problems(n_top).get('top_categories', [])}")