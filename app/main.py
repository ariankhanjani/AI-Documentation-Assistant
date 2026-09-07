from app.ingestion import load_document, split_documents
from app.vector_store import create_vector_store
from app.llm import create_llm
from app.rag import generate_answer


def main():
    documents = load_document("data/documents/example.md")
    chunks = split_documents(documents)
    
    print(f"Total chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks, start=1):
        print(f"\n--- Chunk {i} ---")
        print(chunk.page_content)

    vector_store = create_vector_store(chunks)

    llm = create_llm()

    question = "How do I run this project using Docker?"

    results = vector_store.similarity_search(
        question,
        k=3,
    )
    
    
    print("\nRetrieved Context:\n")
    
    for i, result in enumerate(results, start=1):
        print(f"--- Chunk {i} ---")
        print(result.page_content)
        print()

    
    context = "\n\n".join(
    result.page_content
    for result in results
)

    context = "\n\n".join(
        result.page_content
        for result in results
    )

    answer = generate_answer(
        llm=llm,
        question=question,
        context=context,
    )

    print("\nQuestion:")
    print(question)

    print("\nAnswer:")
    print(answer)


if __name__ == "__main__":
    main()