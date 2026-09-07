from app.ingestion import (load_document,
                           split_documents,
                           create_embedding_model,
)

def main():
    documents = load_document("data/documents/example.md")
    chunks = split_documents(documents)
    
    embeddings = create_embedding_model()
    
    vector = embeddings.embed_query(
        "How do I run the application with Docker?"
    )
    
    print(f"Embedding dimensions: {len(vector)}")
    print(vector[:10])


if __name__ == "__main__":
    main()