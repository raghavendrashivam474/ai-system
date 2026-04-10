"""
FastAPI Backend for Local AI System
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import time

from llm import ask_ai

app = FastAPI(title="Local AI System", version="0.1.0")


class QuestionRequest(BaseModel):
    text: str = Field(..., min_length=1)
    context: Optional[str] = None


class QuestionResponse(BaseModel):
    question: str
    answer: str
    processing_time: float
    model: str


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "🤖 Local AI System",
        "model": "mistral-local"
    }


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    start_time = time.time()
    
    try:
        answer = ask_ai(request.text, request.context)
        processing_time = time.time() - start_time
        
        return QuestionResponse(
            question=request.text,
            answer=answer,
            processing_time=round(processing_time, 2),
            model="mistral-local"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health_check():
    try:
        test = ask_ai("Say OK")
        return {"status": "healthy", "ollama": "connected"}
    except:
        return {"status": "unhealthy", "ollama": "disconnected"}
