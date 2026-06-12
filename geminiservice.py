from google.generativeai.client import configure
from google.generativeai.generative_models import GenerativeModel
import json
import os

# Configure the Gemini API key
configure(api_key=os.getenv("GEMINI_API_KEY","AQ.Ab8RN6Kc70DBd42vY8rHo8x5jRe9_CqxwYZ-WpMqhCFe2E1xPQ"))
model = GenerativeModel('gemini-2.5-flash')    

def analyze_reviews(reviews_text: str) -> dict:
    prompt = f"""
    Here are some customer reviews :
    {reviews_text}
    
    Analyse these reviews and return ONLY a JSON with this exact structure :
    {{
        "score": 75,
        "positiveAspects": [
            {{"name": "Customer service", "count": 3, "evidence": ["example 1", "example 2"]}}
        ],
        "negativeAspects": [
            {{"name": "Delivery delay", "count": 2, "evidence": ["example 1", "example 2"]}}
        ],
        "summary": "Short summary of the analysis",
        "verdict": "General conclusion",
        "trends": [
            {{"name": "Global tone", "text": "4 positive reviews dominate the corpus."}},
            {{"name": "Recurring signal", "text": "Delivery appears most often in the critical reviews."}},
            {{"name": "Analysis base", "text": "6 reviews processed, including 1 neutral or mixed."}}
        ],
        "reviews": [
            {{"text": "original review", "sentiment": "positive", "score": 85}}
        ]
    }}
    
    Use only English labels in the JSON. Give me only the json.
    """
    
    response = model.generate_content(prompt)
    json_str = response.text.replace('```json', '').replace('```', '').strip()
    return json.loads(json_str)