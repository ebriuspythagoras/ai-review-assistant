from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from ai_review_assistant.config import get_groq_api_key, get_groq_model
from ai_review_assistant.prompts import REVIEW_ANALYSIS_PROMPT


def build_chain():
    api_key = get_groq_api_key()
    model = get_groq_model()

    llm = ChatGroq(
        api_key=api_key,
        model=model,
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template(REVIEW_ANALYSIS_PROMPT)

    chain = prompt | llm
    return chain