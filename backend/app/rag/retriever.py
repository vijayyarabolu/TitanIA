from typing import List
from langchain_core.documents import Document
from app.rag.vector_store import VectorStore

class Retriever:
    def __init__(self):
        self.vector_store = VectorStore()

    def retrieve(self, query: str, k: int = 10) -> List[Document]:
        """
        Retrieve top-k documents from the vector store based on semantic similarity.
        """
        return self.vector_store.similarity_search(query, k=k)
