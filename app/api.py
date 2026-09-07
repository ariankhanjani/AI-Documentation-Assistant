from fastapi import FastAPI
from pydantic import BaseModel

from app.services import RAGService


app = FastAPI(
    title="AI Documentation Assistant",
    description="RAG-based technical documentation assistant",
    version="0.1.0",
)


class QuestionRequest(BaseModel):
    question: str


rag_service = RAGService()


@app.get("/")
def root():
    return {
        "message": "AI Documentation Assistant is running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = rag_service.ask(request.question)

    return {
        "answer": answer
    }