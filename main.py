"""
FastAPI Backend for Local AI System
Now with RAG - AI answers from YOUR data
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
import time

from llm import ask_ai
from app.services.retriever import initialize, get_context

app = FastAPI(title="Local AI System", version="0.2.0")

# Initialize RAG on startup
initialize()


class QuestionRequest(BaseModel):
    text: str = Field(..., min_length=1)
    use_rag: Optional[bool] = True


class QuestionResponse(BaseModel):
    question: str
    answer: str
    context_used: str
    processing_time: float
    model: str
    rag_enabled: bool


@app.get("/")
def root():
    return {
        "status": "running",
        "message": "🤖 Local AI System with RAG",
        "model": "mistral-local",
        "version": "0.2.0 - RAG Enabled"
    }


@app.post("/ask", response_model=QuestionResponse)
def ask_question(request: QuestionRequest):
    start_time = time.time()

    try:
        if request.use_rag:
            context = get_context(request.text)
        else:
            context = None

        answer = ask_ai(request.text, context)
        processing_time = time.time() - start_time

        return QuestionResponse(
            question=request.text,
            answer=answer,
            context_used=context if context else "No RAG",
            processing_time=round(processing_time, 2),
            model="mistral-local",
            rag_enabled=request.use_rag
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health_check():
    try:
        test = ask_ai("Say OK")
        return {"status": "healthy", "ollama": "connected", "rag": "enabled"}
    except:
        return {"status": "unhealthy", "ollama": "disconnected"}