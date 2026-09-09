from pathlib import Path
from pydantic import BaseModel
from app.services import RAGService
from fastapi.responses import PlainTextResponse
from fastapi import FastAPI, UploadFile, File, HTTPException



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


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    allowed_extensions = {".txt", ".md"}

    extension = Path(file.filename).suffix.lower()

    if extension not in allowed_extensions:
        raise HTTPException(
            status_code=400,
            detail="Only .txt and .md files are supported.",
        )

    upload_dir = Path("data/documents/uploads")
    upload_dir.mkdir(parents=True, exist_ok=True)

    file_path = upload_dir / Path(file.filename).name

    content = await file.read()

    with open(file_path, "wb") as f:
        f.write(content)

    chunks_count = rag_service.add_document(str(file_path))

    return {
        "filename": file.filename,
        "chunks_added": chunks_count,
        "message": "Document uploaded and indexed successfully.",
    }


@app.post("/ask", response_class=PlainTextResponse)
def ask_question(request: QuestionRequest):
    answer = rag_service.ask(request.question)

    return answer