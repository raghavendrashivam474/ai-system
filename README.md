﻿<div align="center">

# 🤖 Local AI System

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/Ollama-0.20.4-orange)](https://ollama.com/)
[![Mistral](https://img.shields.io/badge/Mistral-7B-red)](https://mistral.ai/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Day%201%20Complete-success)](README.md)

**Self-sufficient AI • RAG-ready • Zero API costs • 100% local**

[Features](#-features) • [Quick Start](#-quick-start) • [API Docs](#-api-endpoints) • [Roadmap](#-roadmap)

</div>

## 🎯 Features

- ✅ Local AI via Ollama + Mistral 7B
- ✅ FastAPI REST API
- ✅ Context-aware responses (RAG ready)
- ✅ Interactive API documentation
- ✅ Zero external dependencies for inference

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Ollama installed
- 8GB+ RAM

### Installation

```bash
# 1. Clone repository
git clone https://github.com/raghavendrashivam474/ai-system.git
cd ai-system

# 2. Install Ollama from https://ollama.com/download

# 3. Pull Mistral model
ollama pull mistral

# 4. Set up Python environment
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# 5. Install dependencies
pip install -r requirements.txt

### Run

```bash
uvicorn main:app --reload

Open: http://127.0.0.1:8000/docs

## 📡 API Endpoints

- **GET /** - Health check
- **POST /ask** - Ask questions to AI
- **GET /health** - System status

## 🔧 Tech Stack

- Mistral 7B (via Ollama)
- FastAPI
- Python 3.12
- Uvicorn

## 📊 Performance

- Model Size: 4.4GB
- First Request: ~24s
- RAM Usage: ~6GB

## 🎯 Roadmap

- [x] Week 1: Local AI setup
- [ ] Week 2: RAG with FAISS
- [ ] Week 3: Memory & tools
- [ ] Week 4: Production ready

## 📝 License

MIT

---

**Day 1 Complete** ✅
=======
﻿<div align="center">

# 🤖 Local AI System

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Ollama](https://img.shields.io/badge/Ollama-0.20.4-orange)](https://ollama.com/)
[![Mistral](https://img.shields.io/badge/Mistral-7B-red)](https://mistral.ai/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Day%201%20Complete-success)](README.md)

**Self-sufficient AI • RAG-ready • Zero API costs • 100% local**

[Features](#-features) • [Quick Start](#-quick-start) • [API](#-api-endpoints) • [Roadmap](#-roadmap)

</div>

---

## 🎯 Features

- ✅ **Local AI** via Ollama + Mistral 7B
- ✅ **FastAPI REST API** with automatic documentation
- ✅ **Context-aware responses** (RAG foundation)
- ✅ **Zero external dependencies** for inference
- ✅ **Privacy-focused** - your data stays local
- ✅ **Cost-effective** - no API charges
- ✅ **Production-ready** architecture

---

## 🏗️ Architecture

| Layer | Component | File | Description |
|-------|-----------|------|-------------|
| 1️⃣ | **User Interface** | - | Browser / API client |
| 2️⃣ | **API Server** | ``main.py`` | FastAPI on Port 8000 |
| 3️⃣ | **LLM Interface** | ``llm.py`` | Context injection & prompts |
| 4️⃣ | **AI Runtime** | Ollama | Local AI server |
| 5️⃣ | **Model** | Mistral 7B | 4.4GB neural network |

**Flow:** ``User Query → FastAPI → LLM Interface → Ollama → Mistral → Response``

---

## 🚀 Quick Start

### Prerequisites

- **Python 3.10+**
- **Ollama** installed ([download](https://ollama.com/download))
- **8GB+ RAM**
- **10GB+ disk space**

### Installation

```bash
# 1. Clone repository
git clone https://github.com/YOUR-USERNAME/ai-system.git
cd ai-system

# 2. Install Ollama (if not installed)
# Download from: https://ollama.com/download

# 3. Pull Mistral model
ollama pull mistral

# 4. Set up Python environment
python -m venv venv

# Activate virtual environment
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

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
  "message": "🤖 Local AI System",
  "model": "mistral-local"
}
POST /ask
Ask a question to the AI

Simple question:

Bash

curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"text": "What is machine learning?"}'
With context (RAG preview):

Bash

curl -X POST http://127.0.0.1:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
    "text": "What does this platform do?",
    "context": "MedSave helps users save money on medicines by comparing prices across pharmacies."
  }'
Response:

JSON

{
  "question": "What is machine learning?",
  "answer": "Machine learning is a subfield of artificial intelligence...",
  "processing_time": 2.45,
  "model": "mistral-local"
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
  "model": "mistral"
}
📁 Project Structure
text

ai-system/
├── venv/              # Virtual environment (not in git)
├── data/              # Data storage for RAG (coming soon)
├── logs/              # Application logs (coming soon)
│
├── llm.py            # ✅ AI interface layer
├── main.py           # ✅ FastAPI server
├── requirements.txt  # ✅ Python dependencies
├── .gitignore       # ✅ Git ignore rules
└── README.md        # ✅ This file
🔧 Tech Stack
Component	Technology	Purpose
LLM	Mistral 7B	Language model (4.4GB)
Runtime	Ollama 0.20.4	Local AI server
API Framework	FastAPI 0.109	REST API with auto docs
Server	Uvicorn 0.27	ASGI server
Validation	Pydantic 2.9+	Request/response validation
Language	Python 3.12	Core development
📊 Performance
Metric	Value	Notes
Model Size	4.4 GB	Loaded in RAM
First Request	~20-30s	Includes model loading
Subsequent	2-5s	Model stays in memory
RAM Usage	~6GB	During active inference
API Latency	<100ms	Excluding LLM processing
🎯 Roadmap
✅ Week 1: Foundation (Complete)
 Ollama + Mistral setup
 FastAPI backend
 Basic question answering
 Interactive API documentation
 Context injection capability
🚧 Week 2: RAG Implementation (In Progress)
 FAISS vector store integration
 Document chunking system
 Embeddings generation
 Semantic search
 Multi-source data ingestion
📅 Week 3: Intelligence Layer
 Conversation memory
 Tool/function calling
 Advanced retrieval strategies
 Response caching
📅 Week 4: Production Ready
 Performance optimization
 Monitoring & logging
 Error recovery
 Deployment guides
 Docker containerization
🧪 Example Usage
Interactive Python
Python

from llm import ask_ai

# Simple question
response = ask_ai("Explain AI in simple terms")
print(response)

# With context (RAG preview)
context = "MedSave is a healthcare platform for medicine discounts"
response = ask_ai("What is MedSave?", context=context)
print(response)
PowerShell
PowerShell

# Simple request
$body = @{text = "What is RAG?"} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method POST -Body $body -ContentType "application/json"

# With context
$body = @{
    text = "How much can I save?"
    context = "Users typically save 30% on medicines with MedSave"
} | ConvertTo-Json
Invoke-RestMethod -Uri "http://127.0.0.1:8000/ask" -Method POST -Body $body -ContentType "application/json"
🔍 Use Cases
1. MedSave AI Assistant
Medicine information lookup
Price comparison explanations
Prescription analysis
User query handling
2. DataSanity Intelligence
Data analysis Q&A
Report generation
Insight extraction
Onboarding assistance
3. Document Q&A System
Upload PDFs/CSVs
Ask questions about content
Get sourced answers
Private data processing
🛠️ Development
Running Tests
Bash

# Test LLM directly
python llm.py

# Test API
uvicorn main:app --reload
Adding New Endpoints
Python

# In main.py
@app.post("/your-endpoint")
def your_function(request: YourModel):
    # Your logic here
    return {"result": "success"}
🤝 Contributing
This is a learning project, but contributions are welcome!

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request
📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Ollama Team - Making local LLMs accessible
Mistral AI - Excellent open-source model
FastAPI - Amazing web framework
Community - For inspiration and support
📚 Learning Resources
Ollama Documentation
FastAPI Tutorial
Mistral AI Docs
RAG Explained
🔗 Related Projects
LangChain - AI application framework
LlamaIndex - Data framework for LLMs
Chroma - AI-native vector database
<div align="center">
Built as part of a 30-day AI learning journey 🚀

Day 1: ✅ Foundation Complete

⭐ Star this repo • 🐛 Report Bug • 💡 Request Feature

