from app.ingestion import load_document, split_documents
from app.vector_store import create_vector_store
from app.llm import create_llm
from app.rag import generate_answer


class RAGService:
    def __init__(self):
        documents = load_document("data/documents/example.md")
        chunks = split_documents(documents)

        self.vector_store = create_vector_store(chunks)
        self.llm = create_llm()

    def ask(self, question: str) -> str:
        results = self.vector_store.similarity_search(
            question,
            k=3,
        )

        context = "\n\n".join(
            result.page_content
            for result in results
        )

        answer = generate_answer(
            llm=self.llm,
            question=question,
            context=context,
        )

        return answer