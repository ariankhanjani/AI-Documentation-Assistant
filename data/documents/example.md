# AI Documentation Assistant

## Introduction

AI Documentation Assistant is a RAG-based application designed to answer questions about technical documentation. The system uses document retrieval and a language model to generate grounded answers.

## Installation

To install the project, create a Python virtual environment:

python -m venv .venv

Then activate the environment and install the dependencies:

pip install -r requirements.txt

## Configuration

The application uses environment variables for configuration. Create a .env file in the project root and define the required variables.

The application requires an API key for accessing the language model service.

## Docker

The application can be started using Docker Compose:

docker compose up --build

Docker Compose starts all required services and exposes the application on port 8000.

## API

The application exposes a REST API on port 8000.

You can access the API documentation at:

/docs

The main endpoint accepts a user question and returns an answer generated using the RAG pipeline.

## Troubleshooting

If the application does not start, first check whether all required environment variables are configured correctly.

You should also check the application logs and verify that port 8000 is not already being used by another process.

## Architecture

The system consists of several components including document loaders, text splitters, embedding models, a vector database, and a language model.

Documents are first loaded and split into smaller chunks. The chunks are then converted into vector embeddings and stored in ChromaDB.

When a user submits a question, the system retrieves the most relevant chunks from the vector database and provides them as context to the language model.

## Future Improvements

Future versions may include document upload through a FastAPI endpoint, authentication, evaluation of retrieval quality, monitoring, and support for multiple knowledge bases.