from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from geminiservice import analyze_reviews
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

class ReviewRequest(BaseModel):
    reviews: str  # Review text

class AnalysisResponse(BaseModel):
    score: int
    positiveAspects: list
    negativeAspects: list
    summary: str
    verdict: str
    trends: list
    reviews: list

@app.post("/analyze")
async def analyze(request: ReviewRequest):
    print("Received request at", datetime.now())
    
    try:
        result = analyze_reviews(request.reviews)
        return result

    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
