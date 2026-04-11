﻿<div align="center">

# 🤖 Local AI System with RAG

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/Ollama-0.20.4-orange)](https://ollama.com/)
[![Mistral](https://img.shields.io/badge/Mistral-7B-red)](https://mistral.ai/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-purple)](https://github.com/facebookresearch/faiss)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-RAG%20Complete-success)](README.md)

**RAG-Powered AI • FAISS Vector Search • Zero API Costs • 100% Local • Privacy First**

[Features](#-features) • [Architecture](#-architecture) • [Quick Start](#-quick-start) • [API Docs](#-api-endpoints) • [Roadmap](#-roadmap)

</div>

---

## 🎯 What This Does

AI that answers questions **from YOUR data** — not random internet knowledge.

```text
WITH RAG:    "Paracetamol 500mg, Rs 10, Brand Crocin"  ← YOUR data (5 sec)
WITHOUT RAG: "Several medications exist for fever..."   ← Generic (39 sec)
🎯 Features
✅ Local AI via Ollama + Mistral 7B
✅ RAG System — AI answers from YOUR data
✅ FAISS Vector Search — lightning fast retrieval
✅ Sentence Embeddings — semantic understanding
✅ FastAPI REST API with automatic documentation
✅ RAG ON/OFF Toggle — compare results instantly
✅ Context-aware responses with strict prompting
✅ Zero external dependencies for inference
✅ Privacy-focused — your data stays local
✅ Cost-effective — no API charges
✅ Production-ready architecture
🏗️ Architecture
text

┌─────────────────┐
│   User Query    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  FastAPI Server  │ ← main.py (Port 8000)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Retriever     │ ← retriever.py (RAG layer)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  FAISS Search   │ ← embeddings.py (Vector search)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Your Data      │ ← med_data.txt (Knowledge source)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  LLM Interface  │ ← llm.py (Context + Prompt)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Ollama Runtime  │ ← Local AI server
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Mistral 7B     │ ← 4.4GB model in memory
└─────────────────┘
RAG Flow (How it works):
text

"What medicine for fever?"
         ↓
   Convert to embedding (all-MiniLM-L6-v2)
         ↓
   Search FAISS index (find similar vectors)
         ↓
   Return top 3 matching chunks from YOUR data
         ↓
   Inject as context into Mistral prompt
         ↓
   "Paracetamol 500mg, Rs 10, Brand: Crocin"
🚀 Quick Start
Prerequisites
Python 3.10+
Ollama installed (download)
8GB+ RAM
10GB+ disk space
Installation
Bash

# 1. Clone repository
git clone https://github.com/YOUR-USERNAME/ai-system.git
cd ai-system

# 2. Install Ollama (if not installed)
# Download from: https://ollama.com/download

# 3. Pull Mistral model
ollama pull mistral

# 4. Set up Python environment
python -m venv .venv

# Activate virtual environment
# Windows:
.\.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# 5. Install dependencies
pip install -r requirements.txt
Run
Bash

# Start API server
uvicorn main:app --reload

# Server will run on: http://127.0.0.1:8000
Test
Open your browser:

API Docs: http://127.0.0.1:8000/docs
Health Check: http://127.0.0.1:8000/health
📡 API Endpoints
GET /
Health check and system info

Bash

curl http://127.0.0.1:8000/
Response:

JSON

{
  "status": "running",
  "message": "🤖 Local AI System with RAG",
  "model": "mistral-local",
  "version": "0.2.0 - RAG Enabled"
}
POST /ask (RAG-Powered)
Ask a question — AI searches YOUR data first

With RAG (default):

Bash

curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"text": "What medicine for fever?", "use_rag": true}'
Response:

JSON

{
  "question": "What medicine for fever?",
  "answer": "Paracetamol 500mg (Crocin, Rs 10) and Dolo 650mg (Rs 12) are used for fever.",
  "context_used": "Paracetamol 500mg is used for fever and mild pain...\nDolo 650mg contains paracetamol...",
  "processing_time": 5.84,
  "model": "mistral-local",
  "rag_enabled": true
}
Without RAG (generic AI):

Bash

curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"text": "What medicine for fever?", "use_rag": false}'
Response:

JSON

{
  "question": "What medicine for fever?",
  "answer": "There are several types of medications used to treat fever...(long generic response)",
  "context_used": "No RAG",
  "processing_time": 39.51,
  "model": "mistral-local",
  "rag_enabled": false
}
GET /health
Detailed system health check

Bash

curl http://127.0.0.1:8000/health
Response:

JSON

{
  "status": "healthy",
  "ollama": "connected",
  "rag": "enabled"
}
📁 Project Structure
text

ai-system/
├── .venv/                     # Virtual environment (not in git)
├── data/
│   └── med_data.txt           # Knowledge source (10 medicines)
├── app/
│   ├── __init__.py
│   └── services/
│       ├── __init__.py
│       ├── embeddings.py      # Text → vectors + FAISS index
│       └── retriever.py       # Query → relevant context
│
├── llm.py                     # Ollama/Mistral interface + strict prompting
├── main.py                    # FastAPI server with RAG integration
├── requirements.txt           # Python dependencies
├── .gitignore                 # Git ignore rules
└── README.md                  # This file
🔧 Tech Stack
Component	Technology	Purpose
LLM	Mistral 7B	Language model (4.4GB)
Runtime	Ollama 0.20.4	Local AI server
Embeddings	all-MiniLM-L6-v2	Text to vectors
Vector DB	FAISS	Similarity search
API Framework	FastAPI 0.109	REST API with auto docs
Server	Uvicorn 0.27	ASGI server
Validation	Pydantic 2.9+	Request/response validation
Language	Python 3.12	Core development
📊 Performance
Metric	RAG ON	RAG OFF
Response Time	~5s	~39s
Accuracy	From your data	Generic/hallucinated
Answer Length	Short & precise	Long & generic
Data Source	med_data.txt	Model's training data
System Requirements
Metric	Value	Notes
Model Size	4.4 GB	Loaded in RAM
RAM Usage	~6GB	During active inference
First Request	~20-30s	Includes model loading
Subsequent	2-5s	Model stays in memory
API Latency	<100ms	Excluding LLM processing
🧪 Example Usage
Interactive Python
Python

from llm import ask_ai

# Simple question
response = ask_ai("Explain AI in simple terms")
print(response)

# With context (RAG style)
context = "Paracetamol 500mg is used for fever. Price: Rs 10. Brand: Crocin."
response = ask_ai("What is paracetamol used for?", context=context)
print(response)
PowerShell
PowerShell

# RAG ON
$body = @{text = "What medicine for fever?"; use_rag = $true} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method POST -Body $body -ContentType "application/json"

# RAG OFF
$body = @{text = "What medicine for fever?"; use_rag = $false} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method POST -Body $body -ContentType "application/json"
Test Embeddings Directly
Bash

python app/services/embeddings.py
Test Retriever Directly
Bash

python -m app.services.retriever
🔍 Use Cases
1. MedSave AI Assistant
Medicine information lookup
Price comparison
Brand alternatives
Prescription analysis
2. DataSanity Intelligence
Data analysis Q&A
Report generation
Insight extraction
3. Document Q&A System
Upload custom data
Ask questions about content
Get sourced answers
Private data processing
🎯 Roadmap
✅ Phase 1: Foundation (Complete)
 Ollama + Mistral setup
 FastAPI backend
 Basic question answering
 Interactive API documentation
 Context injection capability
✅ Phase 2: RAG System (Complete)
 Knowledge source (med_data.txt)
 Sentence embeddings (all-MiniLM-L6-v2)
 FAISS vector store
 Retriever service
 RAG ↔ Mistral integration
 RAG ON/OFF toggle
 Strict prompting (answer only from data)
🚧 Phase 3: Improvements (Next)
 Better chunking for large datasets
 Larger medicine database
 Accuracy improvements
 Response caching
📅 Phase 4: Memory & Intelligence
 Conversation memory
 Context awareness across sessions
 Tool/function calling
 Advanced retrieval strategies
📅 Phase 5: Product Layer
 MedSave integration
 Multi-mode system
 Performance optimization
 Docker containerization
 Production deployment
🛠️ Development
Adding New Data
Edit data/med_data.txt and restart server. Each line = one knowledge chunk.

Adding New Endpoints
Python

# In main.py
@app.post("/your-endpoint")
def your_function(request: YourModel):
    context = get_context(request.text)
    answer = ask_ai(request.text, context)
    return {"result": answer}
🤝 Contributing
Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Ollama - Local LLM runtime
Mistral AI - Open-source model
FastAPI - Web framework
FAISS - Vector search by Meta
Sentence Transformers - Embedding models
<div align="center">
Phase 1 ✅ Foundation Complete | Phase 2 ✅ RAG Complete

Built locally • Zero API costs • Your data, your AI 🚀

⭐ Star this repo • 🐛 Report Bug • 💡 Request Feature

</div> ```