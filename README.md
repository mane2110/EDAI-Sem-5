# Document-AI v0.1

<p align="center">
  <img width=200px height=200px src="EDAI.png" alt="Document-AI Logo">
</p>

<h3 align="center">Insurance Policy Assistant v0.1</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-green.svg)]()
[![Streamlit](https://img.shields.io/badge/Streamlit-1.47+-red.svg)]()

</div>

---

<p align="center">
Document-AI is an intelligent, session-based insurance assistant that combines semantic document retrieval using FAISS with reasoning powered by Gemini 1.5 Flash. Users can upload multiple policy documents, ask natural language questions, and receive structured, justified decisions in real time.
</p>

##  Features

- **Multi-Document Upload**: Support for PDF and DOCX insurance policy documents
- **Session-Based Processing**: Each upload session is isolated for clean context separation
- **Semantic Search**: FAISS-based vector search for relevant policy clauses
- **AI-Powered Analysis**: Gemini 1.5 Flash for intelligent decision evaluation
- **Structured Responses**: JSON-formatted decisions with justification and clause references
- **Real-Time Processing**: Instant analysis and response generation
- **Web Interface**: Streamlit-based user interface for easy interaction
- **REST API**: FastAPI backend for programmatic access

##  Table of Contents

- [About](#about)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Contributing](#contributing)

##  About

Document-AI is designed to streamline insurance policy analysis by providing instant, accurate answers to complex policy questions. The system processes uploaded documents through advanced NLP techniques, creates semantic embeddings, and uses AI reasoning to evaluate claims and provide structured decisions.

Key capabilities:
- **Document Ingestion**: Automatic parsing of PDF and DOCX files
- **Text Chunking**: Intelligent document segmentation for optimal retrieval
- **Vector Indexing**: FAISS-based similarity search for relevant clauses
- **AI Reasoning**: Step-by-step analysis using Gemini 1.5 Flash
- **Session Management**: Clean separation between different document sets

##  Architecture

The system follows a modular architecture with clear separation of concerns:

```
Document-AI/
├── app/                    # Core application logic
│   ├── core/             # Core components (engine, retriever, embedder)
│   ├── ingestion/        # Document loading and chunking
│   └── main.py          # FastAPI application entry point
├── ui/                   # Streamlit user interface
├── config/               # Configuration files
├── data/                 # Session data and document storage
└── scripts/              # Utility scripts
```

### Core Components

- **Engine**: Handles AI reasoning and decision evaluation
- **Retriever**: Manages FAISS index and semantic search
- **Embedder**: Generates text embeddings using sentence transformers
- **Ingestion**: Processes and chunks uploaded documents

##  Installation

### Prerequisites

- Python 3.12 or higher
- Google Gemini API key
- Virtual environment (recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd DOCUMENT-AI.v01
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On Unix/MacOS
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API keys**
   ```bash
   # Edit config/config.yaml
   gemini_api_key: "your_gemini_api_key_here"
   ```

##  Usage

### Web Interface (Recommended)

1. **Start the backend API**
   ```bash
   cd app
   uvicorn main:app --reload --host 0.0.0.0 --port 8000

OR 

  cd F:\REQUIREMENT-EDAI-EM\DOCUMENT-AI.v01
  uvicorn app.main:app --reload
   ```

2. **Launch the Streamlit interface**
   ```bash
   cd ui
   streamlit run app.py
   ```

3. **Upload documents and ask questions**
   - Upload PDF or DOCX insurance policy documents
   - Ask natural language questions about coverage
   - Receive structured decisions with justification

### API Usage

#### Upload Documents
```bash
curl -X POST "http://localhost:8000/upload_docs" \
  -F "uploaded_files=@policy_document.pdf"
```

#### Query Documents
```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"query": "Does this policy cover dental procedures?", "session_id": "session_id"}'
```

## 🔌 API Reference

### Endpoints

#### `POST /upload_docs`
Upload and index insurance policy documents.

**Request**: Multipart form with PDF/DOCX files
**Response**: 
```json
{
  "status": "success",
  "indexed_files": [...],
  "session_id": "20241201_143022",
  "message": "All uploaded documents parsed and indexed into a single index."
}
```

#### `POST /query`
Query indexed documents for policy analysis.

**Request**:
```json
{
  "query": "Does this policy cover heart surgery?",
  "session_id": "20241201_143022"
}
```

**Response**:
```json
{
  "query": "Does this policy cover heart surgery?",
  "response": {
    "decision": "approved",
    "amount": 50000,
    "justification": "Policy covers major surgeries including cardiac procedures"
  },
  "retrieved_clauses": ["relevant policy text..."]
}
```

## Configuration

The system configuration is managed through `config/config.yaml`:

```yaml
# API keys and settings
gemini_api_key: "your_gemini_api_key_here"
```

##  Project Structure

```
DOCUMENT-AI.v01/
├── app/                           # Core application
│   ├── __pycache__/
│   ├── core/                     # Core components
│   │   ├── __pycache__/
│   │   ├── embedder.py          # Text embedding generation
│   │   ├── engine.py            # AI reasoning engine
│   │   └── retriever.py         # FAISS index management
│   ├── ingestion/               # Document processing
│   │   ├── __pycache__/
│   │   ├── chunk.py             # Text chunking logic
│   │   └── load.py              # Document loading
│   └── main.py                  # FastAPI application
├── config/                       # Configuration files
│   └── config.yaml              # API keys and settings
├── data/                         # Data storage
│   ├── docs/                    # Sample documents
│   └── session_*/               # Session-specific data
│       └── backup/              # FAISS index and chunks
├── scripts/                      # Utility scripts
│   ├── index_build.py           # Index building utilities
│   ├── ingestion_testing.py     # Testing scripts
│   └── test.py                  # General testing
├── temp_uploads/                 # Temporary file storage
├── ui/                          # User interface
│   ├── app.py                   # Streamlit application
│   └── app.txt                  # UI configuration
├── pyproject.toml               # Project metadata
├── requirements.txt              # Python dependencies
├── README.md                    # This file
└── VeriSureAI.svg              # Project logo
```

##  Dependencies

### Core Dependencies
- **FastAPI** (≥0.116.1) - Modern web framework for building APIs
- **Streamlit** (≥1.47.1) - Web application framework
- **Uvicorn** (≥0.35.0) - ASGI server

### AI & ML
- **Google Generative AI** (≥0.8.5) - Gemini 1.5 Flash integration
- **Sentence Transformers** (≥5.0.0) - Text embedding generation
- **FAISS-CPU** (≥1.11.0) - Vector similarity search
- **LangChain** (≥0.3.26) - LLM framework

### Document Processing
- **PyMuPDF** (≥1.26.3) - PDF processing
- **Python-DOCX** (≥1.2.0) - DOCX processing
- **Unstructured** (≥0.18.9) - Document parsing

### Utilities
- **NumPy** (≥2.3.1) - Numerical computing
- **Pandas** (≥2.3.1) - Data manipulation
- **Pydantic** (≥2.11.7) - Data validation
- **Tiktoken** (≥0.9.0) - Token counting

##  Deployment

### Local Development
```bash
# Backend
cd app && uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Frontend
cd ui && streamlit run app.py
```

### Production Deployment
1. Set up a production server
2. Install dependencies
3. Configure environment variables
4. Use a production ASGI server like Gunicorn
5. Set up reverse proxy (nginx/Apache)

##  Testing

Run the testing scripts to verify system functionality:

```bash
cd scripts
python test.py
python ingestion_testing.py
python index_build.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Acknowledgments

- **Google Gemini** for providing the AI reasoning capabilities
- **FAISS** for efficient vector similarity search
- **FastAPI** and **Streamlit** for the robust web framework
- **Sentence Transformers** for high-quality text embeddings

## Support

For questions and support, please open an issue in the repository or contact the development team:

### Development Team
- [![LinkedIn](https://img.shields.io/badge/Arhant%20Bagde-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/arhant-bagde-8ab5111a0/)
- [![LinkedIn](https://img.shields.io/badge/Aditya%20Bhagat-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/aditya-bhagat-13b3a2307/)
- [![LinkedIn](https://img.shields.io/badge/Anish%20Mane-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/anish-mane-281391384/)
- [![LinkedIn](https://img.shields.io/badge/Member%204-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/member4/)
- [![LinkedIn](https://img.shields.io/badge/Member%205-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/member5/)


**Document-AI v0.1** - Making insurance policy analysis intelligent and accessible.