<div align="center">

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

\\\ash
# 1. Clone repository
git clone <your-repo-url>
cd ai-system

# 2. Install Ollama from https://ollama.com/download

# 3. Pull Mistral model
ollama pull mistral

# 4. Set up Python environment
python -m venv venv
.\venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements.txt
\\\

### Run

\\\ash
uvicorn main:app --reload
\\\

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
