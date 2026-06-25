# Document-AI v0.1

<p align="center">
  <img width="200px" height="200px" src="EDAI.png" alt="Document-AI Logo">
</p>

<h3 align="center">Insurance Policy Assistant</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-green.svg)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-1.47+-red.svg)]()

</div>

---

<p align="center">
Document-AI is an intelligent, session-based insurance assistant that combines semantic document retrieval using FAISS with reasoning powered by Gemini 1.5 Flash. Upload multiple policy documents, ask natural language questions, and receive structured, justified decisions in real time.
</p>

## Features

- **Multi-Document Upload** — Supports PDF and DOCX insurance policy documents
- **Session-Based Processing** — Each upload session is isolated for clean context separation
- **Semantic Search** — FAISS-based vector search for relevant policy clauses
- **AI-Powered Analysis** — Gemini 1.5 Flash for intelligent decision evaluation
- **Structured Responses** — JSON-formatted decisions with justification and clause references
- **Web Interface** — Streamlit-based UI for easy interaction
- **REST API** — FastAPI backend for programmatic access

## Table of Contents

- [About](#about)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

## About

Document-AI streamlines insurance policy analysis by providing instant, accurate answers to complex policy questions. The system processes uploaded documents through NLP techniques, creates semantic embeddings, and uses AI reasoning to evaluate claims and return structured decisions.

Key capabilities:
- **Document Ingestion** — Automatic parsing of PDF and DOCX files
- **Text Chunking** — Intelligent document segmentation for optimal retrieval
- **Vector Indexing** — FAISS-based similarity search across policy clauses
- **AI Reasoning** — Step-by-step analysis using Gemini 1.5 Flash
- **Session Management** — Clean separation between different document sets

## Architecture

```
Document-AI/
├── app/                    # Core application logic
│   ├── core/               # Engine, retriever, embedder
│   ├── ingestion/          # Document loading and chunking
│   └── main.py             # FastAPI entry point
├── ui/                     # Streamlit user interface
├── config/                 # Configuration files
├── data/                   # Session data and document storage
└── scripts/                # Utility scripts
```

### Core Components

| Component | Description |
|-----------|-------------|
| **Engine** | Handles AI reasoning and decision evaluation |
| **Retriever** | Manages FAISS index and semantic search |
| **Embedder** | Generates text embeddings using sentence transformers |
| **Ingestion** | Processes and chunks uploaded documents |

## Installation

### Prerequisites

- Python 3.12+
- Google Gemini API key
- Virtual environment (recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DOCUMENT-AI.v01
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # Unix / macOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your API key**

   Edit `config/config.yaml`:
   ```yaml
   gemini_api_key: "your_gemini_api_key_here"
   ```

## Usage

### Web Interface (Recommended)

1. **Start the backend**
   ```bash
   # From project root
   uvicorn app.main:app --reload

   # Or from the app directory
   cd app && uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Launch the UI**
   ```bash
   cd ui && streamlit run app.py
   ```

3. Upload PDF or DOCX policy documents, ask natural language questions, and receive structured decisions with justification.

### API Usage

**Upload documents:**
```bash
curl -X POST "http://localhost:8000/upload_docs" \
  -F "uploaded_files=@policy_document.pdf"
```

**Query documents:**
```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "Does this policy cover dental procedures?", "session_id": "your_session_id"}'
```

## API Reference

### `POST /upload_docs`

Upload and index insurance policy documents.

**Request:** Multipart form with PDF/DOCX files

**Response:**
```json
{
  "status": "success",
  "indexed_files": ["policy.pdf"],
  "session_id": "20241201_143022",
  "message": "All uploaded documents parsed and indexed into a single index."
}
```

### `POST /query`

Query indexed documents for policy analysis.

**Request:**
```json
{
  "query": "Does this policy cover heart surgery?",
  "session_id": "20241201_143022"
}
```

**Response:**
```json
{
  "query": "Does this policy cover heart surgery?",
  "response": {
    "decision": "approved",
    "amount": 50000,
    "justification": "Policy covers major surgeries including cardiac procedures."
  },
  "retrieved_clauses": ["relevant policy text..."]
}
```

## Configuration

All configuration is managed in `config/config.yaml`:

```yaml
gemini_api_key: "your_gemini_api_key_here"
```

## Project Structure

```
DOCUMENT-AI.v01/
├── app/
│   ├── core/
│   │   ├── embedder.py          # Text embedding generation
│   │   ├── engine.py            # AI reasoning engine
│   │   └── retriever.py         # FAISS index management
│   ├── ingestion/
│   │   ├── chunk.py             # Text chunking logic
│   │   └── load.py              # Document loading
│   └── main.py                  # FastAPI application
├── config/
│   └── config.yaml              # API keys and settings
├── data/
│   ├── docs/                    # Sample documents
│   └── session_*/               # Session-specific FAISS index and chunks
├── scripts/
│   ├── index_build.py
│   ├── ingestion_testing.py
│   └── test.py
├── temp_uploads/
├── ui/
│   └── app.py                   # Streamlit application
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Dependencies

### Web Framework
- **FastAPI** ≥ 0.116.1 — API backend
- **Uvicorn** ≥ 0.35.0 — ASGI server
- **Streamlit** ≥ 1.47.1 — Web UI

### AI & ML
- **Google Generative AI** ≥ 0.8.5 — Gemini 1.5 Flash
- **Sentence Transformers** ≥ 5.0.0 — Text embeddings
- **FAISS-CPU** ≥ 1.11.0 — Vector similarity search
- **LangChain** ≥ 0.3.26 — LLM framework

### Document Processing
- **PyMuPDF** ≥ 1.26.3 — PDF parsing
- **Python-DOCX** ≥ 1.2.0 — DOCX parsing
- **Unstructured** ≥ 0.18.9 — General document parsing

### Utilities
- **NumPy** ≥ 2.3.1, **Pandas** ≥ 2.3.1, **Pydantic** ≥ 2.11.7, **Tiktoken** ≥ 0.9.0

## Testing

```bash
cd scripts
python test.py
python ingestion_testing.py
python index_build.py
```

## Deployment

### Local Development
```bash
# Backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Frontend
cd ui && streamlit run app.py
```

### Production
1. Set up a production server and install dependencies
2. Configure environment variables
3. Use Gunicorn as the ASGI server
4. Set up a reverse proxy (nginx or Apache)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Add tests if applicable
5. Open a pull request

## Acknowledgments

- **Google Gemini** — AI reasoning capabilities
- **FAISS** — Efficient vector similarity search
- **FastAPI** & **Streamlit** — Web framework
- **Sentence Transformers** — High-quality text embeddings

## Support

Open an issue in the repository, or reach out to the development team:

### Development Team
[![LinkedIn](https://img.shields.io/badge/Arhant%20Bagde-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/arhant-bagde-8ab5111a0/)
[![LinkedIn](https://img.shields.io/badge/Aditya%20Bhagat-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/aditya-bhagat-13b3a2307/)
[![LinkedIn](https://img.shields.io/badge/Member%203-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/member3/)
[![LinkedIn](https://img.shields.io/badge/Member%204-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/member4/)
[![LinkedIn](https://img.shields.io/badge/Member%205-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/member5/)

---

**Document-AI v0.1** — Making insurance policy analysis intelligent and accessible.