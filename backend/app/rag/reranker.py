from typing import List
from sentence_transformers import CrossEncoder
from langchain_core.documents import Document

class Reranker:
    def __init__(self, model_name: str = "cross-encoder/ms-marco-MiniLM-L-6-v2"):
        # Load the cross-encoder model (runs locally)
        self.model = CrossEncoder(model_name)

    def rerank(self, query: str, documents: List[Document], top_k: int = 5) -> List[Document]:
        """
        Re-rank a list of documents based on their relevance to the query.
        """
        if not documents:
            return []

        # Prepare pairs for the cross-encoder
        pairs = [[query, doc.page_content] for doc in documents]
        
        # Predict scores
        scores = self.model.predict(pairs)
        
        # Combine docs with scores
        doc_score_pairs = list(zip(documents, scores))
        
        # Sort by score descending
        sorted_pairs = sorted(doc_score_pairs, key=lambda x: x[1], reverse=True)
        
        # Return top_k documents
        return [doc for doc, score in sorted_pairs[:top_k]]
