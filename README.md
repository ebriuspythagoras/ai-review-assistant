# AI Customer Review Assistant
AI-system for analyzing customer feedback using large language models and vector databases.

## Business Problem
Companies receive large volumes of unstructured customer feedback.
Manual analysis is slow, subjective, unscalable and expensive.
This project demonstrates how LLMs can be used to automatically extract structured insights from customer reviews.

## What the system does
- analyzes customer sentiment
- identifies main customer problems
- generates business recommendations
- stores insights in a vector database (Pinecone)
- enables semantic search over historical reviews
- provides basic analytics to identify top customer issues

## System Architecture
1. User provides customer review
2. LLM (Llama 3 via Groq API) analyzes the text
3. Structured JSON insight is generated
4. Insight is saved to Pinecone vector database
5. Embeddings enable semantic search
6. Analytics module aggregates customer problems

## Tech Stack
- Python 3.12
- LangChain
- Llama 3 via Groq API
- Pinecone (vector database)
- Sentence Transformers (embeddings)
- dotenv (environment configuration)

## Project Structure
ai_review_assistant/
├── chains.py        # LLM pipeline
├── pipeline.py      # business logic
├── prompts.py       # prompt templates
├── schemas.py       # output structure
├── insights_db.py   # Pinecone integration
├── analytics.py     # basic insights analytics

## Setup
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Create .env file
5. Run the project

## Environment Variables
Create a `.env` file based on `.env.example`:
GROQ_API_KEY=your_api_key_here
GROQ_MODEL=your_groq_model_here
PINECONE_API_KEY=your_api_key_here
PINECONE_INDEX_NAME=customer-insights
PINECONE_NAMESPACE=insights

## Example
Input:
"Horrible customer service! Your site is too slow!"
Output:
{
  "sentiment": "negative",
  "main_problem": "slow website and poor support",
  "business_recommendation": "improve performance monitoring and customer support response time",
  "category": "performance",
  "urgency": 4
}

## Learning Goals
This project was created as a hands-on learning exercise to:
- understand how LLMs work
- practice prompt engineering
- learn vector databases and embeddings
- build end-to-end AI systems
- connect business problems with AI solutions

## Future Improvements
- batch processing of reviews
- clustering similar customer complaints with ML-algorithms
- simple dashboard for insights visualization
