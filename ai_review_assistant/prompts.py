REVIEW_ANALYSIS_PROMPT = """
You are an AI assistant for analyzing customer feedback.

Review:
{review}

Return ONLY a valid JSON object (no extra text).
The JSON MUST contain exactly these keys:
- sentiment
- main_problem
- business_recommendation
- category
- urgency

Allowed values:
- sentiment: "positive" | "neutral" | "negative"
- category: "billing" | "ux" | "bugs" | "support" | "performance" | "other"
- urgency: integer from 1 to 5

Example format:
{{
  "sentiment": "negative",
  "main_problem": "brief description",
  "business_recommendation": "what to improve or do",
  "category": "support",
  "urgency": 4
}}
"""