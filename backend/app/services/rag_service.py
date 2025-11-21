from typing import List, Dict
from app.rag.retriever import Retriever
from app.rag.reranker import Reranker

class RAGService:
    def __init__(self):
        self.retriever = Retriever()
        self.reranker = Reranker()

    def query(self, query_text: str) -> Dict:
        # 1. Retrieve (fetch more candidates than needed)
        initial_docs = self.retriever.retrieve(query_text, k=20)
        
        # 2. Re-rank (refine to top results)
        final_docs = self.reranker.rerank(query_text, initial_docs, top_k=5)
        
        # 3. Format context
        context = "\n\n".join([doc.page_content for doc in final_docs])
        
        return {
            "query": query_text,
            "context": context,
            "source_documents": [{"content": doc.page_content, "metadata": doc.metadata} for doc in final_docs]
        }
