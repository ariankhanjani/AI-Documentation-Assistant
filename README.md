# 📚 RAG Document Q&A API

A lightweight **Retrieval-Augmented Generation (RAG)** application that allows users to upload documents and ask questions about their content.

The application processes uploaded documents, converts their content into searchable vector representations, retrieves the most relevant context for a user query, and uses a **Hugging Face LLM** to generate an answer based on the retrieved information.

> **No external API key is required.** The application is designed to run locally using the included models and components.
>
> The Docker image is approximately **10 GB**, so building, downloading, or loading the image may take some time depending on your internet connection and system performance.

---

## ✨ Features

* 📄 Upload documents through a REST API
* 🔍 Semantic search over document content
* 🧠 Hugging Face embedding and language models
* 🔗 LangChain-based RAG pipeline
* 🤖 Retrieval-Augmented Generation (RAG)
* ⚡ FastAPI-based REST API
* 🐳 Dockerized application
* 📖 Interactive Swagger API documentation
* 🔑 No external API keys required
* 🧩 Modular architecture for future extensions

---

## 🏗️ Architecture

The project implements a standard RAG pipeline using **LangChain**, **Hugging Face models**, and a vector store for semantic retrieval.

```text
                         ┌─────────────────┐
                         │     Document    │
                         │      Upload     │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Text Extraction │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Text Chunking   │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │   HF Embedding  │
                         │      Model      │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  Vector Store   │
                         └────────┬────────┘
                                  │
                         User Question
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Semantic Search │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Relevant Context│
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  HF Language    │
                         │      Model      │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │  Final Answer   │
                         └─────────────────┘
```

The main idea is to **retrieve relevant information from the uploaded documents before generating an answer**, allowing the language model to answer questions using the document content as context.

---

## 🛠️ Tech Stack

| Technology          | Purpose                                                    |
| ------------------- | ---------------------------------------------------------- |
| **Python**          | Core programming language                                  |
| **FastAPI**         | REST API and backend                                       |
| **LangChain**       | RAG pipeline orchestration and document processing         |
| **Hugging Face**    | Local language and embedding models                        |
| **LLM**             | Context-aware answer generation                            |
| **Embedding Model** | Converts documents and queries into vector representations |
| **ChromaDB**        | Stores embeddings and performs semantic similarity search  |
| **Uvicorn**         | ASGI application server                                    |
| **Pydantic**        | Data validation and API schemas                            |
| **Docker**          | Application containerization                               |
| **PyTorch**         | Deep learning backend for local models                     |

### 🤖 AI Components

The application uses locally hosted **Hugging Face models**, eliminating the need for external LLM APIs or API keys.

The RAG system consists of two main model components:

* **Embedding Model** — generates vector representations of document chunks and user queries.
* **Language Model (LLM)** — generates the final answer using the retrieved document context.

LangChain connects these components and manages the overall retrieval and generation workflow.

---

## 📁 Project Structure

```text
rag-project/
│
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── api/                 # API endpoints
│   ├── services/            # RAG and application logic
│   ├── models/              # Data models and schemas
│   └── utils/                # Utility functions
│
├── tests/                   # Tests
│
├── documents/               # Document storage
│
├── Dockerfile               # Docker image configuration
├── requirements.txt         # Python dependencies
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have one of the following environments available:

* Python 3.10+
* Docker

No external API key is required.

---

## 🐳 Run with Docker

The recommended way to run the application is using Docker.

### 1. Clone the repository

```bash
git clone https://github.com/ariankhanjani/<repository-name>.git
cd <repository-name>
```

### 2. Build the Docker image

```bash
docker build -t rag-api .
```

### 3. Run the container

```bash
docker run -p 8000:8000 rag-api
```

The API will then be available at:

```text
http://localhost:8000
```

---

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

Open:

```text
http://localhost:8000/docs
```

You can use Swagger UI to:

1. Upload a document
2. Send questions
3. Test the RAG pipeline
4. Inspect API responses

No additional frontend is required to test the application.

---

## 💻 Run Locally

You can also run the project directly with Python.

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Activate the environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

---

## 🔄 RAG Pipeline

The complete workflow can be summarized as:

```text
Document
   ↓
Text Extraction
   ↓
Text Chunking
   ↓
Hugging Face Embeddings
   ↓
Vector Store
   ↓
Similarity Search
   ↓
Relevant Context
   ↓
Hugging Face LLM
   ↓
Generated Answer
```

When a user asks a question, the system:

1. Converts the query into an embedding.
2. Searches the vector store for semantically similar document chunks.
3. Retrieves the most relevant context.
4. Passes the retrieved context and user question to the LLM.
5. Generates the final answer based on the retrieved information.

---

## 🧪 Testing

Run the test suite with:

```bash
pytest
```

You can also test the API interactively through Swagger:

```text
http://localhost:8000/docs
```

---

## 🔮 Future Improvements

Some possible improvements for future versions:

* [ ] Support for additional document formats
* [ ] Persistent vector database
* [ ] Conversation history
* [ ] Streaming responses
* [ ] Reranking for improved retrieval
* [ ] RAG evaluation and benchmarking
* [ ] Authentication and user management
* [ ] Web-based frontend
* [ ] CI/CD pipeline
* [ ] Production deployment

---

## 🎯 Project Goal

The goal of this project is to demonstrate a practical **end-to-end RAG system**, from document ingestion and semantic retrieval to local LLM-powered question answering.

The project also focuses on practical software engineering concepts such as:

* REST API development
* RAG architecture
* LLM application development
* LangChain integration
* Hugging Face model integration
* Modular application design
* Docker containerization
* Dependency management
* Automated testing

It can serve as a foundation for applications such as:

* 📚 Document Q&A systems
* 🏢 Internal knowledge assistants
* 🔬 Research assistants
* 📄 Document analysis tools
* 💬 AI-powered support systems

---

## 📜 License

This project is licensed under the **MIT License**.
