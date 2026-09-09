
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_document(file_path: str):
    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()
    
    return documents


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30,
    )
    
    chunks = text_splitter.split_documents(documents)
    
    return chunks


def create_embedding_model():
    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )
    
    return embeddings