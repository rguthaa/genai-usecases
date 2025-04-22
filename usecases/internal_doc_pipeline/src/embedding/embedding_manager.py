# embedding/embedding_manager.py
from typing import List
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings

class EmbeddingManager:
    def __init__(self, model_type: str = "openai"):
        if model_type == "huggingface":
            self.embedding_model = HuggingFaceEmbeddings()
        else:
            self.embedding_model = OpenAIEmbeddings()
        self.vectorstore = None

    def save_embeddings(self, documents: List[Document], persist_directory: str):
        valid_docs = []
        for doc in documents:
            content = doc.page_content.strip()
            if content:
                valid_docs.append(doc)
            else:
                print(f"⚠️ Skipping empty document from: {doc.metadata.get('source')}")

        if not valid_docs:
            raise ValueError("No valid documents with content to embed.")

        try:
            self.vectorstore = Chroma.from_documents(
                valid_docs,
                self.embedding_model,
                persist_directory=persist_directory
            )
        except Exception as e:
            raise RuntimeError(f"Failed to save embeddings to vectorstore: {e}")

    def load_vectorstore(self, persist_directory: str):
        self.vectorstore = Chroma(
            persist_directory=persist_directory,
            embedding_function=self.embedding_model
        )

    def similarity_search(self, query: str, k: int = 4) -> List[Document]:
        return self.vectorstore.similarity_search(query, k=k)
