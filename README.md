# 🤖 Local AI System

**Self-sufficient AI system running Mistral via Ollama - 100% local, no API calls**

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
